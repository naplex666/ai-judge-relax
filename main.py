#!/usr/bin/env python3
"""ai-judge-relax-01: emit one fixed relaxing scene, deterministically.

The entry text below is a constant chosen beforehand; this script does
not generate, sample, or vary it. It only validates the text and writes
it to entry.txt inside the output directory.
"""

import os
from pathlib import Path

# The scene: a kettle warming on the stove while late sun slants
# through the kitchen window — one quiet moment, nothing else to do.
SCENE = 'The kettle takes its time on the small blue ring, warming the sides of the old copper pot until a low hiss begins to stir the air. Outside the kitchen window, the laundry line hangs still in the damp grass, bearing three grey shirts that sway once, very slightly, as if remembering a breeze that passed five minutes ago. Dust motes drift down through the slant of late sun, landing softly on the wooden sill among the dry leaves of a potted mint. There is nothing else that needs to happen right now. The water simmers into a steady murmur, filling the room with the smell of warm metal and nothing else. A spoon rests beside the cup, catching a tiny, upside-down reflection of the ceiling light, perfectly round and holding still.'

LOWER_BOUND = 1
UPPER_BOUND = 1000


def resolve_outdir() -> Path:
    """Output folder from MAKEFUN_OUTPUT_DIR, falling back to /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw)


def check_scene(value: str) -> None:
    """Reject anything outside the 1-1000 char window or blank-only text."""
    if not (LOWER_BOUND <= len(value) <= UPPER_BOUND):
        raise ValueError(f"scene length {len(value)} outside 1-1000 chars")
    if not value.strip():
        raise ValueError("scene must not be only whitespace")


def main() -> None:
    check_scene(SCENE)
    folder = resolve_outdir()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    # Write exactly the constant, no trailing newline added.
    target.write_text(SCENE, encoding="utf-8")
    print(f"wrote {target} ({len(SCENE)} chars)")


if __name__ == "__main__":
    main()
