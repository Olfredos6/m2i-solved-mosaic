#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from io import BytesIO, StringIO

from PIL import Image as pil

# LOCAL_FOLDER_PATH = "E:\\work\\m2i\\PRF-CDA-0124(2024)\\3-html-et-css\\_\\mosaic\\images"  # Update with your local folder path
LOCAL_FOLDER_PATH = (
    "E:\\work\\m2i\\aud-d-html-css\\TP validation\\Énoncé\\images"  # tp validation
)


def start_compressing(dry_run=False):
    i = 0
    for filename in os.listdir(LOCAL_FOLDER_PATH):
        filepath = os.path.join(LOCAL_FOLDER_PATH, filename)
        if os.path.isfile(filepath) and os.path.getsize(filepath) > 500000:
            if not dry_run:
                compress_image(filepath, i)
            i += 1

    if dry_run:
        print(f"Will compress {i} images")
    else:
        print(f"Compressed {i} images")


def generate_result_path(filepath):
    filepath = filepath.split("\\")
    filepath.insert(-1, "compressed")
    filepath = "\\".join(filepath)
    return filepath


def compress_image(filepath, index):
    print("{0}: compressing image: {1}".format(index, filepath))
    img = pil.open(filepath)
    tmp = BytesIO()
    img.save(tmp, "JPEG", quality=13)
    tmp.seek(0)
    output_data = tmp.getvalue()

    # Handle saving the compressed image back to the local folder or any desired destination
    compressed_filepath = generate_result_path(filepath)
    with open(compressed_filepath, "wb") as compressed_file:
        compressed_file.write(output_data)

    tmp.close()


def compress_imagex(filepath, index):
    print("{index}: compressing image: {filepath}")
    img = pil.open(filepath)
    tmp = StringIO()
    img.save(tmp, "JPEG", quality=80)
    tmp.seek(0)
    output_data = tmp.getvalue()

    # Handle saving the compressed image back to the local folder or any desired destination
    compressed_filepath = f"{filepath}_compressed.jpg"
    with open(compressed_filepath, "wb") as compressed_file:
        compressed_file.write(output_data)

    tmp.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "dry_run":
            start_compressing(dry_run=True)
        else:
            print(
                "Invalid command. For a dry run please run: python compress_local_images.py dry_run"
            )
    else:
        start_compressing()
    sys.exit()
