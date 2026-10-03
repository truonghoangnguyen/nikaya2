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
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-072-tap-10-p1-pham-apannaka\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-073-tap-10-p1-pham-gioi\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-074-tap-10-p1-pham-kurunga\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-075-tap-10-p1-pham-kulavaka\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-076-tap-10-p1-pham-loi-ai\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-077-tap-10-p1-pham-asimsa\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-078-tap-10-p1-pham-nu-nhan\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-079-tap-10-p1-pham-varana\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-080-tap-10-p1-pham-apayimha\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-081-tap-10-p1-pham-litta\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-082-tap-10-p1-pham-parossata\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-083-tap-10-p1-pham-hamsa\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-084-tap-10-p1-pham-kusanali\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-085-tap-10-p1-pham-asampadana\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-086-tap-10-p1-pham-kakantaka\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-087-tap-10-p2-chuong-2\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-088-tap-10-p2-pham-dalha\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-089-tap-10-p2-pham-santahava\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-090-tap-10-p2-pham-thien-phap\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-091-tap-10-p2-pham-asadisa\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-092-tap-10-p2-pham-ruhaka\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-093-tap-10-p2-pham-natamdaiha\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-094-tap-10-p2-pham-biranatthambahaka-dam-co-thom\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-095-tap-10-p2-pham-kasava\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-096-tap-10-p2-pham-upahana\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-097-tap-10-p2-pham-sigala-cho-rung\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-098-tap-10-p3-chuong-iii-chuong-iv\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-099-tap-10-p3-chuong-3-pham-sankappa\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-100-tap-10-p3-chuong-3-pham-kosya\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-101-tap-10-p3-chuong-3-pham-ba-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-102-tap-10-p3-chuong-3-pham-ba-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-103-tap-10-p3-chuong-3-pham-ba-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-104-tap-10-p3-chuong-4-pham-bon-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-105-tap-10-p3-chuong-4-pham-bon-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-106-tap-10-p3-chuong-4-pham-bon-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-107-tap-10-p3-chuong-4-pham-bon-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-108-tap-10-p3-chuong-4-pham-bon-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-109-tap-10-p4-chuong-v-den-chuong-xxii\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-110-tap-10-p4-chuong-v-pham-nam-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-111-tap-10-p4-chuong-vi-pham-sau-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-112-tap-10-p4-chuong-vii-pham-bay-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-113-tap-10-p4-chuong-viii-pham-tam-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-114-tap-10-p4-chuong-ix-pham-chin-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-115-tap-10-p4-chuong-x-pham-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-116-tap-10-p4-chuong-xi-pham-muoi-mot-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-117-tap-10-p4-chuong-xii-pham-muoi-hai-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-118-tap-10-p5-chuong-xiii-den-chuong-xx\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-119-tap-10-p5-chuong-xiii-pham-muoi-ba-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-120-tap-10-p5-chuong-xiv-tap-pham\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-121-tap-10-p5-chuong-xv-pham-hai-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-122-tap-10-p5-chuong-xvi-pham-ba-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-123-tap-10-p5-chuong-xvii-pham-bon-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-124-tap-10-p5-chuong-xviii-pham-nam-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-125-tap-10-p5-chuong-xix-pham-sau-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-126-tap-10-p5-chuong-xx-pham-bay-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-127-tap-10-p6-chuong-xxi-chuong-xxii\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-128-tap-10-p6-chuong-xxi-pham-tam-muoi-bai-ke\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-129-tap-10-p6-chuong-xxi-pham-tam-muoi-bai-ke-tt\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-130-tap-10-p6-chuong-xxii-dai-pham-1\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-131-tap-10-p6-chuong-xxii-dai-pham-2\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-132-tap-10-p6-chuong-xxii-dai-pham-3\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-133-tap-10-p6-chuong-xxii-dai-pham-4\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-134-tap-10-p6-chuong-xxii-dai-pham-5\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-135-tap-10-p6-chuong-xxii-dai-pham-6\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-136-tap-10-p6-chuong-xxii-dai-pham-7\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-137-tap-10-p6-chuong-xxii-dai-pham-8\.md",
"/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau/kn-138-tap-10-p6-chuong-xxii-dai-pham-9\.md",
]

PATTERN = re.compile(r"\*\*(\d+\..+?)\*\*")   # regex tìm
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
        backup = path.with_suffix(path.suffix + ".bak")
        if not backup.exists():
            backup.write_text(text, encoding=ENCODING)
        path.write_text(new_text, encoding=ENCODING)
        print(f"✅ {path}: {count} thay đổi (backup: {backup.name})")

    return count


def main():
    total = 0
    for f in FILES:
        total += process_file(Path(f))
    print(f"\n🎉 Tổng cộng: {total} thay đổi trong {len(FILES)} file.")


if __name__ == "__main__":
    main()