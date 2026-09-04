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
FILES = [
"kn-004-tap-3-chuong-1-pham-bo-de.md",
"kn-005-tap-3-chuong-2-pham-muccalinda.md",
"kn-006-tap-3-chuong-3-pham-nanda.md",
"kn-007-tap-3-chuong-4-pham-meghiya.md",
"kn-008-tap-3-chuong-5-pham-truong-lao-sona.md",
"kn-009-tap-3-chuong-6-pham-sanh-ra-da-mu.md",
"kn-010-tap-3-chuong-7-pham-nho.md",
"kn-011-tap-3-chuong-8-pham-pataligamiya.md"
]

# ==========================================
# REGEX
# ==========================================
# Tìm H1: # Tiêu đề
H1_RE = re.compile(r'^#\s+(.+)$', re.MULTILINE)

# Tìm header từ ## trở đi và kết thúc bằng {#số}
# Ví dụ: ### SN 1.1 Vượt Qua Bộc Lưu {#1} -> bắt được "1"
HEADING_ANCHOR_RE = re.compile(r'^#{2,}\s+.*?\{#(\d+)\}\s*$', re.MULTILINE)

# Tự động bắt số đầu tiên trong tên file làm key (vd: snc-01-... -> 1)
TOP_INDEX_RE = re.compile(r'^[a-z]+-0*(\d+)', re.IGNORECASE)
CHUONG_RE = re.compile(r'chuong-0*(\d+)', re.IGNORECASE)

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
        children = list(dict.fromkeys(int(x) for x in raw_children))

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