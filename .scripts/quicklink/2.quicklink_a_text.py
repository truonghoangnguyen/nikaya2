import os
import re
import json
from util import flat_json

# ==========================================
# CẤU HÌNH ĐẦU VÀO
# ==========================================
SOURCE_DIR = "../../docs/kinhtrungbo/nanamoli-bodhi-vi"

FILES = [
"mn-001-the-root-of-all-things.md",
"mn-002-all-the-taints.md",
"mn-003-heirs-in-dhamma.md",
"mn-004-fear-and-dread.md",
"mn-005-without-blemishes.md",
"mn-006-if-a-bhikkhu-should-wish.md",
"mn-007-the-simile-of-the-cloth.md",
"mn-008-effacement.md",
"mn-009-right-view.md",
"mn-010-the-foundations-of-mindfulness.md",
"mn-011-the-shorter-discourse-on-the-lion-s-roar.md",
"mn-012-the-greater-discourse-on-the-lion-s-roar.md",
"mn-013-the-greater-discourse-on-the-mass-of-suffering.md",
"mn-014-the-shorter-discourse-on-the-mass-of-suffering.md",
"mn-015-inference.md",
"mn-016-the-wilderness-in-the-heart.md",
"mn-017-jungle-thickets.md",
"mn-018-the-honeyball.md",
"mn-019-two-kinds-of-thought.md",
"mn-020-the-removal-of-distracting-thoughts.md",
"mn-021-the-simile-of-the-saw.md",
"mn-022-the-simile-of-the-snake.md",
"mn-023-the-ant-hill.md",
"mn-024-the-relay-chariots.md",
"mn-025-the-bait.md",
"mn-026-the-noble-search.md",
"mn-027-the-shorter-discourse-on-the-simile-of-the-elephant-s-footprint.md",
"mn-028-the-greater-discourse-on-the-simile-of-the-elephant-s-footprint.md",
"mn-029-the-greater-discourse-on-the-simile-of-the-heartwood.md",
"mn-030-the-shorter-discourse-on-the-simile-of-the-heartwood.md",
"mn-031-the-shorter-discourse-in-gosinga.md",
"mn-032-the-greater-discourse-in-gosinga.md",
"mn-033-the-greater-discourse-on-the-cowherd.md",
"mn-034-the-shorter-discourse-on-the-cowherd.md",
"mn-035-the-shorter-discourse-to-saccaka.md",
"mn-036-the-greater-discourse-to-saccaka.md",
"mn-037-the-shorter-discourse-on-the-destruction-of-craving.md",
"mn-038-the-greater-discourse-on-the-destruction-of-craving.md",
"mn-039-the-greater-discourse-at-assapura.md",
"mn-040-the-shorter-discourse-at-assapura.md",
"mn-041-the-brahmins-of-sala.md",
"mn-042-the-brahmins-of-veranja.md",
"mn-043-the-greater-series-of-questions-and-answers.md",
"mn-044-the-shorter-series-of-questions-and-answers.md",
"mn-045-the-shorter-discourse-on-ways-of-undertaking-things.md",
"mn-046-the-greater-discourse-on-ways-of-undertaking-things.md",
"mn-047-the-inquirer.md",
"mn-048-the-kosambians.md",
"mn-049-the-invitation-of-a-brahma.md",
"mn-050-the-rebuke-to-mara.md",
"mn-051-to-kandaraka.md",
"mn-052-the-man-from-atthakanagara.md",
"mn-053-the-disciple-in-higher-training.md",
"mn-054-to-potaliya.md",
"mn-055-to-jivaka.md",
"mn-056-to-upali.md",
"mn-057-the-dog-duty-ascetic.md",
"mn-058-to-prince-abhaya.md",
"mn-059-the-many-kinds-of-feeling.md",
"mn-060-the-incontrovertible-teaching.md",
"mn-061-advice-to-rahula-at-ambalatthika.md",
"mn-062-the-greater-discourse-of-advice-to-rahula.md",
"mn-063-the-shorter-discourse-to-malunkyaputta.md",
"mn-064-the-greater-discourse-to-malunkyaputta.md",
"mn-065-to-bhaddali.md",
"mn-066-the-simile-of-the-quail.md",
"mn-067-at-catuma.md",
"mn-068-at-nalakapana.md",
"mn-069-gulissani.md",
"mn-070-at-kitagiri.md",
"mn-071-to-vacchagotta-on-the-threefold-true-knowledge.md",
"mn-072-to-vacchagotta-on-fire.md",
"mn-073-the-greater-discourse-to-vacchagotta.md",
"mn-074-to-dighanakha.md",
"mn-075-to-magandiya.md",
"mn-076-to-sandaka.md",
"mn-077-the-greater-discourse-to-sakuludayin.md",
"mn-078-samanamanikaputta.md",
"mn-079-the-shorter-discourse-to-sakuludayin.md",
"mn-080-to-vekhanassa.md",
"mn-081-ghatikara-the-potter.md",
"mn-082-on-ratthapala.md",
"mn-083-king-makhadeva.md",
"mn-084-at-madhura.md",
"mn-085-to-prince-bodhi.md",
"mn-086-on-angulimala.md",
"mn-087-born-from-those-who-are-dear.md",
"mn-088-the-cloak.md",
"mn-089-monuments-to-the-dhamma.md",
"mn-090-at-kannakatthala.md",
"mn-091-brahmayu.md",
"mn-092-to-sela.md",
"mn-093-to-assalayana.md",
"mn-094-to-ghotamukha.md",
"mn-095-with-canki.md",
"mn-096-to-esukari.md",
"mn-097-to-dhananjani.md",
"mn-098-to-vasettha.md",
"mn-099-to-subha.md",
"mn-100-to-sangarava.md",
"mn-101-at-devadaha.md",
"mn-102-the-five-and-three.md",
"mn-103-what-do-you-think-about-me.md",
"mn-104-at-samagama.md",
"mn-105-to-sunakkhatta.md",
"mn-106-the-way-to-the-imperturbable.md",
"mn-107-to-ganaka-moggallana.md",
"mn-108-with-gopaka-moggallana.md",
"mn-109-the-greater-discourse-on-the-full-moon-night.md",
"mn-110-the-shorter-discourse-on-the-full-moon-night.md",
"mn-111-one-by-one-as-they-occurred.md",
"mn-112-the-sixfold-purity.md",
"mn-113-the-true-man.md",
"mn-114-to-be-cultivated-and-not-to-be-cultivated.md",
"mn-115-the-many-kinds-of-elements.md",
"mn-116-isigili-the-gullet-of-the-seers.md",
"mn-117-the-great-forty.md",
"mn-118-mindfulness-of-breathing.md",
"mn-119-mindfulness-of-the-body.md",
"mn-120-reappearance-by-aspiration.md",
"mn-121-the-shorter-discourse-on-voidness.md",
"mn-122-the-greater-discourse-on-voidness.md",
"mn-123-wonderful-and-marvellous.md",
"mn-124-bakkula.md",
"mn-125-the-grade-of-the-tamed.md",
"mn-126-bhumija.md",
"mn-127-anuruddha.md",
"mn-128-imperfections.md",
"mn-129-fools-and-wise-men.md",
"mn-130-the-divine-messengers.md",
"mn-131-one-fortunate-attachment.md",
"mn-132-ananda-and-one-fortunate-attachment.md",
"mn-133-maha-kaccana-and-one-fortunate-attachment.md",
"mn-134-lomasakangiya-and-one-fortunate-attachment.md",
"mn-135-the-shorter-exposition-of-action.md",
"mn-136-the-greater-exposition-of-action.md",
"mn-137-the-exposition-of-the-sixfold-base.md",
"mn-138-the-exposition-of-a-summary.md",
"mn-139-the-exposition-of-non-conflict.md",
"mn-140-the-exposition-of-the-elements.md",
"mn-141-the-exposition-of-the-truths.md",
"mn-142-the-exposition-of-offerings.md",
"mn-143-advice-to-anathapinika.md",
"mn-144-advice-to-channa.md",
"mn-145-advice-to-punna.md",
"mn-146-advice-from-nandaka.md",
"mn-147-the-shorter-discourse-of-advice-to-rahula.md",
"mn-148-the-six-sets-of-six.md",
"mn-149-the-great-sixfold-base.md",
"mn-150-to-the-nagaravindans.md",
"mn-151-the-purification-of-almsfood.md",
"mn-152-the-development-of-the-faculties.md",
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