import os
import re
import unicodedata

def slugify(text):
    # Strip H1 prefix and whitespace
    text = text.lstrip('#').strip()
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
    output_dir = "/Users/ng/projects/n5/docs/kinhtruongbo/pali-vi"

    if not os.path.exists(output_dir):
        print(f"Directory {output_dir} does not exist.")
        return

    files = [f for f in os.listdir(output_dir) if f.endswith(".md")]

    # Process files matching "sn-XXX.md"
    for file in files:
        match = re.match(r'^(dn-\d+)\.md$', file)
        if not match:
            continue

        file_prefix = match.group(1)
        file_path = os.path.join(output_dir, file)

        # Read the first line to get H1 heading
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()

        if first_line.startswith('# '):
            title = first_line.strip()
            slug = slugify(title)

            if slug:
                new_filename = f"{file_prefix}-{slug}.md"
                new_file_path = os.path.join(output_dir, new_filename)

                os.rename(file_path, new_file_path)
                print(f"Renamed {file} -> {new_filename}")
            else:
                print(f"Could not generate slug for H1 in {file}: '{first_line.strip()}'")
        else:
            print(f"First line of {file} is not an H1 heading: '{first_line.strip()}'")

if __name__ == "__main__":
    main()
