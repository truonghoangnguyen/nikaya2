"""
build_an_index.py
Sinh file JSON index cho Tăng Chi Bộ (Anguttara Nikāya) để tra cứu link
dạng "AN X.Y" -> slug file + anchor.

Khác với Tương Ưng Bộ (SN), mỗi "mục" (nipāta) của Tăng Chi Bộ được chia
thành NHIỀU file (mỗi file = một "phẩm"/vagga chứa ~10 kinh). Vì vậy không
thể suy trực tiếp từ số mục ra 1 file duy nhất như SN — cần quét từng file
để biết nó chứa các số kinh nào, rồi build bảng tra cứu.

Một số heading gộp nhiều kinh vào 1 anchor dạng range, ví dụ:
    ### AN 1.1–10 *Cittapariyādānavagga* (Phẩm Về Sự Xâm Chiếm Tâm) {#1-10}
Trường hợp này anchor {#1-10} được bung thành các số 1,2,...,10 — tất cả
đều trỏ về cùng 1 anchor #1-10 trong file (vì DOM chỉ có 1 heading đó).

Cách chạy: python build_an_index.py
(chạy tại thư mục gốc repo, nơi có docs/kinhtangchi/sujato-vi/)

Hướng dẫn: thường sẽ tạo 1 bản của sujato, 1 bản của tmc sau đó lấy childrent của sujato và title+slug của tmc
vào thành bản compare



 if MAP:
            # map: số kinh -> anchor thật trên trang (để xử lý case gộp range)
            number_to_anchor = {}
            for raw in anchor_ranges:
                if "-" in raw or "–" in raw or "—" in raw:
                    parts = re.split(r"[-–—]", raw)
                    lo, hi = int(parts[0]), int(parts[1])
                    for n in range(lo, hi + 1):
                        number_to_anchor[n] = raw
                else:
                    number_to_anchor[int(raw)] = raw

        nipatas[nipata].append({
            "slug": path.stem,
            "title": vagga_title,
            "start": min(anchors),
            "end": max(anchors),
            "children": anchors,

        })

        if MAP:
            nipatas[nipata].append({"anchor_map": number_to_anchor}),  # số kinh -> anchor thật (vd 5 -> "1-10")
"""


import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from util import flat_json

# an-05-021-the-chapter-with-kimbila.md -> nipata="05", order="021"
FILENAME_RE = re.compile(r"^an-(\d+)-(\d+)-.+\.md$")

# ### AN 5.231 ... {#231}          -> anchor đơn
# ### AN 1.1–10 ... {#1-10}        -> anchor dạng range (gộp nhiều kinh)
# Chấp nhận cả '-', '–' (en dash), '—' (em dash) làm dấu nối trong anchor.
HEADING_RE = re.compile(r"^###\s+AN\s+\d+\.\d+.*\{#(\d+)(?:[-–—](\d+))?\}")

# # Phẩm Về Kẻ Ngu   (tiêu đề phẩm dùng H1, chỉ 1 dấu #)
VAGGA_TITLE_RE = re.compile(r"^#\s+(.+?)\s*$")

NIPATA_SO = {
    1: "Một", 2: "Hai", 3: "Ba", 4: "Bốn", 5: "Năm", 6: "Sáu",
    7: "Bảy", 8: "Tám", 9: "Chín", 10: "Mười", 11: "Mười Một",
}


def env_bool(name: str, default: bool) -> bool:
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "y", "on")

_kinh="thichminhchau"
HEAD_ONLY = True
output_file = 'an-index-tmc.json'

def parse_args():
    # docs/kinhtangchi/thichminhchau/an-01-001-pham-sac.md
    p = argparse.ArgumentParser(description="Sinh index tra cứu cho Tăng Chi Bộ (AN)")
    p.add_argument("--src", default=f"../../docs/kinhtangchi/{_kinh}", help="Thư mục chứa file .md của AN")
    p.add_argument("--out", default=f"{output_file}", help="File JSON output")
    p.add_argument(
        "--head-only",
        dest="head_only",
        action=argparse.BooleanOptionalAction,
        default=env_bool("HEAD_ONLY", HEAD_ONLY),
        help="Chỉ lấy title + slug (children luôn []), không quét anchor kinh. "
             "Có thể bật qua biến môi trường HEAD_ONLY=true.",
    )
    p.add_argument(
        "--map",
        dest="include_map",
        action=argparse.BooleanOptionalAction,
        default=env_bool("MAP", False),
        help="Có xuất trường anchor_map hay không (mặc định: có). "
             "Không áp dụng khi --head-only. Có thể set qua biến môi trường MAP=true|false.",
    )
    return p.parse_args()


def scan_file(path: Path, head_only: bool):
    anchors = []          # danh sách số kinh đã bung range, VD [1,2,...,10]
    anchor_ranges = []    # anchor thật sự có trên trang, VD ["1-10"] hoặc ["231"]
    vagga_title = None

    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")

            if vagga_title is None:
                m = VAGGA_TITLE_RE.match(line)
                if m:
                    vagga_title = m.group(1)
                    if head_only:
                        break  # HEAD_ONLY: có title là đủ, khỏi đọc tiếp file
                    continue

            if head_only:
                continue  # không quét heading kinh trong chế độ HEAD_ONLY

            m = HEADING_RE.match(line)
            if m:
                start_a = int(m.group(1))
                end_a = int(m.group(2)) if m.group(2) else start_a
                anchors.extend(range(start_a, end_a + 1))
                anchor_ranges.append(m.group(0).rsplit("{#", 1)[1].rstrip("}"))

    return anchors, anchor_ranges, vagga_title


def build_anchor_map(anchor_ranges):
    number_to_anchor = {}
    for raw in anchor_ranges:
        if re.search(r"[-–—]", raw):
            lo_s, hi_s = re.split(r"[-–—]", raw)
            for n in range(int(lo_s), int(hi_s) + 1):
                number_to_anchor[n] = raw
        else:
            number_to_anchor[int(raw)] = raw
    return number_to_anchor


def build_index(args):
    src_dir = Path(args.src)
    out_file = Path(args.out)
    nipatas = defaultdict(list)

    print(args)
    for path in sorted(src_dir.glob("an-*.md")):

        fm = FILENAME_RE.match(path.name)

        if not fm or fm.group(2)=='000':

            print(f"⚠️  Bỏ qua (tên file không khớp mẫu hay 000 file): {path.name}")
            continue

        nipata = str(int(fm.group(1)))  # "05" -> "5"
        anchors, anchor_ranges, vagga_title = scan_file(path, args.head_only)

        if args.head_only:
            nipatas[nipata].append({
                "slug": path.stem,
                "title": vagga_title,
                "children": [],
            })
            continue

        if not anchors:
            print(f"⚠️  Không tìm thấy anchor kinh nào trong: {path.name}")
            continue

        entry = {
            "slug": path.stem,
            "title": vagga_title,
            "start": min(anchors),
            "end": max(anchors),
            "children": anchors,
        }
        if args.include_map:
            entry["anchor_map"] = build_anchor_map(anchor_ranges)

        nipatas[nipata].append(entry)

    result = {}
    for nipata, files in sorted(nipatas.items(), key=lambda kv: int(kv[0])):
        if not args.head_only:
            files.sort(key=lambda f: f["start"])
        # ở chế độ head_only, thứ tự file giữ nguyên theo glob (đã sort theo tên file)
        result[nipata] = {
            "title": f"Chương {NIPATA_SO.get(int(nipata), nipata)} Pháp",
            "files": files,
        }

    txt = flat_json (result)
    out_file.write_text(txt, encoding="utf-8")

    mode_desc = "HEAD_ONLY" if args.head_only else ("kèm anchor_map" if args.include_map else "không anchor_map")
    print(f"✅ Đã ghi {out_file} ({mode_desc}) — {len(result)} mục (nipāta)")

    if not args.head_only:
        for nipata, data in result.items():
            prev_end = 0
            for f in data["files"]:
                if prev_end != 0 and f["start"] != prev_end + 1:
                    print(
                        f"⚠️  Mục {nipata}: khoảng trống/chồng lấn số kinh giữa "
                        f"{prev_end} và {f['start']} (file {f['slug']})"
                    )
                prev_end = f["end"]


if __name__ == "__main__":
    build_index(parse_args())