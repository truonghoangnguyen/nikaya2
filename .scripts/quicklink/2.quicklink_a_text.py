import os
import re
import json
from util import flat_json

# ==========================================
# CẤU HÌNH ĐẦU VÀO
# ==========================================
SOURCE_DIR = "../../docs/kinhtrungbo/pali-vi"

FILES = [
   "mn-001-mulapariyayasutta.md",
"mn-002-sabbasavasutta.md",
"mn-003-dhammadayadasutta.md",
"mn-004-bhayabheravasutta.md",
"mn-005-ananganasutta.md",
"mn-006-akankheyyasutta.md",
"mn-007-vatthasutta.md",
"mn-008-sallekhasutta.md",
"mn-009-sammaditthisutta.md",
"mn-010-satipatthanasutta.md",
"mn-011-culasihanadasutta.md",
"mn-012-mahasihanadasutta.md",
"mn-013-mahadukkhakkhandhasutta.md",
"mn-014-culadukkhakkhandhasutta.md",
"mn-015-anumanasutta.md",
"mn-016-cetokhilasutta.md",
"mn-017-vanapatthasutta.md",
"mn-018-madhupindikasutta.md",
"mn-019-dvedhavitakkasutta.md",
"mn-020-vitakkasanthanasutta.md",
"mn-021-kakacupamasutta.md",
"mn-022-alagaddupamasutta.md",
"mn-023-vammikasutta.md",
"mn-024-rathavinitasutta.md",
"mn-025-nivapasutta.md",
"mn-026-pasarasisutta.md",
"mn-027-culahatthipadopamasutta.md",
"mn-028-mahahatthipadopamasutta.md",
"mn-029-mahasaropamasutta.md",
"mn-030-culasaropamasutta.md",
"mn-031-culagosingasutta.md",
"mn-032-mahagosingasutta.md",
"mn-033-mahagopalakasutta.md",
"mn-034-culagopalakasutta.md",
"mn-035-culasaccakasutta.md",
"mn-036-mahasaccakasutta.md",
"mn-037-culatanhasankhayasutta.md",
"mn-038-mahatanhasankhayasutta copy.md",
"mn-038-mahatanhasankhayasutta.md",
"mn-039-mahaassapurasutta.md",
"mn-040-culaassapurasutta.md",
"mn-041-saleyyakasutta.md",
"mn-042-veranjakasutta.md",
"mn-043-mahavedallasutta.md",
"mn-044-culavedallasutta.md",
"mn-045-culadhammasamadanasutta.md",
"mn-046-mahadhammasamadanasutta.md",
"mn-047-vimamsakasutta.md",
"mn-048-kosambiyasutta.md",
"mn-049-brahmanimantanikasutta.md",
"mn-050-maratajjaniyasutta.md",
"mn-051-kandarakasutta.md",
"mn-052-atthakanagarasutta.md",
"mn-053-sekhasutta.md",
"mn-054-potaliyasutta.md",
"mn-055-jivakasutta.md",
"mn-056-upalisutta.md",
"mn-057-kukkuravatikasutta.md",
"mn-058-abhayarajakumarasutta.md",
"mn-059-bahuvedaniyasutta.md",
"mn-060-apannakasutta.md",
"mn-061-ambalatthikarahulovadasutta.md",
"mn-062-maharahulovadasutta.md",
"mn-063-culamalukyasutta.md",
"mn-064-mahamalukyasutta.md",
"mn-065-bhaddalisutta.md",
"mn-066-latukikopamasutta.md",
"mn-067-catumasutta.md",
"mn-068-nalakapanasutta.md",
"mn-069-goliyanisutta.md",
"mn-070-kitagirisutta.md",
"mn-071-tevijjavacchasutta.md",
"mn-072-aggivacchasutta.md",
"mn-073-mahavacchasutta.md",
"mn-074-dighanakhasutta.md",
"mn-075-magandiyasutta.md",
"mn-076-sandakasutta.md",
"mn-077-mahasakuludayisutta.md",
"mn-078-samanamundikasutta.md",
"mn-079-culasakuludayisutta.md",
"mn-080-vekhanasasutta.md",
"mn-081-ghatikarasutta.md",
"mn-082-ratthapalasutta.md",
"mn-083-maghadevasutta.md",
"mn-084-madhurasutta.md",
"mn-085-bodhirajakumarasutta.md",
"mn-086-angulimalasutta.md",
"mn-087-piyajatikasutta.md",
"mn-088-bahitikasutta.md",
"mn-089-dhammacetiyasutta.md",
"mn-090-kannakatthalasutta.md",
"mn-091-brahmayusutta.md",
"mn-092-selasutta.md",
"mn-093-assalayanasutta.md",
"mn-094-ghotamukhasutta.md",
"mn-095-cankisutta.md",
"mn-096-esukarisutta.md",
"mn-097-dhananjanisutta.md",
"mn-098-vasetthasutta.md",
"mn-099-subhasutta.md",
"mn-100-sangaravasutta.md",
"mn-101-devadahasutta.md",
"mn-102-pancattayasutta.md",
"mn-103-kintisutta.md",
"mn-104-samagamasutta.md",
"mn-105-sunakkhattasutta.md",
"mn-106-anenjasappayasutta.md",
"mn-107-ganakamoggallanasutta.md",
"mn-108-gopakamoggallanasutta.md",
"mn-109-mahapunnamasutta.md",
"mn-110-culapunnamasutta.md",
"mn-111-anupadasutta.md",
"mn-112-chabbisodhanasutta.md",
"mn-113-sappurisasutta.md",
"mn-114-sevitabbasevitabbasutta.md",
"mn-115-bahudhatukasutta.md",
"mn-116-isigilisutta.md",
"mn-117-mahacattarisakasutta.md",
"mn-118-anapanassatisutta.md",
"mn-119-kayagatasatisutta.md",
"mn-120-sankharupapattisutta.md",
"mn-121-culasunnatasutta.md",
"mn-122-mahasunnatasutta.md",
"mn-123-acchariyaabbhutasutta.md",
"mn-124-bakulasutta.md",
"mn-125-dantabhumisutta.md",
"mn-126-bhumijasutta.md",
"mn-127-anuruddhasutta.md",
"mn-128-upakkilesasutta.md",
"mn-129-balapanditasutta.md",
"mn-130-devadutasutta.md",
"mn-131-bhaddekarattasutta.md",
"mn-132-anandabhaddekarattasutta.md",
"mn-133-mahakaccanabhaddekarattasutta.md",
"mn-134-lomasakangiyabhaddekarattasutta.md",
"mn-135-culakammavibhangasutta.md",
"mn-136-mahakammavibhangasutta.md",
"mn-137-salayatanavibhangasutta.md",
"mn-138-uddesavibhangasutta.md",
"mn-139-aranavibhangasutta.md",
"mn-140-dhatuvibhangasutta.md",
"mn-141-saccavibhangasutta.md",
"mn-142-dakkhinavibhangasutta.md",
"mn-143-anathapindikovadasutta.md",
"mn-144-channovadasutta.md",
"mn-145-punnovadasutta.md",
"mn-146-nandakovadasutta.md",
"mn-147-cularahulovadasutta.md",
"mn-148-chachakkasutta.md",
"mn-149-mahasalayatanikasutta.md",
"mn-150-nagaravindeyyasutta.md",
"mn-151-pindapataparisuddhisutta.md",
"mn-152-indriyabhavanasutta.md",
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
CHUONG_RE = re.compile(r'mn-*(\d+)', re.IGNORECASE)


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