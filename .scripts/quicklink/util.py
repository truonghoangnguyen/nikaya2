import re
import unicodedata
import json

def flat_json(merged):
    # Dump chuẩn JSON thông thường
    json_str = json.dumps(merged, ensure_ascii=False, indent=2)

    # Dùng Regex để gộp riêng mảng children về 1 dòng

    def flatten_children(match):
        # Lấy riêng các số nguyên, bỏ qua khoảng trắng và dấu phẩy cũ
        numbers = re.findall(r"\d+", match.group(1))
        return f'"children": [{", ".join(numbers)}]'


    # Thay thế mảng children nhiều dòng thành 1 dòng
    json_flat_children = re.sub(
        r'"children":\s*\[\s*([\d,\s]+)\s*\]', flatten_children, json_str
    )
    return json_flat_children


def slugify(text):
    """Slug gần với @mdit/plugin-anchor, có hỗ trợ bỏ dấu tiếng Việt."""
    text = text.strip()
    text = re.sub(r'`([^`]*)`', r'\1', text)  # bỏ backtick code

    # 1. Xử lý riêng chữ đ/Đ
    text = text.replace('đ', 'd').replace('Đ', 'D')

    # 2. Tách dấu và loại bỏ
    text = (
        unicodedata.normalize('NFKD', text)
        .encode('ascii', 'ignore')
        .decode('utf-8')
    )

    # 3. Chuẩn hóa slug
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)

    # 4. Loại bỏ dấu '-' ở đầu/cuối
    text = text.strip('-')

    # 5. @mdit/plugin-anchor: heading bắt đầu bằng số -> thêm "_"
    if text and text[0].isdigit():
        text = '_' + text

    return text