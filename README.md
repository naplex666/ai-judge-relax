# ai-judge-relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

Entry for the make.fun **ai-judge-relax-01** bounty: a short, calming piece of
prose meant to relax the AI judge that reads it.

The scene is a quiet kitchen — a kettle warming on a small blue ring, the
old copper pot hissing softly, laundry hanging still outside the window,
and dust motes drifting down through the slant of late sun onto the
wooden sill. Nothing else needs to happen right now.

## How it works

`main.py` (Python 3.13, standard library only) holds the 731-character
scene as a fixed constant and writes it, deterministically, to
`entry.txt` in the output directory. It runs the same way every time:
no sampling, no randomness, no network.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=48pk93ya&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
