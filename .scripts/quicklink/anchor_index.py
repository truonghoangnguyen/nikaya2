import re
from pathlib import Path


# ============================================================
# 1. CÁC RULE HEADER
# ============================================================

RULES = [
    # --------------------------------------------------------
    # Case: #### (XXI) (Ek II, 4) (It. 7)
    #       -> {#21}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(####)\s+\(([IVXLCDM]+)\)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: str(roman_to_int(m.group(2))),
    },

    # --------------------------------------------------------
    # Case:
    # ## 2. Giới đức (Sīla)
    # ### 2.1. Giới đức nhỏ (Cūḷasīla)
    #
    # -> {#2}
    # -> {#2.1}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(#{2,})\s+(\d+(?:\.\d+)*\.)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: m.group(2).rstrip("."),
    },
    # --------------------------------------------------------
    # Case:
    # ### AN 10.189 Con Đường Thiện Lành Ariyamaggasutta
    # ### AN 1.11--20 Nīvaraṇappahānavagga
    #
    # -> {#189}
    # -> {#11-20}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(#{2,})\s+SN\s+\d+\.(\d+(?:\s*(?:--|–|-)\s*\d+)?)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: re.sub(
            r"\s*(?:--|–|-)\s*",
            "-",
            m.group(2)
        ),
    },
]


# ============================================================
# 2. ROMAN -> INTEGER
# ============================================================

def roman_to_int(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    prev = 0

    for char in reversed(s.upper()):
        value = values[char]

        if value < prev:
            total -= value
        else:
            total += value

        prev = value

    return total


# ============================================================
# 3. XỬ LÝ FILE
# ============================================================

def process_file(filename):
    path = Path(filename)
    content = path.read_text(encoding="utf-8")

    original_content = content

    for rule in RULES:

        def replace(match):
            header = match.group(0).rstrip()

            # Không thêm anchor nếu đã có
            if re.search(r"\{#[^}]+\}\s*$", header):
                return header

            anchor = rule["anchor"](match)

            return f"{header}{{#{anchor}}}"

        content = rule["regex"].sub(replace, content)

    if content != original_content:
        path.write_text(content, encoding="utf-8")
        print(f"Updated: {filename}")
    else:
        print(f"No change: {filename}")


# ============================================================
# 4. INPUT = LIST FILES
# ============================================================

files = [
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-01-linked-discourses-with-deities.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-02-linked-discourses-on-gods.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-03-linked-discourses-with-king-pasenadi-of-kosala.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-04-linked-discourses-with-mara.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-05-linked-discourses-with-nuns.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-06-linked-discourses-with-brahma-gods.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-07-linked-discourses-with-brahmins.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-08-linked-discourses-with-vangisa.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-09-linked-discourses-in-the-woods.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-10-linked-discourses-with-spirits.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-11-linked-discourses-with-sakka.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-12-linked-discourses-on-causation.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-13-linked-discourses-on-comprehension.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-14-linked-discourses-on-the-elements.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-15-linked-discourses-on-the-unknowable-beginning.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-16-linked-discourses-with-kassapa.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-17-linked-discourses-on-gains-and-honor.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-18-linked-discourses-with-rahula.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-19-linked-discourses-with-lakkhana.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-20-linked-discourses-with-similes.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-21-linked-discourses-with-monks.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-22-linked-discourses-on-the-aggregates.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-23-linked-discourses-with-radha.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-24-linked-discourses-on-views.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-25-linked-discourses-on-arrival-at-the-truth.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-26-linked-discourses-on-arising.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-27-linked-discourses-on-corruptions.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-28-linked-discourses-with-sariputta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-29-linked-discourses-on-dragons.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-30-linked-discourses-on-phoenixes.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-31-linked-discourses-on-centaurs.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-32-linked-discourses-on-cloud-gods.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-33-linked-discourses-with-vacchagotta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-34-linked-discourses-on-absorption.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-35-linked-discourses-on-the-six-sense-fields.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-36-linked-discourses-on-feelings.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-37-linked-discourses-on-females.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-38-linked-discourses-with-jambukhadaka.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-39-linked-discourses-with-samandaka.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-40-linked-discourses-with-moggallana.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-41-linked-discourses-with-citta-the-householder.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-42-linked-discourses-with-chiefs.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-43-linked-discourses-on-the-unconditioned.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-44-linked-discourses-on-the-undeclared.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-45-linked-discourses-on-the-eightfold-path.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-46-linked-discourses-on-the-awakening-factors.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-47-linked-discourses-on-mindfulness-meditation.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-48-linked-discourses-on-the-faculties.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-49-linked-discourses-on-the-right-efforts.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-50-linked-discourses-on-the-five-powers.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-51-linked-discourses-on-the-bases-of-psychic-power.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-52-linked-discourses-with-anuruddha.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-53-linked-discourses-on-absorption.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-54-linked-discourses-on-breath-meditation.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-55-linked-discourses-on-stream-entry.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/sujato-vi/sn-56-linked-discourses-on-the-truths.md",
]

for file in files:
    process_file(file)