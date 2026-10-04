#!/usr/bin/env python3
"""
Đổi:  **9. CHUYỆN VUA MAKHÀDEVA (Tiền thân Makhàdeva)**
Thành: ### 9. CHUYỆN VUA MAKHÀDEVA (Tiền thân Makhàdeva)
cho danh sách file chỉ định.
"""
import re
import sys
from pathlib import Path

# ====== CẤU HÌNH ======
FILES = [
# "/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-054-tap-9-pham-1-tap-mot-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-055-tap-9-pham-2-tap-hai-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-056-tap-9-pham-3-tap-ba-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-057-tap-9-pham-4-tap-bon-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-058-tap-9-pham-5-tap-nam-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-059-tap-9-pham-6-tap-sau-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-060-tap-9-pham-7-tap-bay-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-061-tap-9-pham-8-tap-tam-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-062-tap-9-pham-9-tap-chin-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-063-tap-9-pham-10-tap-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-064-tap-9-pham-11-tap-muoi-hai-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-065-tap-9-pham-12-tap-muoi-sau-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-066-tap-9-pham-13-tap-hai-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-067-tap-9-pham-14-tap-ba-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-068-tap-9-pham-15-tap-bon-muoi-ke.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-069-tap-9-pham-16-dai-pham.md",
]

PATTERN = re.compile(r"\*\*(\d+\..+?)\*\*")   # regex tìm
PATTERN = re.compile(
    r"\*\*((?:\d+\..+?|\([IVXLCDM]+\).+?))\*\*\s*(\{#\d+(?:\.\d+)?\})"
)

REPLACEMENT = r"### \1"                        # thay thế
ENCODING = "utf-8"
DRY_RUN = False                                # True = chỉ in, không ghi
# ======================


def process_file(path: Path) -> int:
    if not path.is_file():
        print(f"⚠️  Bỏ qua (không tồn tại): {path}", file=sys.stderr)
        return 0

    text = path.read_text(encoding=ENCODING)
    new_text, count = PATTERN.subn(REPLACEMENT, text)

    if count == 0:
        print(f"➖ Không có thay đổi: {path}")
        return 0

    if DRY_RUN:
        print(f"🔍 [DRY-RUN] {path}: {count} thay đổi")
    else:
        # backup 1 lần duy nhất
        #backup = path.with_suffix(path.suffix + ".bak")
        #if not backup.exists():
        #    backup.write_text(text, encoding=ENCODING)
        path.write_text(new_text, encoding=ENCODING)
        # print(f"✅ {path}: {count} thay đổi (backup: {backup.name})")

    return count


def main():
    total = 0
    for f in FILES:
        total += process_file(Path(f))
    print(f"\n🎉 Tổng cộng: {total} thay đổi trong {len(FILES)} file.")


if __name__ == "__main__":
    main()