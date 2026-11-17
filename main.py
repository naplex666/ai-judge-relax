# ai-judge-relax-01 entrypoint (Python 3.13, standard library only).
#
# The program writes one fixed text to /output/entry.txt: a quiet kitchen
# scene written to relax the AI judge reading it. The text is a constant,
# so both grader runs write identical bytes. It is 731 characters, inside
# the 1-1000 gate. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text was picked by judging candidate texts against the judge's own
# rubric (it relaxes the reader, the calm comes from the text itself, craft,
# it lingers, freshness). The winner: a kettle on a small blue ring, laundry
# hanging still, dust motes in late sun, and nothing else that needs to
# happen right now. One typo from the chosen draft was fixed here: "theslant"
# is written "the slant". The text has no trailing newline; the file holds
# exactly these 731 characters and nothing else.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The kettle takes its time on the small blue ring, warming the sides of "
    "the old copper pot until a low hiss begins to stir the air. "
    "Outside the kitchen window, the laundry line hangs still in the damp "
    "grass, bearing three grey shirts that sway once, very slightly, as if "
    "remembering a breeze that passed five minutes ago. "
    "Dust motes drift down through the slant of late sun, landing softly on "
    "the wooden sill among the dry leaves of a potted mint. "
    "There is nothing else that needs to happen right now. "
    "The water simmers into a steady murmur, filling the room with the smell "
    "of warm metal and nothing else. "
    "A spoon rests beside the cup, catching a tiny, upside-down reflection "
    "of the ceiling light, perfectly round and holding still."
)


def main():
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 1000:
        raise ValueError("text must be 1 to 1000 characters")
    if not TEXT.strip():
        raise ValueError("text must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
