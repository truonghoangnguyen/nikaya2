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
            r"^(###)\s+\(([IVXLCDM]+)\)\s+(.+?)[ \t]*$",
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
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-1-mahakhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-2-uposathakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-3-vassupanayikakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-4-pavaranakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-5-cammakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-6-bhesajjakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-7-kathinakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-8-civarakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-9-campeyyakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/mv/pli-tv-kd-10-kosambakakkhandhaka.md"
]

for file in files:
    process_file(file)