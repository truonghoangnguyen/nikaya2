#!/usr/bin/env python3
"""
Script đổi tên các file có dạng *-tap-8*.md thành *-thag-*.md
trong một folder chỉ định.
"""

import os
import re
import sys
import argparse


def rename_files(folder: str, dry_run: bool = False) -> None:
    if not os.path.isdir(folder):
        print(f"❌ Folder không tồn tại: {folder}")
        sys.exit(1)

    # Pattern: khớp "tap-8" trong tên file .md
    pattern = re.compile(r"thag")
    count = 0

    for filename in os.listdir(folder):
        if not filename.endswith(".md"):
            continue
        if not pattern.search(filename):
            continue

        new_name = pattern.sub("tap-8", filename)

        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)

        if os.path.exists(new_path) and new_path != old_path:
            print(f"⚠️  Bỏ qua (đích đã tồn tại): {new_name}")
            continue

        if dry_run:
            print(f"[DRY-RUN] {filename}  →  {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"✅ {filename}  →  {new_name}")
        count += 1

    print(f"\nTổng cộng: {count} file {'sẽ được' if dry_run else 'đã được'} đổi tên.")


def main():


    pa = "/Users/ng/projects/nikaya2/docs/kinhtieubo/thichminhchau"
    rename_files(pa, dry_run=False)


if __name__ == "__main__":
    main()