import os
import re
import json
from util import flat_json

# ==========================================
# CẤU HÌNH ĐẦU VÀO
# ==========================================
SOURCE_DIR = "../../docs/vinaya-vi/kd/cv"

FILES = [
"pli-tv-kd-5-khuddakavatthukkhandhaka.md",

]

# ==========================================
# REGEX
# ==========================================
# Tìm H1: # Tiêu đề
H1_RE = re.compile(r'^#\s+(.+)$', re.MULTILINE)

# Tìm TẤT CẢ anchor trong file: {#1}, {#2}, {#1.1}, ...
ANCHOR_RE = re.compile(r'\{#(\d+(?:\.\d+)*)\}')

# Tự động bắt số đầu tiên trong tên file làm key (vd: snc-01-... -> 1)
TOP_INDEX_RE = re.compile(r'^[a-z]+-0*(\d+)', re.IGNORECASE)
CHUONG_RE = re.compile(r'kd-*(\d+)', re.IGNORECASE)


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

        # 3. Lấy danh sách children từ TẤT CẢ anchor {#...}
        raw_children = ANCHOR_RE.findall(content)

        # Loại bỏ trùng lặp nhưng vẫn giữ nguyên thứ tự xuất hiện
        children = list(dict.fromkeys(raw_children))

        # Lưu kết quả
        result[key] = {
            "title": title,
            "slug": slug,
            "children": children
        }

    return result


if __name__ == "__main__":
    output_data = process_files(SOURCE_DIR, FILES)

    txt = flat_json(output_data)
    print(txt)

    # (Tuỳ chọn) Ghi ra file json nếu muốn:
    # with open("output.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(output_data, ensure_ascii=False, indent=2))