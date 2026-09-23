#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def convert(source):
    source = Path(source).expanduser().resolve()

    if not source.is_file():
        print(f"Không tìm thấy file: {source}")
        sys.exit(1)

    stem = source.stem

    output_dir = Path('../docs/public/covers').resolve()

    commands = [
        [
            "cwebp",
            "-q", "85",
            "-resize", "300", "0",
            str(source),
            "-o", str(output_dir / f"{stem}-300w.webp"),
        ],
        [
            "cwebp",
            "-q", "85",
            "-resize", "600", "0",
            str(source),
            "-o", str(output_dir / f"{stem}-600w.webp"),
        ],
        [
            "cwebp",
            "-q", "85",
            str(source),
            "-o", str(output_dir / f"{stem}.webp"),
        ],
    ]

    for command in commands:
        print(" ".join(command))
        subprocess.run(command, check=True)

    print(f"\nDone: {output_dir}/{stem}-300w.webp")
    print(f"      {output_dir}/{stem}-600w.webp")
    print(f"      {output_dir}/{stem}.webp")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py /path/to/image.jpg")
        sys.exit(1)

    convert(sys.argv[1])