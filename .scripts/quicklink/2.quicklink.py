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
"kn-054-tap-9-pham-1-tap-mot-ke.md",
"kn-055-tap-9-pham-2-tap-hai-ke.md",
"kn-056-tap-9-pham-3-tap-ba-ke.md",
"kn-057-tap-9-pham-4-tap-bon-ke.md",
"kn-058-tap-9-pham-5-tap-nam-ke.md",
"kn-059-tap-9-pham-6-tap-sau-ke.md",
"kn-060-tap-9-pham-7-tap-bay-ke.md",
"kn-061-tap-9-pham-8-tap-tam-ke.md",
"kn-062-tap-9-pham-9-tap-chin-ke.md",
"kn-063-tap-9-pham-10-tap-muoi-ke.md",
"kn-064-tap-9-pham-11-tap-muoi-hai-ke.md",
"kn-065-tap-9-pham-12-tap-muoi-sau-ke.md",
"kn-066-tap-9-pham-13-tap-hai-muoi-ke.md",
"kn-067-tap-9-pham-14-tap-ba-muoi-ke.md",
"kn-068-tap-9-pham-15-tap-bon-muoi-ke.md",
"kn-069-tap-9-pham-16-dai-pham.md"
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
CHUONG_RE = re.compile(r'pham-*(\d+)', re.IGNORECASE)

def extract_key_from_filename(filename):
    m = CHUONG_RE.search(filename.lower())
    return str(int(m.group(1))) if m else None


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