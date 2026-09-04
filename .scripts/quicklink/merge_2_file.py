import re
from pathlib import Path
import json

def load_js_export(path):
    text = Path(path).read_text(encoding="utf-8")

    # Bỏ "export default" để còn lại object JavaScript/Python-like
    text = re.sub(r"^\s*export\s+default\s*", "", text)

    # Dữ liệu này dùng double quote + object syntax hợp lệ cho Python
    return eval(text)


def load_json(path):
    text = Path(path).read_text(encoding="utf-8")
    return json.loads(text)

def merge_files(file1, file2, output_file):
    data1 = load_json(file1)
    data2 = load_json(file2)

    merged = {}

    # Map 1-1 theo id: 1, 2, 3, ...
    for book_id, book1 in data1.items():
        book2 = data2.get(book_id)

        if book2 is None:
            print(f"Warning: file 2 không có id {book_id}")
            continue

        merged[book_id] = {
            "title": book1["title"],
            "slug": book1["slug"],
            "children": book2.get("children", {})
        }

    # Xuất lại thành JS
    output = "export default " + json.dumps(
        merged,
        ensure_ascii=False,
        indent=2
    )

    # Đổi quote Python thành quote JS đẹp hơn
    output = output.replace("'", '"')

    Path(output_file).write_text(output + "\n", encoding="utf-8")

f1='an-index-tmc.json'
f2='an-index.json'
f3='../../docs/.vitepress/data/link-an-sujato-tmc.js'
if __name__ == "__main__":
    merge_files(
        f1,
        f2,
        f3
    )