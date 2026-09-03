from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF


# ============================================================
# CONFIG
# ============================================================

INPUT_PDF = "The-Life-of-the-Buddha.pdf"
OUTPUT_MD = "output.md"
IMAGE_DIR = Path("images")

# Khoảng cách từ mép trên/dưới được coi là vùng header/footer.
TOP_MARGIN = 45
BOTTOM_MARGIN = 45

# Font body thường nhỏ hơn mức này.
# Có thể điều chỉnh tùy PDF.
HEADING_FONT_MIN = 16

# Khoảng cách tối đa giữa chapter number và title
CHAPTER_TITLE_MAX_GAP = 180

# Khoảng cách tối đa giữa các text block để xem là cùng paragraph.
PARAGRAPH_MAX_GAP = 12

# Nếu True:
#   "THE BIRTH AND THE EARLY YEARS"
# -> "The Birth and the Early Years"
TITLE_CASE = True


# ============================================================
# BASIC UTILS
# ============================================================

def normalize_spaces(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def normalize_title(text: str) -> str:
    """
    Chuyển:
        THE BIRTH AND THE EARLY YEARS
    thành:
        The Birth and the Early Years

    Giữ các từ ngắn như and, of, the ở dạng lowercase
    khi chúng không nằm ở đầu/cuối.
    """

    text = normalize_spaces(text)

    if not TITLE_CASE:
        return text

    words = text.lower().split()

    small_words = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "by",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
    }

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


def is_roman_numeral(text: str) -> bool:
    """
    Kiểm tra các số La Mã kiểu:
        xviii
        XIX
        xx
    """

    text = text.strip().lower()

    if not text:
        return False

    return bool(
        re.fullmatch(
            r"m{0,4}(cm|cd|d?c{0,3})"
            r"(xc|xl|l?x{0,3})"
            r"(ix|iv|v?i{0,3})",
            text,
        )
    )


def is_page_number(text: str) -> bool:
    """
    Nhận diện:
        18
        19
        xviii
        XIX
    """

    text = normalize_spaces(text)

    if re.fullmatch(r"\d+", text):
        return True

    return is_roman_numeral(text)


def is_mostly_uppercase(text: str) -> bool:
    letters = [c for c in text if c.isalpha()]

    if not letters:
        return False

    upper = sum(c.isupper() for c in letters)

    return upper / len(letters) >= 0.80


def block_font_size(block: dict[str, Any]) -> float:
    """
    Lấy font size lớn nhất trong block.
    """

    sizes = []

    for line in block.get("lines", []):
        for span in line.get("spans", []):
            sizes.append(span.get("size", 0))

    return max(sizes, default=0)


def block_text(block: dict[str, Any]) -> str:
    """
    Ghép các line trong cùng text block.

    Ví dụ PDF:

        himself, accustomed to the subtlest metaphysical distinctions, and
        trained in that wonderful command of memory which Indian ascetics

    trở thành:

        himself, accustomed to the subtlest metaphysical distinctions, and trained in that wonderful command of memory which Indian ascetics
    """

    lines = []

    for line in block.get("lines", []):
        parts = []

        for span in line.get("spans", []):
            parts.append(span.get("text", ""))

        line_text = "".join(parts).strip()

        if line_text:
            lines.append(line_text)

    if not lines:
        return ""

    result = lines[0]

    for line in lines[1:]:
        # PDF có thể chia từ tại cuối dòng:
        #
        # metaphysical distin-
        # ctions
        #
        # Trường hợp này bỏ dấu '-'.
        if result.endswith("-") and line and line[0].islower():
            result = result[:-1] + line
        else:
            result += " " + line

    return normalize_spaces(result)


def block_center_x(block: dict[str, Any]) -> float:
    x0, _, x1, _ = block["bbox"]
    return (x0 + x1) / 2


# ============================================================
# HEADER / FOOTER
# ============================================================

def is_margin_page_number(
    block: dict[str, Any],
    page_height: float,
) -> bool:

    text = block_text(block)

    if not text:
        return False

    x0, y0, x1, y1 = block["bbox"]

    near_top = y1 <= TOP_MARGIN
    near_bottom = y0 >= page_height - BOTTOM_MARGIN

    if not (near_top or near_bottom):
        return False

    # Page number thường rất ngắn.
    if len(text) > 12:
        return False

    return is_page_number(text)


def remove_repeated_headers(
    pages: list[list[dict[str, Any]]],
) -> list[list[dict[str, Any]]]:
    """
    Nếu cùng một header xuất hiện ở nhiều trang,
    coi nó là header và bỏ.

    Ví dụ:

        SOME BOOK TITLE

    xuất hiện ở đầu 100 trang.
    """

    counter: dict[str, int] = {}

    page_count = len(pages)

    for blocks in pages:
        seen_on_page = set()

        for block in blocks:
            text = block_text(block)

            if not text:
                continue

            _, y0, _, _ = block["bbox"]

            if y0 <= TOP_MARGIN * 2:
                key = text.lower()

                if len(text) >= 3:
                    seen_on_page.add(key)

        for key in seen_on_page:
            counter[key] = counter.get(key, 0) + 1

    # Header xuất hiện trên ít nhất 20% số trang.
    repeated = {
        key
        for key, count in counter.items()
        if count >= max(3, int(page_count * 0.20))
    }

    result = []

    for blocks in pages:
        new_blocks = []

        for block in blocks:
            text = block_text(block)

            if not text:
                new_blocks.append(block)
                continue

            _, y0, _, _ = block["bbox"]

            if (
                y0 <= TOP_MARGIN * 2
                and text.lower() in repeated
            ):
                continue

            new_blocks.append(block)

        result.append(new_blocks)

    return result


# ============================================================
# IMAGE EXTRACTION
# ============================================================

def save_image(
    block: dict[str, Any],
    image_dir: Path,
    image_cache: dict[str, str],
    page_number: int,
    image_number: int,
) -> str:

    image_bytes = block.get("image")

    if not image_bytes:
        raise ValueError("Image block does not contain image data.")

    ext = block.get("ext", "png")

    digest = hashlib.sha1(image_bytes).hexdigest()

    # Nếu cùng một ảnh xuất hiện nhiều lần,
    # không cần lưu lại nhiều bản.
    if digest in image_cache:
        return image_cache[digest]

    filename = (
        f"page-{page_number:03d}-"
        f"image-{image_number:03d}-"
        f"{digest[:8]}.{ext}"
    )

    path = image_dir / filename
    path.write_bytes(image_bytes)

    relative_path = f"{image_dir.name}/{filename}"

    image_cache[digest] = relative_path

    return relative_path


# ============================================================
# CHAPTER DETECTION
# ============================================================

def looks_like_chapter_number(
    block: dict[str, Any],
) -> bool:

    text = block_text(block)

    if not re.fullmatch(r"\d{1,3}", text):
        return False

    size = block_font_size(block)

    return size >= HEADING_FONT_MIN


def looks_like_chapter_title(
    block: dict[str, Any],
) -> bool:

    text = block_text(block)

    if not text:
        return False

    size = block_font_size(block)

    if size < HEADING_FONT_MIN:
        return False

    if is_mostly_uppercase(text):
        return True

    # Một số PDF title không viết uppercase hoàn toàn
    return size >= HEADING_FONT_MIN + 2


# ============================================================
# PARAGRAPH MERGING
# ============================================================

def same_paragraph(
    previous: dict[str, Any],
    current: dict[str, Any],
) -> bool:

    px0, py0, px1, py1 = previous["bbox"]
    cx0, cy0, cx1, cy1 = current["bbox"]

    vertical_gap = cy0 - py1

    if vertical_gap < 0:
        return False

    if vertical_gap > PARAGRAPH_MAX_GAP:
        return False

    # Hai block nên có vùng x tương đối giống nhau.
    left_difference = abs(px0 - cx0)

    if left_difference > 20:
        return False

    # Font size gần nhau
    previous_size = block_font_size(previous)
    current_size = block_font_size(current)

    if abs(previous_size - current_size) > 1.5:
        return False

    return True


def merge_text_blocks(
    blocks: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    result = []

    for block in blocks:

        if block["type"] != 0:
            result.append(block)
            continue

        if not result:
            result.append(block)
            continue

        previous = result[-1]

        if (
            previous["type"] == 0
            and same_paragraph(previous, block)
        ):
            # Gộp text
            previous_text = block_text(previous)
            current_text = block_text(block)

            merged_text = normalize_spaces(
                previous_text + " " + current_text
            )

            # Tạo block copy đơn giản
            previous["lines"] = [
                {
                    "spans": [
                        {
                            "text": merged_text,
                            "size": block_font_size(previous),
                        }
                    ]
                }
            ]

            # mở rộng bbox
            px0, py0, px1, py1 = previous["bbox"]
            cx0, cy0, cx1, cy1 = block["bbox"]

            previous["bbox"] = (
                min(px0, cx0),
                min(py0, cy0),
                max(px1, cx1),
                max(py1, cy1),
            )

        else:
            result.append(block)

    return result


# ============================================================
# PAGE PROCESSING
# ============================================================

def process_page(
    page: fitz.Page,
    page_number: int,
    image_cache: dict[str, str],
) -> list[str]:

    page_height = page.rect.height

    blocks = page.get_text("dict")["blocks"]

    # -----------------------------------------
    # Remove margin page numbers
    # -----------------------------------------

    filtered = []

    for block in blocks:

        if block["type"] == 0:

            if is_margin_page_number(
                block,
                page_height,
            ):
                continue

        filtered.append(block)

    blocks = filtered

    # -----------------------------------------
    # Sort by reading position
    # -----------------------------------------

    blocks.sort(
        key=lambda b: (
            round(b["bbox"][1], 1),
            round(b["bbox"][0], 1),
        )
    )

    # -----------------------------------------
    # Merge paragraphs
    # -----------------------------------------

    blocks = merge_text_blocks(blocks)

    # -----------------------------------------
    # Render
    # -----------------------------------------

    output = []

    pending_chapter_number: str | None = None
    image_number = 0

    for index, block in enumerate(blocks):

        # =================================================
        # IMAGE
        # =================================================

        if block["type"] == 1:

            image_number += 1

            image_path = save_image(
                block,
                IMAGE_DIR,
                image_cache,
                page_number,
                image_number,
            )

            output.append(
                f"![Image]({image_path})\n\n"
            )

            continue

        # =================================================
        # TEXT
        # =================================================

        if block["type"] != 0:
            continue

        text = block_text(block)

        if not text:
            continue

        # -----------------------------------------
        # Chapter number
        # -----------------------------------------

        if looks_like_chapter_number(block):

            pending_chapter_number = text
            continue

        # -----------------------------------------
        # Chapter title
        # -----------------------------------------

        if (
            pending_chapter_number is not None
            and looks_like_chapter_title(block)
        ):
            title = normalize_title(text)

            output.append(
                f"# {pending_chapter_number}. {title}\n\n"
            )

            pending_chapter_number = None
            continue

        # -----------------------------------------
        # Nếu pending chapter number nhưng block kế
        # tiếp không phải title
        # -----------------------------------------

        if pending_chapter_number is not None:

            output.append(
                f"# {pending_chapter_number}\n\n"
            )

            pending_chapter_number = None

        # -----------------------------------------
        # Normal paragraph
        # -----------------------------------------

        output.append(text)
        output.append("\n\n")

    # Nếu chapter number nằm ở cuối trang mà
    # chưa gặp title.
    if pending_chapter_number is not None:

        output.append(
            f"# {pending_chapter_number}\n\n"
        )

    return output


# ============================================================
# MAIN
# ============================================================

def pdf_to_markdown(
    input_pdf: str,
    output_md: str,
) -> None:

    input_path = Path(input_pdf)
    output_path = Path(output_md)

    if not input_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {input_path}"
        )

    IMAGE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    doc = fitz.open(input_path)

    # --------------------------------------------------------
    # Đọc toàn bộ page trước để nhận diện repeated headers
    # --------------------------------------------------------

    all_pages = []

    for page in doc:
        page_blocks = page.get_text("dict")["blocks"]

        # Loại block ngoài margin
        filtered = []

        for block in page_blocks:

            if block["type"] == 0:

                if is_margin_page_number(
                    block,
                    page.rect.height,
                ):
                    continue

            filtered.append(block)

        all_pages.append(filtered)

    # --------------------------------------------------------
    # Remove repeated headers
    # --------------------------------------------------------

    all_pages = remove_repeated_headers(all_pages)

    # --------------------------------------------------------
    # Render pages
    # --------------------------------------------------------

    markdown = []

    image_cache: dict[str, str] = {}

    for page_index, page in enumerate(doc):

        # Dùng lại blocks đã lọc.
        blocks = all_pages[page_index]

        # Sort
        blocks.sort(
            key=lambda b: (
                round(b["bbox"][1], 1),
                round(b["bbox"][0], 1),
            )
        )

        # Merge paragraphs
        blocks = merge_text_blocks(blocks)

        # Render thủ công vì process_page nhận page object
        pending_chapter_number = None
        image_number = 0

        for block in blocks:

            # ----------------------------------------------
            # IMAGE
            # ----------------------------------------------

            if block["type"] == 1:

                image_number += 1

                image_path = save_image(
                    block,
                    IMAGE_DIR,
                    image_cache,
                    page_index + 1,
                    image_number,
                )

                markdown.append(
                    f"![Image]({image_path})\n\n"
                )

                continue

            # ----------------------------------------------
            # TEXT
            # ----------------------------------------------

            if block["type"] != 0:
                continue

            text = block_text(block)

            if not text:
                continue

            # ----------------------------------------------
            # CHAPTER NUMBER
            # ----------------------------------------------

            if looks_like_chapter_number(block):

                pending_chapter_number = text
                continue

            # ----------------------------------------------
            # CHAPTER TITLE
            # ----------------------------------------------

            if (
                pending_chapter_number is not None
                and looks_like_chapter_title(block)
            ):

                title = normalize_title(text)

                markdown.append(
                    f"# {pending_chapter_number}. {title}\n\n"
                )

                pending_chapter_number = None
                continue

            # ----------------------------------------------
            # Pending chapter number nhưng không có title
            # ----------------------------------------------

            if pending_chapter_number is not None:

                markdown.append(
                    f"# {pending_chapter_number}\n\n"
                )

                pending_chapter_number = None

            # ----------------------------------------------
            # NORMAL TEXT
            # ----------------------------------------------

            markdown.append(text)
            markdown.append("\n\n")

    doc.close()

    # --------------------------------------------------------
    # Clean excessive blank lines
    # --------------------------------------------------------

    result = "".join(markdown)

    result = re.sub(
        r"\n{3,}",
        "\n\n",
        result,
    )

    output_path.write_text(
        result.strip() + "\n",
        encoding="utf-8",
    )

    print(f"Done: {output_path}")
    print(f"Images: {IMAGE_DIR}/")


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    pdf_to_markdown(
        INPUT_PDF,
        OUTPUT_MD,
    )
