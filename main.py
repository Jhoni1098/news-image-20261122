#!/usr/bin/env python3
"""news-image-20261122 entrypoint (Python 3.13, standard library only).

Copies the pre-drawn front page ``entry.png`` (1024x1024 PNG, under 1 MiB)
from this repository into ``$MAKEFUN_OUTPUT_DIR/entry.png``. No network,
no timestamps, no randomness: the same input bytes always produce the
same output bytes. Validates the PNG header before copying so a corrupt
source fails loudly instead of shipping a broken entry.
"""

import hashlib
import os
import shutil
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def validate_png(path):
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError("entry.png is larger than 1024x1024")
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError("entry.png is larger than 1 MiB")
    return width, height, size


def main():
    src = source_path()
    width, height, size = validate_png(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    with open(src, "rb") as handle:
        expected = handle.read()
    with open(dest, "rb") as handle:
        written = handle.read()
    if written != expected:
        raise ValueError("written entry.png differs from the source")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {dest} ({width}x{height}, {size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
