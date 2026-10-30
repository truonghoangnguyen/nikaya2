
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
    # Case: SN pali
    # ### 1.3 Upanīyasutta
    # -> {#3}
    #
    # Lấy segment số cuối cùng làm anchor
    # (khác rule 2 ở chỗ: KHÔNG có dấu chấm ở cuối)
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(#{2,})\s+(\d+(?:\.\d+)+)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: m.group(2).split(".")[-1],
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
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-002-devaputtasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-003-kosalasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-004-marasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-005-bhikkhunisamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-006-brahmasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-007-brahmanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-008-vangisasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-009-vanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-010-yakkhasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-011-sakkasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-012-nidanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-013-abhisamayasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-014-dhatusamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-015-anamataggasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-016-kassapasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-017-labhasakkarasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-018-rahulasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-019-lakkhanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-020-opammasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-021-bhikkhusamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-022-khandhasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-023-radhasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-024-ditthisamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-025-okkantasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-026-uppadasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-027-kilesasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-028-sariputtasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-029-nagasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-030-supannasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-031-gandhabbakayasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-032-valahakasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-033-vacchagottasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-034-jhanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-035-salayatanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-036-vedanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-037-matugamasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-038-jambukhadakasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-039-samandakasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-040-moggallanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-041-cittasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-042-gamanisamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-043-asankhatasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-044-abyakatasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-045-maggasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-046-bojjhangasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-047-satipatthanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-048-indriyasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-049-sammappadhanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-050-balasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-051-iddhipadasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-052-anuruddhasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-053-jhanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-054-anapanasamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-055-sotapattisamyutta.md",
"/Users/ng/projects/nikaya2/docs/kinhtuongung/pali-vi/sn-056-saccasamyutta.md",
]

for file in files:
    process_file(file)