import os, re, json

# Thư mục chứa các file .md",", "range": (1, 10)},
SOURCE_DIR = "../../docs/kinhtangchi/thichminhchau"

# Danh sách tên file .md",", cần xử lý (chỉ tên file, không cần đường dẫn đầy đủ)
FILES = [
{"filename": "an-01-001-pham-sac.md", "range": (1, 10)},
{"filename": "an-01-002-pham-doan-trien-cai.md", "range": (11, 20)},
{"filename": "an-01-003-pham-kho-su-dung.md", "range": (21, 30)},
{"filename": "an-01-004-pham-khong-dieu-phuc.md", "range": (31, 40)},
{"filename": "an-01-005-pham-dat-huong-va-trong-sang.md", "range": (41, 50)},
{"filename": "an-01-006-pham-bung-ngon-tay.md", "range": (51, 60)},
{"filename": "an-01-007-pham-tinh-tan.md", "range": (61, 70)},
{"filename": "an-01-008-pham-lam-ban-voi-thien.md", "range": (71, 81)},
{"filename": "an-01-009-pham-phong-dat.md", "range": (82, 97)},
{"filename": "an-01-010-pham-phi-phap-1.md", "range": (98, 139)},
{"filename": "an-01-011-pham-phi-phap-3.md", "range": (140, 149)},
{"filename": "an-01-012-pham-vo-pham.md", "range": (150, 169)},
{"filename": "an-01-013-pham-mot-nguoi.md", "range": (170, 187)},
{"filename": "an-01-014-pham-nguoi-toi-thang.md", "range": (188, 197)},
{"filename": "an-01-015-pham-khong-the-co-duoc.md", "range": (268, 277)},
{"filename": "an-01-016-pham-mot-phap.md", "range": (296, 305)},
{"filename": "an-01-017-pham-chung-tu.md", "range": (306, 315)},
{"filename": "an-01-018-pham-makkhali.md", "range": (316, 332)},
{"filename": "an-01-019-pham-khong-phong-dat.md", "range": (333, 377)},
{"filename": "an-01-020-pham-thien-dinh-that-su-la-vay.md", "range": (378, 393)},
{"filename": "an-01-021-pham-thien-dinh-bung-ngon-tay.md", "range": (394, 574)},
{"filename": "an-01-022-pham-thien-dinh-2-than-hanh-niem.md", "range": (575, 615)},
{"filename": "an-01-023-pham-thien-dinh-2-bat-tu.md", "range": (616, 627)},
{"filename": "an-02-001-pham-hinh-phat.md", "range": (1, 10)},
{"filename": "an-02-002-pham-tranh-luan.md", "range": (11, 20)},
{"filename": "an-02-003-pham-nguoi-ngu.md", "range": (21, 31)},
{"filename": "an-02-004-pham-tam-thang-bang.md", "range": (32, 41)},
{"filename": "an-02-005-pham-hoi-chung.md", "range": (42, 51)},
{"filename": "an-02-006-pham-nguoi.md", "range": (52, 63)},
{"filename": "an-02-007-pham-lac.md", "range": (64, 76)},
{"filename": "an-02-008-pham-tuong.md", "range": (77, 86)},
{"filename": "an-02-009-pham-cac-phap.md", "range": (87, 97)},
{"filename": "an-02-010-pham-ke-ngu.md", "range": (98, 117)},
{"filename": "an-02-011-pham-cac-hy-vong.md", "range": (118, 129)},
{"filename": "an-02-012-pham-hy-cau.md", "range": (130, 140)},
{"filename": "an-02-013-pham-bo-thi.md", "range": (141, 150)},
{"filename": "an-02-014-pham-don-chao.md", "range": (151, 162)},
{"filename": "an-02-015-pham-nhap-dinh.md", "range": (163, 179)},
{"filename": "an-02-016-pham-phan-no.md", "range": (180, 279)},
{"filename": "an-02-017-pham-thu-muoi-bay.md", "range": (280, 309)},
{"filename": "an-03-001-pham-nguoi-ngu.md", "range": (1, 10)},
{"filename": "an-03-002-pham-nguoi-dong-xe.md", "range": (11, 20)},
{"filename": "an-03-003-pham-nguoi.md", "range": (21, 30)},
{"filename": "an-03-004-pham-su-gia-cua-troi.md", "range": (31, 40)},
{"filename": "an-03-005-pham-nho.md", "range": (41, 50)},
{"filename": "an-03-006-pham-cac-ba-la-mon.md", "range": (51, 60)},
{"filename": "an-03-007-pham-lon.md", "range": (61, 70)},
{"filename": "an-03-008-pham-ananda.md", "range": (71, 80)},
{"filename": "an-03-009-pham-sa-mon.md", "range": (81, 91)},
{"filename": "an-03-010-pham-hat-muoi.md", "range": (92, 102)},
{"filename": "an-03-011-pham-chanh-giac.md", "range": (103, 112)},
{"filename": "an-03-012-pham-doa-xu.md", "range": (113, 122)},
{"filename": "an-03-013-pham-kusinara.md", "range": (123, 132)},
{"filename": "an-03-014-pham-ke-chien-si.md", "range": (133, 145)},
{"filename": "an-03-015-pham-cat-tuong.md", "range": (146, 155)},
{"filename": "an-03-016-pham-loa-the.md", "range": (156, 352)},
{"filename": "an-04-001-pham-bhandagana.md", "range": (1, 10)},
{"filename": "an-04-002-pham-hanh.md", "range": (11, 20)},
{"filename": "an-04-003-pham-uruvela.md", "range": (21, 30)},
{"filename": "an-04-004-pham-banh-xe.md", "range": (31, 40)},
{"filename": "an-04-005-pham-rohitassa.md", "range": (41, 50)},
{"filename": "an-04-006-pham-nguon-sanh-phuoc.md", "range": (51, 60)},
{"filename": "an-04-007-pham-nghiep-cong-duc.md", "range": (61, 70)},
{"filename": "an-04-008-pham-khong-hy-luan.md", "range": (71, 80)},
{"filename": "an-04-009-pham-khong-co-rung-dong.md", "range": (81, 90)},
{"filename": "an-04-010-pham-asura-a-tu-la.md", "range": (91, 100)},
{"filename": "an-04-011-pham-may-mua.md", "range": (101, 110)},
{"filename": "an-04-012-pham-kesi.md", "range": (111, 120)},
{"filename": "an-04-013-pham-so-hai.md", "range": (121, 130)},
{"filename": "an-04-014-pham-loai-nguoi.md", "range": (131, 140)},
{"filename": "an-04-015-pham-anh-sang.md", "range": (141, 150)},
{"filename": "an-04-016-pham-cac-can.md", "range": (151, 160)},
{"filename": "an-04-017-pham-dao-hanh.md", "range": (161, 170)},
{"filename": "an-04-018-pham-tu-tam-so.md", "range": (171, 180)},
{"filename": "an-04-019-pham-chien-si.md", "range": (181, 190)},
{"filename": "an-04-020-dai-pham.md", "range": (191, 200)},
{"filename": "an-04-021-pham-bac-chan-nhan.md", "range": (201, 210)},
{"filename": "an-04-022-pham-o-ue.md", "range": (211, 220)},
{"filename": "an-04-023-pham-dieu-hanh.md", "range": (211, 231)},
{"filename": "an-04-024-pham-nghiep.md", "range": (232, 242)},
{"filename": "an-04-025-pham-so-hai-pham-toi.md", "range": (243, 253)},
{"filename": "an-04-026-pham-thang-tri.md", "range": (254, 263)},
{"filename": "an-04-027-pham-nghiep-dao.md", "range": (264, 273)},
{"filename": "an-04-028-pham-tham.md", "range": (274, 783)},
{"filename": "an-05-001-pham-suc-manh-huu-hoc.md", "range": (1, 10)},
{"filename": "an-05-002-pham-suc-manh.md", "range": (11, 20)},
{"filename": "an-05-003-pham-nam-phan.md", "range": (21, 30)},
{"filename": "an-05-004-pham-sumana.md", "range": (31, 40)},
{"filename": "an-05-005-pham-vua-munda.md", "range": (41, 50)},
{"filename": "an-05-006-pham-trien-cai.md", "range": (51, 60)},
{"filename": "an-05-007-pham-tuong.md", "range": (61, 70)},
{"filename": "an-05-008-pham-chien-si.md", "range": (71, 80)},
{"filename": "an-05-009-pham-truong-lao.md", "range": (81, 90)},
{"filename": "an-05-010-pham-kakudha.md", "range": (91, 100)},
{"filename": "an-05-011-pham-an-on-tru.md", "range": (101, 110)},
{"filename": "an-05-012-pham-andhakavinda.md", "range": (111, 120)},
{"filename": "an-05-013-pham-benh.md", "range": (121, 130)},
{"filename": "an-05-014-pham-vua.md", "range": (131, 140)},
{"filename": "an-05-015-pham-tikandaki.md", "range": (141, 150)},
{"filename": "an-05-016-pham-dieu-phap.md", "range": (151, 160)},
{"filename": "an-05-017-pham-hiem-han.md", "range": (161, 170)},
{"filename": "an-05-018-pham-nam-cu-si.md", "range": (171, 180)},
{"filename": "an-05-019-pham-rung.md", "range": (181, 190)},
{"filename": "an-05-020-pham-ba-la-mon.md", "range": (191, 200)},
{"filename": "an-05-021-pham-kimbila.md", "range": (201, 210)},
{"filename": "an-05-022-pham-mang-nhiec.md", "range": (211, 220)},
{"filename": "an-05-023-pham-du-hanh-dai.md", "range": (221, 230)},
{"filename": "an-05-024-pham-tru-tai-cho.md", "range": (231, 240)},
{"filename": "an-05-025-pham-ac-hanh.md", "range": (241, 250)},
{"filename": "an-05-026-pham-cu-tuc-gioi.md", "range": (251, 1152)},
{"filename": "an-06-001-pham-dang-duoc-cung-kinh.md", "range": (1, 10)},
{"filename": "an-06-002-pham-can-phai-nho.md", "range": (11, 20)},
{"filename": "an-06-003-pham-tren-tat-ca.md", "range": (21, 30)},
{"filename": "an-06-004-pham-chu-thien.md", "range": (31, 42)},
{"filename": "an-06-005-pham-dhammika.md", "range": (43, 54)},
{"filename": "an-06-006-dai-pham.md", "range": (55, 64)},
{"filename": "an-06-007-pham-chu-thien.md", "range": (65, 74)},
{"filename": "an-06-008-pham-a-la-han.md", "range": (75, 84)},
{"filename": "an-06-009-pham-mat-lanh.md", "range": (85, 95)},
{"filename": "an-06-010-pham-loi-ich.md", "range": (96, 106)},
{"filename": "an-06-011-pham-ba-phap.md", "range": (107, 116)},
{"filename": "an-06-012-pham-cac-kinh-khong-nhiep-trong-pham.md", "range": (117, 649)},
{"filename": "an-07-001-pham-tai-san.md", "range": (1, 10)},
{"filename": "an-07-002-pham-tuy-mien.md", "range": (11, 20)},
{"filename": "an-07-003-pham-vajji-bat-ky.md", "range": (21, 31)},
{"filename": "an-07-004-pham-chu-thien.md", "range": (32, 43)},
{"filename": "an-07-005-pham-dai-te-dan.md", "range": (44, 53)},
{"filename": "an-07-006-pham-khong-tuyen-bo.md", "range": (54, 64)},
{"filename": "an-07-007-dai-pham.md", "range": (65, 74)},
{"filename": "an-07-008-pham-ve-luat.md", "range": (75, 84)},
{"filename": "an-07-009-pham-cac-kinh-khong-nhiep.md", "range": (85, 1124)},
{"filename": "an-08-001-pham-tu.md", "range": (21, 31)},
{"filename": "an-08-002-pham-lon.md", "range": (32, 10)},
{"filename": "an-08-003-pham-gia-chu.md", "range": (44, 10)},
{"filename": "an-08-004-pham-bo-thi.md", "range": (54, 10)},
{"filename": "an-08-005-pham-ngay-trai-gioi.md", "range": (65, 10)},
{"filename": "an-08-006-pham-gotami.md", "range": (75, 10)},
{"filename": "an-08-007-pham-dat-rung-dong.md", "range": (1, 10)},
{"filename": "an-08-008-pham-song-doi.md", "range": (1, 10)},
{"filename": "an-08-009-pham-niem.md", "range": (1, 10)},
{"filename": "an-08-010-pham-tham-ai.md", "range": (1, 10)},
{"filename": "an-09-000-chuong-9.md", "range": (1, 10)},
{"filename": "an-09-001-pham-chanh-giac.md", "range": (1, 10)},
{"filename": "an-09-002-pham-tieng-rong-con-su-tu.md", "range": (1, 10)},
{"filename": "an-09-003-pham-cho-cu-tru-cua-huu-tinh.md", "range": (1, 10)},
{"filename": "an-09-004-dai-pham.md", "range": (1, 10)},
{"filename": "an-09-005-pham-pancala.md", "range": (1, 10)},
{"filename": "an-09-006-pham-an-on.md", "range": (1, 10)},
{"filename": "an-09-007-pham-niem-xu.md", "range": (1, 10)},
{"filename": "an-09-008-pham-chanh-can.md", "range": (1, 10)},
{"filename": "an-09-009-pham-bon-nhu-y-tuc.md", "range": (1, 10)},
{"filename": "an-09-010-pham-tham.md", "range": (1, 10)},
{"filename": "an-10-000-chuong-10.md", "range": (1, 10)},
{"filename": "an-10-001-pham-loi-ich.md", "range": (1, 10)},
{"filename": "an-10-002-pham-ho-tri.md", "range": (1, 10)},
{"filename": "an-10-003-pham-lon.md", "range": (1, 10)},
{"filename": "an-10-004-pham-upali-va-ananda.md", "range": (1, 10)},
{"filename": "an-10-005-pham-mang-nhiec.md", "range": (1, 10)},
{"filename": "an-10-006-pham-tam-cua-minh.md", "range": (1, 10)},
{"filename": "an-10-007-pham-song-doi.md", "range": (1, 10)},
{"filename": "an-10-008-pham-uoc-nguyen.md", "range": (1, 10)},
{"filename": "an-10-009-pham-truong-lao.md", "range": (1, 10)},
{"filename": "an-10-010-pham-nam-cu-si.md", "range": (1, 10)},
{"filename": "an-10-011-pham-sa-mon-tuong.md", "range": (1, 10)},
{"filename": "an-10-012-pham-di-xuong.md", "range": (1, 10)},
{"filename": "an-10-013-pham-thanh-tinh.md", "range": (1, 10)},
{"filename": "an-10-014-pham-thien-luong.md", "range": (1, 10)},
{"filename": "an-10-015-pham-thanh-dao.md", "range": (1, 10)},
{"filename": "an-10-016-pham-nguoi.md", "range": (1, 10)},
{"filename": "an-10-017-pham-janussoni.md", "range": (1, 10)},
{"filename": "an-10-018-pham-thien-luong.md", "range": (1, 10)},
{"filename": "an-10-019-pham-thanh-dao.md", "range": (1, 10)},
{"filename": "an-10-020-pham-cac-hang-nguoi.md", "range": (1, 10)},
{"filename": "an-10-021-pham-than-do-nghiep-sanh.md", "range": (1, 10)},
{"filename": "an-10-022-pham-khong-co-dau-de.md", "range": (1, 10)},
{"filename": "an-11-000-chuong-11.md", "range": (1, 10)},
{"filename": "an-11-001-pham-y-chi.md", "range": (1, 10)},
{"filename": "an-11-002-pham-tuy-niem.md", "range": (1, 10)},
{"filename": "an-11-003-pham-ba-tong-ket.md", "range": (1, 10)},
]

# Heading cấp mấy được coi là "đoạn con" (### = 3, ## = 2, ...)
CHILD_HEADING_LEVEL = 1


# (Tùy chọn) đặt tiêu đề tay cho 1 top-index thay vì lấy H1 của file đầu tiên gặp.
# Hữu ích cho case gộp nhiều file (AN) vì H1 của từng phẩm không đại diện cho cả nipata.
NIPATA_TITLES = {
    # "1": "AN 1. Chương Một Pháp", "range": (1, 10)},
}

# Heading cấp mấy được coi là "đoạn con" (### = 3, ## = 2, ...)
CHILD_HEADING_LEVEL = 3
####
TOP_INDEX_RE = re.compile(r'^[a-z]+-0*(\d+)')
H1_RE = re.compile(r'^#\s+(.*)$', re.MULTILINE)
CHILD_RE = re.compile(r'^#{%d}\s+(.*)$' % CHILD_HEADING_LEVEL)
NUM_PREFIX_RE = re.compile(r'^(\d+(?:\.\d+)+)\.?\s*')


def slugify(text):
    """Đoán anchor kiểu markdown-it-anchor. Xem ghi chú ở đầu notebook."""
    text = text.strip()
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '-', text, flags=re.UNICODE)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def top_index_from_slug(slug):
    m = TOP_INDEX_RE.match(slug.lower())
    return m.group(1) if m else None


def extract_h1(text):
    m = H1_RE.search(text)
    return m.group(1).strip() if m else None


def insert_path(item, path, default_slug, slug=None, anchor=None):
    """Đi xuống item['children'][...] theo path (list số dạng string), tạo node
    nếu chưa có. Ở node lá: chỉ gắn slug nếu KHÁC trang mặc định của item (tránh
    lặp thừa khi con nằm cùng trang cha)."""
    node = item
    for i, k in enumerate(path):
        node.setdefault("children", {})
        node["children"].setdefault(k, {})
        node = node["children"][k]
        if i == len(path) - 1:
            if slug and slug != default_slug:
                node["slug"] = slug
            if anchor:
                node["anchor"] = anchor


def process_file(dirpath, spec, items, warnings, titles_override):
    filename = spec["filename"]
    file_range = spec.get("range")  # (start, end) hoặc None

    slug = filename[:-3] if filename.endswith(".md") else filename
    filepath = os.path.join(dirpath, filename)
    if not os.path.isfile(filepath):
        warnings.append(f"{filename}: không tìm thấy file, bỏ qua")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    top_index = top_index_from_slug(slug)
    if top_index is None:
        warnings.append(f"{filename}: không suy ra được số thứ tự (top index) từ tên file, bỏ qua")
        return
    key = str(int(top_index))

    is_new_key = key not in items
    item = items.setdefault(key, {})

    if is_new_key:
        if key in titles_override:
            item["title"] = titles_override[key]
        else:
            h1 = extract_h1(text)
            item["title"] = h1 if h1 else f"??? (chưa có tiêu đề cho key {key})"
            if not h1:
                warnings.append(f"{filename}: không tìm thấy H1, cần điền title tay cho key {key}")
        # Trang mặc định khi user chỉ gõ tới top-index (vd "an 1"), không có số con.
        # Với case gộp nhiều file, đây là trang của file ĐẦU TIÊN gặp trong danh sách FILES.
        item["slug"] = slug
    elif key in titles_override and item.get("title") != titles_override[key]:
        item["title"] = titles_override[key]

    default_slug = item["slug"]

    # 1) điền mặc định theo range khai báo -> đảm bảo MỌI số trong range có link,
    #    kể cả khi trong file không có heading riêng cho từng kinh
    if file_range:
        start, end = file_range
        for n in range(start, end + 1):
            insert_path(item, [str(n)], default_slug, slug=slug)

    # 2) quét heading đánh số trong file để bổ sung anchor chính xác (nếu có)
    for line in text.splitlines():
        m = CHILD_RE.match(line)
        if not m:
            continue
        heading_text = m.group(1).strip()
        num_match = NUM_PREFIX_RE.match(heading_text)
        if not num_match:
            continue
        numbers = num_match.group(1).split(".")
        if numbers[0] != key:
            warnings.append(
                f'{filename}: heading "{heading_text}" có số đầu ({numbers[0]}) khác key ({key})'
            )
            continue
        path = numbers[1:]
        if not path:
            continue
        anchor = slugify(heading_text)
        insert_path(item, path, default_slug, slug=slug, anchor=anchor)

##########

def run():

    items = {}
    warnings = []

    for spec in FILES:
        process_file(SOURCE_DIR, spec, items, warnings, NIPATA_TITLES)

    if warnings:
        print("⚠️  Cảnh báo:")
        for w in warnings:
            print(" -", w)
    else:
        print("Không có cảnh báo.")


    output = {
        "folder": "kinhtangchi",
        "editions": {
            "tmc": {
                "label": "Thích Minh Châu",
                "path": "thichminhchau",
                "index_length": "1",
                "items": items,
            }
        },
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))

run()