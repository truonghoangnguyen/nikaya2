import os
import re
import requests
from urllib.parse import urlparse

# ===== Cấu hình =====
MD_FILE = "buddhism - outline of. HW.md"           # đường dẫn file markdown
OUTPUT_DIR = "images"           # folder lưu ảnh
# ====================

# Tạo folder nếu chưa có
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Đọc nội dung markdown
with open(MD_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Regex bắt ảnh:
# 1. HTML: <img ... src="URL" ...>
# 2. Markdown: ![alt](URL)
html_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
md_pattern = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')

# Gộp tất cả match theo đúng thứ tự xuất hiện trong file
matches = []
for m in html_pattern.finditer(content):
    matches.append((m.start(), m.group(1)))
for m in md_pattern.finditer(content):
    matches.append((m.start(), m.group(1)))

# Sắp xếp theo vị trí xuất hiện
matches.sort(key=lambda x: x[0])

print(f"Tìm thấy {len(matches)} ảnh trong file markdown.")

# Tải từng ảnh
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
})

for idx, (pos, url) in enumerate(matches):
    url = url.strip()

    # Xác định đuôi file từ URL (mặc định .jpeg nếu không rõ)
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"):
        ext = ".jpeg"

    filename = f"img-{idx}{ext}"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        resp = session.get(url, timeout=30, stream=True)
        resp.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        size_kb = os.path.getsize(filepath) / 1024
        print(f"[{idx+1}/{len(matches)}] Đã lưu: {filename} ({size_kb:.1f} KB)")

    except Exception as e:
        print(f"[{idx+1}/{len(matches)}] LỖI khi tải {url[:80]}... -> {e}")

print("\nHoàn tất!")