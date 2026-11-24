"""Publish the prepared news illustration without network access."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE_LIMIT = 1024 * 1024


def main():
    artwork = (ROOT / "world-news.jpg").read_bytes()
    if len(artwork) > IMAGE_LIMIT or not artwork.startswith(b"\xff\xd8") or not artwork.endswith(b"\xff\xd9"):
        raise ValueError("Expected a complete JPEG no larger than 1 MiB")

    output_directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "entry.png").write_bytes(artwork)


if __name__ == "__main__":
    main()
