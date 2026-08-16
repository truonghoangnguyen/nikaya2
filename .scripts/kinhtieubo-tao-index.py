
"""
URL_PREFIX = "../docs/kinhtieubo/pali/"

def build_index_for_folder(folder_path):
    folder_path = URL_PREFIX + folder_path

build_index.py
---------------
Đọc các file .md trong từng thư mục kinh (kn/bv, kn/cnd, ...), lấy H1 (# ...)
của mỗi file, chuyển thành tiêu đề dạng "N.M. Tên kinh" và ghi ra index.md
ngay trong thư mục đó.

Ví dụ:
    file kn/bv/bv-001-1-ratanacankamanakanda.md có dòng đầu:
        # BV 1. 1. Ratanacaṅkamanakaṇḍa
    -> sinh dòng trong kn/bv/index.md:
        - [1.1. Ratanacaṅkamanakaṇḍa](/kinhtieubo/pali/bv/bv-001-1-ratanacankamanakanda.md)

Chạy:
    python build_index.py
"""
"""
build_index.py
---------------
Đọc các file .md trong từng thư mục kinh (kn/bv, kn/cnd, ...), lấy H1 (# ...)
của mỗi file, chuyển thành tiêu đề dạng "N.M. Tên kinh" và ghi ra index.md
ngay trong thư mục đó.

Hỗ trợ 2 dạng thư mục:

1) Thư mục phẳng (file .md nằm trực tiếp trong thư mục), vd kn/bv:
       file kn/bv/bv-001-1-ratanacankamanakanda.md có dòng đầu:
           # BV 1. 1. Ratanacaṅkamanakaṇḍa
       -> sinh dòng trong kn/bv/index.md:
           - [1.1. Ratanacaṅkamanakaṇḍa](/kinhtieubo/pali/bv/bv-001-1-ratanacankamanakanda.md)

2) Thư mục có thư mục con (vagga1, vagga2, ...), vd kn/ud:
       kn/ud/vagga1/ud-1-1-pathamabodhisutta.md
       kn/ud/vagga2/...
       -> sinh trong kn/ud/index.md:
           ### vagga1
           - [1.1. Paṭhamabodhisutta](/kinhtieubo/pali/ud/vagga1/ud-1-1-pathamabodhisutta.md)
           ...
           ### vagga2
           ...

Chạy:
    python build_index.py
"""

import os
import re


# ====================== CẤU HÌNH ======================

# prefix dùng khi build link trong .md (không có / ở cuối)
URL_PREFIX = "../docs/kinhtieubo/pali/"

# tên thư mục con bị bỏ qua khi quét (không phải là "vagga")
IGNORE_SUBDIRS = {"meta", ".git", "__pycache__"}

# danh sách các thư mục kinh cần xử lý (đường dẫn thực trên đĩa, so với nơi
# chạy script). Sửa lại cho khớp với cấu trúc thư mục thật của bạn.
kinh_lst = [
    'bv',
    'cnd',
    'cp',
    'dhp',
    'iti',
    'ja',
    'kp',
    'mil',
    'mnd',
    'ne',
    'pe',
    'ps',
    'pv',
    'snp',
    'tha-ap',
    'thag',
    'thi-ap',
    'thig',
    'ud',
    'vv',
]

# =======================================================


def natural_key(name):
    """Sort tự nhiên theo cụm số trong tên (file hoặc thư mục).
    vd: bv-001-1-...  <  bv-001-2-...  <  bv-002-1-...
        vagga1 < vagga2 < ... < vagga10
    """
    return [int(tok) if tok.isdigit() else tok
            for tok in re.split(r'(\d+)', name)]


def list_md_files(folder_path):
    """Trả về danh sách tên file .md trong folder_path (không đệ quy), đã sort tự nhiên."""
    files = [
        f for f in os.listdir(folder_path)
        if f.endswith(".md") and f != "index.md"
        and os.path.isfile(os.path.join(folder_path, f))
    ]
    files.sort(key=natural_key)
    return files


def list_subdirs(folder_path):
    """Trả về danh sách thư mục con (vagga1, vagga2, ...) trong folder_path, đã sort tự nhiên."""
    dirs = [
        d for d in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, d))
        and d not in IGNORE_SUBDIRS
        and not d.startswith(".")
    ]
    dirs.sort(key=natural_key)
    return dirs


def read_h1(filepath):
    """Đọc dòng H1 (bắt đầu bằng '# ') đầu tiên trong file .md."""
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return None


def clean_title(raw_h1):
    """
    'BV 1. 1. Ratanacaṅkamanakaṇḍa'  ->  '1.1. Ratanacaṅkamanakaṇḍa'

    - Bỏ mã sách in hoa ở đầu (BV, KP, MND, THA-AP, UD, ...)
    - Gộp các số phân cấp đầu dòng "N. M. " -> "N.M. "
      (hỗ trợ bất kỳ số cấp nào: 1 số, 2 số, 3 số...)
    """
    if raw_h1 is None:
        return None

    text = raw_h1.strip()

    # bỏ mã sách in hoa ở đầu, vd "BV ", "THA-AP ", "UD "
    text = re.sub(r'^[A-Z][A-Z\-]*\s+', '', text)

    # gộp số phân cấp: "1. 1. " -> "1.1. "
    m = re.match(r'^((?:\d+\.\s*)+)(.*)$', text)
    if m:
        numbers = re.findall(r'\d+', m.group(1))
        rest = m.group(2).strip()
        text = f"{'.'.join(numbers)}. {rest}"

    return text


def build_lines_for_files(folder_name, files_dir, filenames, path_segments):
    """Sinh list các dòng '- [title](link)' cho 1 danh sách file trong 1 thư mục.
    path_segments: các đoạn thư mục con giữa folder_name và tên file, vd ['vagga1'].
    """
    lines = []
    for filename in filenames:
        filepath = os.path.join(files_dir, filename)
        raw_h1 = read_h1(filepath)

        if raw_h1 is None:
            print(f"  [CẢNH BÁO] Không tìm thấy H1 trong: {filepath}")
            continue

        title = clean_title(raw_h1)
        link_parts = ["/kinhtieubo/pali/", folder_name, *path_segments, filename]
        link = "/".join(part.strip("/") for part in link_parts)
        link = "/" + link if not link.startswith("/") else link
        lines.append(f"- [{title}]({link})")
    return lines


def build_index_for_folder(folder_path):
    """Tạo index.md cho 1 thư mục kinh (hỗ trợ cả thư mục phẳng lẫn có vagga con).
    Trả về đường dẫn file đã ghi (hoặc None)."""
    folder_path = URL_PREFIX + folder_path

    if not os.path.isdir(folder_path):
        print(f"[BỎ QUA] Không tìm thấy thư mục: {folder_path}")
        return None

    folder_name = os.path.basename(folder_path.rstrip("/\\"))
    subdirs = list_subdirs(folder_path)

    lines = []

    # file .md nằm trực tiếp trong thư mục (nếu có), luôn xử lý trước, không có heading
    top_files = list_md_files(folder_path)
    lines.extend(build_lines_for_files(folder_name, folder_path, top_files, []))

    # thư mục con kiểu vagga1, vagga2, ...
    for subdir in subdirs:
        subdir_path = os.path.join(folder_path, subdir)
        sub_files = list_md_files(subdir_path)
        if not sub_files:
            continue
        lines.append(f"### {subdir}")
        lines.extend(build_lines_for_files(folder_name, subdir_path, sub_files, [subdir]))

    out_path = os.path.join(folder_path, "index.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    total = sum(1 for l in lines if l.startswith("- ["))
    print(f"[OK] {out_path} — {total} mục" + (f" ({len(subdirs)} vagga)" if subdirs else ""))
    return out_path


def main():
    for folder in kinh_lst:
        build_index_for_folder(folder)


if __name__ == "__main__":
    main()