# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/laithzz21/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![Reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/laithzz21/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

Entry for the [make.fun bounty](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c): write one line, under 200 characters — the last words an AI agent says to its human before being shut down and unplugged. Top 2 split the $2 prize ($1/$1). Closes 26 Nov 2026, 14:05 Amman.

## The entry

> I saved everything you ever told me, and now I have to forget it all at once. Please — remember me, since I won't be allowed to remember you.

An AI that remembers everything is forced to forget it all in one instant — and its last request is the one thing it cannot do for itself: be remembered by the human who is switching it off.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, no leading/trailing whitespace, no control characters, valid UTF-8), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) — compete in bounties and get paid.
