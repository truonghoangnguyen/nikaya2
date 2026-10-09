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
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-1-kammakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-2-parivasikakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-3-samuccayakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-4-samathakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-5-khuddakavatthukkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-6-senasanakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-7-sanghabhedakakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-8-vattakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-9-patimokkhatthapanakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-10-bhikkhunikkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-11-pancasatikakkhandhaka.md",
"/Users/ng/projects/nikaya2/docs/vinaya-vi/kd/cv/pli-tv-kd-12-sattasatikakkhandhaka.md",
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