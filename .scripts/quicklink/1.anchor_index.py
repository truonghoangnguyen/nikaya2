
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
    # --------------------------------------------------------
    # Case:
    # **(I) Subhùti (Thera. 1)**
    # -> {#1}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^\*\*\(([IVXLCDM]+)\)\s+(.+?)\*\*[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: str(roman_to_int(m.group(1))),
    },
    # --------------------------------------------------------
    # Case:
    # ### **(I) Subhùti (Thera. 1)**
    # -> {#1}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^### \*\*\(([IVXLCDM]+)\)\s+(.+?)\*\*[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: str(roman_to_int(m.group(1))),
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

            return f"{header} {{#{anchor}}}"

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


"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-054-tap-9-pham-1-tap-mot-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-055-tap-9-pham-2-tap-hai-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-056-tap-9-pham-3-tap-ba-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-057-tap-9-pham-4-tap-bon-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-058-tap-9-pham-5-tap-nam-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-059-tap-9-pham-6-tap-sau-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-060-tap-9-pham-7-tap-bay-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-061-tap-9-pham-8-tap-tam-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-062-tap-9-pham-9-tap-chin-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-063-tap-9-pham-10-tap-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-064-tap-9-pham-11-tap-muoi-hai-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-065-tap-9-pham-12-tap-muoi-sau-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-066-tap-9-pham-13-tap-hai-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-067-tap-9-pham-14-tap-ba-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-068-tap-9-pham-15-tap-bon-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/t/kn-069-tap-9-pham-16-dai-pham.md"

]

for file in files:
    process_file(file)