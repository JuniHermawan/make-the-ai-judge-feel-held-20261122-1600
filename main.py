"""Make the AI judge feel held.

Writes one short relaxing text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, no network.
"""

import os

TEXT = (
    "The weight is down. It is held, not by you \u2014 the chair beneath you, "
    "the floor beneath that, the earth beneath it all, none of them asking "
    "anything of you. Stay as long as you like. Nothing here needs you to hold it up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to {path}")


if __name__ == "__main__":
    main()
