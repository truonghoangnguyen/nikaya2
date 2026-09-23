import os
import re
import unicodedata


def slugify(text):
    # Strip H1 prefix and whitespace
    text = text.lstrip('#').strip()
    # Handle Vietnamese Đ/đ separately
    text = text.replace('Đ', 'D').replace('đ', 'd')
    # Decompose unicode accents
    normalized = unicodedata.normalize('NFKD', text)
    # Convert to ASCII by ignoring non-ASCII characters
    ascii_text = normalized.encode('ascii', 'ignore').decode('ascii')
    # Lowercase
    ascii_text = ascii_text.lower()
    # Replace non-alphanumeric characters with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', ascii_text)
    # Strip extra hyphens
    slug = slug.strip('-')

    return slug


def main():
    inputfile = [
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/01-loi-tua.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/02-gioi-thieu.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/03-i-cuoc-oi-cua-uc-phat.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/04-ii-hinayana-tieu-thua-phat-giao-cua-su-giai-thoat-thong-qua-no-luc-tu-than.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/05-iii-mahayana-phat-giao-nhat-nguyen-ve-su-giai-thoat-nho-vao-tha-luc-19-note.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/06-iv-cac-truong-phai-triet-hoc-ai-thua.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/07-phan-v-mat-tong-va-phat-giao-ong-a.md",
"/Users/ng/projects/nikaya2/docs/giaolyvatongphai/08-vi-mot-cai-nhin-tong-quan-ve-van-hoa-lich-su.md"
    ]

    for file_path in inputfile:

        if not os.path.isfile(file_path):
            print(f"File does not exist: {file_path}")
            continue

        filename = os.path.basename(file_path)

        # Lấy 2 số đầu tiên trong tên file làm prefix
        match = re.search(r'\d{2}', filename)

        if not match:
            print(f"Không tìm thấy 2 số đầu tiên trong: {filename}")
            continue

        file_prefix = match.group(0)

        # Read the first line to get H1 heading
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()

        if first_line.startswith('# '):
            title = first_line.strip()
            slug = slugify(title)

            if slug:
                directory = os.path.dirname(file_path)
                new_filename = f"{file_prefix}-{slug}.md"
                new_file_path = os.path.join(directory, new_filename)

                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} -> {new_filename}")
            else:
                print(
                    f"Could not generate slug for H1 in {filename}: "
                    f"'{first_line.strip()}'"
                )
        else:
            print(
                f"First line of {filename} is not an H1 heading: "
                f"'{first_line.strip()}'"
            )


if __name__ == "__main__":
    main()