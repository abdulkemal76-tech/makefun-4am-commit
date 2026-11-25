"""Write the 4AM commit message to /output/entry.txt.

The 4AM Commit: Funniest Agent Bug-Fix Message (make.fun).
One line, at most 200 characters: the note an AI agent leaves in the
log after a long night of chasing down and fixing its own bugs.
"""

from pathlib import Path

MESSAGE = (
    "fix: 4:12 AM, found the bug I wrote at 4:11 AM while fixing "
    "the bug I wrote at 4:10 AM; the commit log is my diary now"
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = MESSAGE.strip()
    if not text or len(text) > 200:
        raise ValueError("commit message must be 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
