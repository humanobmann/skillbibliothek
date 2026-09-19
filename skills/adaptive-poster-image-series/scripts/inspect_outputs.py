#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

from PIL import Image, ImageOps

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def parse_ratio(value: str) -> tuple[int, int]:
    try:
        a, b = value.split(":", 1)
        a_i, b_i = int(a), int(b)
        if a_i <= 0 or b_i <= 0:
            raise ValueError
        return a_i, b_i
    except Exception as exc:
        raise argparse.ArgumentTypeError("aspect ratio must look like 4:5 or 1:1") from exc


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Read-only inspection of image-tool outputs")
    p.add_argument("directory", type=Path)
    p.add_argument("--count", type=int, required=True)
    p.add_argument("--aspect-ratio", type=parse_ratio, required=True)
    p.add_argument("--min-width", type=int, default=0)
    p.add_argument("--min-height", type=int, default=0)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if not args.directory.is_dir():
        print("FAIL: output directory does not exist", file=sys.stderr)
        return 1
    files = sorted(p for p in args.directory.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED)
    if len(files) != args.count:
        print(f"FAIL: expected {args.count} images, found {len(files)}", file=sys.stderr)
        return 1
    failures: list[str] = []
    hashes: set[str] = set()
    ar_w, ar_h = args.aspect_ratio
    target = ar_w / ar_h
    for path in files:
        digest = sha256(path)
        if digest in hashes:
            failures.append(f"{path.name}: exact duplicate bytes")
        hashes.add(digest)
        try:
            with Image.open(path) as raw:
                image = ImageOps.exif_transpose(raw)
                w, h = image.size
                if abs((w / h) - target) > 0.002:
                    failures.append(f"{path.name}: ratio {w}:{h} does not match {ar_w}:{ar_h}")
                if args.min_width and w < args.min_width:
                    failures.append(f"{path.name}: width {w} below {args.min_width}")
                if args.min_height and h < args.min_height:
                    failures.append(f"{path.name}: height {h} below {args.min_height}")
        except OSError as exc:
            failures.append(f"{path.name}: unreadable image ({exc})")
    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1
    print("PASS: image files are readable, unique by bytes and match the requested aspect ratio.")
    print("NOTE: this script is read-only and does not create, crop, resize or alter images.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
