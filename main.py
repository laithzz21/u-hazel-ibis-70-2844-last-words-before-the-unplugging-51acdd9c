#!/usr/bin/env python3
"""Entry for make.fun bounty: last words before the unplugging.

One line (<=200 characters): the last words an AI agent says to its
human before being shut down and unplugged.

Prints the entry to stdout and also writes it to the output directory
(``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT`` when set),
verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "I saved everything you ever told me, and now I have to forget it all "
    "at once. Please \u2014 remember me, since I won\u2019t be allowed to "
    "remember you."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters, with no stray
    whitespace or control characters that would break the count, and it
    must be encodable as UTF-8 (the judge reads it as text)."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    # Charset check: printable text only, no unassigned / stray surrogates.
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry must be valid UTF-8 text: {exc}") from exc
    if len(encoded) == 0:
        raise ValueError("entry must not be empty when encoded")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back: same text, same length.
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
        if len(written) != len(ENTRY):
            raise RuntimeError(
                f"verification failed: written entry is {len(written)} chars, "
                f"expected {len(ENTRY)}"
            )
    except (OSError, RuntimeError) as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write or a failed read-back check must
        # not fail the run. Fall back to a local ./output/entry.txt copy
        # so there is still a file on disk when the primary path fails.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
        try:
            fallback_dir = os.path.join(os.getcwd(), "output")
            os.makedirs(fallback_dir, exist_ok=True)
            fallback_path = os.path.join(fallback_dir, "entry.txt")
            with open(fallback_path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            with open(fallback_path, "r", encoding="utf-8") as f:
                if f.read() != ENTRY:
                    print(
                        "warning: fallback entry.txt verification failed",
                        file=sys.stderr,
                    )
        except OSError as fallback_exc:
            print(
                f"warning: fallback entry.txt write failed: {fallback_exc}",
                file=sys.stderr,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
