import re
import unicodedata

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