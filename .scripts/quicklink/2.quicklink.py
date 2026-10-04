import os
import re
import json
from util import flat_json
# ==========================================
# CẤU HÌNH ĐẦU VÀO
# ==========================================
SOURCE_DIR = "../../docs/kinhtieubo/thichminhchau"  # Thư mục chứa file markdown (đổi lại nếu cần)

# Bạn nhập danh sách file vào đây:
# - Cách 1: Chỉ cần tên file (sẽ tự động suy ra key từ số đầu tên file)
# - Cách 2: Dict có key nếu tên file không tự suy ra được (ví dụ: {"filename": "...", "key": "1"})

# "kn-037-tap-8-chuong-1-pham-mot-ke.md",
# "kn-038-tap-8-chuong-2-pham-hai-ke.md",
# "kn-039-tap-8-chuong-3-pham-ba-ke.md",
# "kn-040-tap-8-chuong-4-pham-bon-ke.md",
# "kn-041-tap-8-chuong-5-pham-nam-ke.md",
# "kn-042-tap-8-chuong-6-pham-sau-ke.md",
# "kn-043-tap-8-chuong-7-pham-bay-ke.md",
# "kn-044-tap-8-chuong-8-pham-tam-ke.md",
# "kn-045-tap-8-chuong-9-pham-chin-ke.md",
# "kn-046-tap-8-chuong-10-pham-muoi-ke.md",
# "kn-046-tap-8-chuong-11-pham-muoi-mot-ke.md",
# "kn-046-tap-8-chuong-12-pham-muoi-hai-ke.md",
# "kn-047-tap-8-chuong-13-pham-muoi-ba-ke.md",
# "kn-047-tap-8-chuong-14-pham-muoi-bon-ke.md",
# "kn-047-tap-8-chuong-15-pham-muoi-lam-ke.md",
# "kn-047-tap-8-chuong-16-pham-hai-muoi-ke.md",
# "kn-048-tap-8-chuong-17-pham-ba-muoi-ke.md",
# "kn-049-tap-8-chuong-18-pham-bon-muoi-ke.md",
# "kn-050-tap-8-chuong-19-pham-nam-muoi-ke.md",
# "kn-051-tap-8-chuong-20-pham-sau-muoi-ke.md",
# "kn-052-tap-8-chuong-21-pham-bay-muoi-ke.md",

FILES = [
"kn-072-tap-10-p1-pham-apannaka.md",
"kn-073-tap-10-p1-pham-gioi.md",
"kn-074-tap-10-p1-pham-kurunga.md",
"kn-075-tap-10-p1-pham-kulavaka.md",
"kn-076-tap-10-p1-pham-loi-ai.md",
"kn-077-tap-10-p1-pham-asimsa.md",
"kn-078-tap-10-p1-pham-nu-nhan.md",
"kn-079-tap-10-p1-pham-varana.md",
"kn-080-tap-10-p1-pham-apayimha.md",
"kn-081-tap-10-p1-pham-litta.md",
"kn-082-tap-10-p1-pham-parossata.md",
"kn-083-tap-10-p1-pham-hamsa.md",
"kn-084-tap-10-p1-pham-kusanali.md",
"kn-085-tap-10-p1-pham-asampadana.md",
"kn-086-tap-10-p1-pham-kakantaka.md",
"kn-087-tap-10-p2-chuong-2.md",
"kn-088-tap-10-p2-pham-dalha.md",
"kn-089-tap-10-p2-pham-santahava.md",
"kn-090-tap-10-p2-pham-thien-phap.md",
"kn-091-tap-10-p2-pham-asadisa.md",
"kn-092-tap-10-p2-pham-ruhaka.md",
"kn-093-tap-10-p2-pham-natamdaiha.md",
"kn-094-tap-10-p2-pham-biranatthambahaka-dam-co-thom.md",
"kn-095-tap-10-p2-pham-kasava.md",
"kn-096-tap-10-p2-pham-upahana.md",
"kn-097-tap-10-p2-pham-sigala-cho-rung.md",
"kn-098-tap-10-p3.md",
"kn-099-tap-10-p3-chuong-3-pham-sankappa.md",
"kn-100-tap-10-p3-chuong-3-pham-kosya.md",
"kn-101-tap-10-p3-chuong-3-pham-ba-bai-ke.md",
"kn-102-tap-10-p3-chuong-3-pham-ba-bai-ke-tt.md",
"kn-103-tap-10-p3-chuong-3-pham-ba-bai-ke-tt.md",
"kn-104-tap-10-p3-chuong-4-pham-bon-bai-ke.md",
"kn-105-tap-10-p3-chuong-4-pham-bon-bai-ke-tt.md",
"kn-106-tap-10-p3-chuong-4-pham-bon-bai-ke-tt.md",
"kn-107-tap-10-p3-chuong-4-pham-bon-bai-ke-tt.md",
"kn-108-tap-10-p3-chuong-4-pham-bon-bai-ke-tt.md",
"kn-109-tap-10-p4.md",
"kn-110-tap-10-p4-chuong-v-pham-nam-bai-ke.md",
"kn-111-tap-10-p4-chuong-vi-pham-sau-bai-ke.md",
"kn-112-tap-10-p4-chuong-vii-pham-bay-bai-ke.md",
"kn-113-tap-10-p4-chuong-viii-pham-tam-bai-ke.md",
"kn-114-tap-10-p4-chuong-ix-pham-chin-bai-ke.md",
"kn-115-tap-10-p4-chuong-x-pham-muoi-bai-ke.md",
"kn-116-tap-10-p4-chuong-xi-pham-muoi-mot-bai-ke.md",
"kn-117-tap-10-p4-chuong-xii-pham-muoi-hai-bai-ke.md",
"kn-118-tap-10-p5.md",
"kn-119-tap-10-p5-chuong-xiii-pham-muoi-ba-bai-ke.md",
"kn-120-tap-10-p5-chuong-xiv-tap-pham.md",
"kn-121-tap-10-p5-chuong-xv-pham-hai-muoi-bai-ke.md",
"kn-122-tap-10-p5-chuong-xvi-pham-ba-muoi-bai-ke.md",
"kn-123-tap-10-p5-chuong-xvii-pham-bon-muoi-bai-ke.md",
"kn-124-tap-10-p5-chuong-xviii-pham-nam-muoi-bai-ke.md",
"kn-125-tap-10-p5-chuong-xix-pham-sau-muoi-bai-ke.md",
"kn-126-tap-10-p5-chuong-xx-pham-bay-muoi-bai-ke.md",
"kn-127-tap-10-p6.md",
"kn-128-tap-10-p6-chuong-xxi-pham-tam-muoi-bai-ke.md",
"kn-129-tap-10-p6-chuong-xxi-pham-tam-muoi-bai-ke-tt.md",
"kn-130-tap-10-p6-chuong-xxii-dai-pham-1.md",
"kn-131-tap-10-p6-chuong-xxii-dai-pham-2.md",
"kn-132-tap-10-p6-chuong-xxii-dai-pham-3.md",
"kn-133-tap-10-p6-chuong-xxii-dai-pham-4.md",
"kn-134-tap-10-p6-chuong-xxii-dai-pham-5.md",
"kn-135-tap-10-p6-chuong-xxii-dai-pham-6.md",
"kn-136-tap-10-p6-chuong-xxii-dai-pham-7.md",
"kn-137-tap-10-p6-chuong-xxii-dai-pham-8.md",
"kn-138-tap-10-p6-chuong-xxii-dai-pham-9.md",

]

# ==========================================
# REGEX
# ==========================================
# Tìm H1: # Tiêu đề
H1_RE = re.compile(r'^#\s+(.+)$', re.MULTILINE)

# Tìm header từ ## trở đi và kết thúc bằng {#số}
# Ví dụ: ### SN 1.1 Vượt Qua Bộc Lưu {#1} -> bắt được "1"
# HEADING_ANCHOR_RE = re.compile(r'^#{2,}\s+.*?\{#(\d+)\}\s*$', re.MULTILINE)
HEADING_ANCHOR_RE = re.compile(
    r'^#{2,}\s+.*?\{#(\d+(?:\.\d+)*)\}\s*$',
    re.MULTILINE
)

# cho kiểu header **xxx**
HEADING_ANCHOR_RE = re.compile(
    r'^(?:#{2,}\s+.*?|\*\*.*?\*\*)\s*\{#(\d+(?:\.\d+)*)\}\s*$',
    re.MULTILINE
)

# Tự động bắt số đầu tiên trong tên file làm key (vd: snc-01-... -> 1)
TOP_INDEX_RE = re.compile(r'^[a-z]+-0*(\d+)', re.IGNORECASE)
CHUONG_RE = re.compile(r'kn-*(\d+)', re.IGNORECASE)

def extract_key_from_filename(filename):
    m = CHUONG_RE.search(filename.lower())
    return str(int(m.group(1))-71) if m else None


def process_files(source_dir, file_list):
    result = {}

    for item in file_list:
        # Xử lý input dù là string hay dict
        if isinstance(item, dict):
            filename = item["filename"]
            key_override = str(item.get("key")) if item.get("key") is not None else None
        else:
            filename = item
            key_override = None

        slug = filename[:-3] if filename.endswith(".md") else filename
        filepath = os.path.join(source_dir, filename)

        if not os.path.isfile(filepath):
            print(f"⚠️  Không tìm thấy file: {filepath}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Xác định Key
        if key_override:
            key = key_override
        else:
            key = extract_key_from_filename(filename)
            if not key:
                print(f"⚠️  Không trích xuất được key từ file '{filename}', hãy truyền 'key' thủ công.")
                continue

        # 2. Lấy Title từ H1
        h1_match = H1_RE.search(content)
        if h1_match:
            title = h1_match.group(1).strip()
        else:
            title = f"Chưa có tiêu đề ({slug})"
            print(f"⚠️  Không tìm thấy H1 trong file: {filename}")

        # 3. Lấy danh sách children từ anchor {#number}
        # findall sẽ lấy group (\d+) trong regex HEADING_ANCHOR_RE
        raw_children = HEADING_ANCHOR_RE.findall(content)

        # Loại bỏ trùng lặp nếu có mà vẫn giữ nguyên thứ tự xuất hiện
        children = list(dict.fromkeys(x for x in raw_children))

        # Lưu kết quả
        result[key] = {
            "title": title,
            "slug": slug,
            "children": children
        }

    return result


if __name__ == "__main__":
    output_data = process_files(SOURCE_DIR, FILES)

    # In kết quả ra màn hình định dạng JSON
    # json_output = json.dumps(output_data, ensure_ascii=False, indent=2)
    txt=flat_json(output_data)
    print(txt)

    # (Tuỳ chọn) Ghi ra file json nếu muốn:
    # with open("output.json", "w", encoding="utf-8") as f:
    #     f.write(json_output)