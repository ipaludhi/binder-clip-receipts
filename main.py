"""Office Artifacts: The One-Line Placard Contest — one-line entry (program/v1, python3.13).

Writes the placard to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
The entry is a fixed original line; the program is deterministic.
"""
import os

ENTRY = "Binder Clip, c. 1300 BCE. Iron jaw that held the empire's receipts together; released only at the coronation. On loan from Accounts."


def main():
    # Gate self-check (revision edit): sealed gate wants 1-180 chars, non-blank,
    # one line. The placard must read as a single museum label — no trailing
    # newline, no second sentence hiding after a line break.
    assert 1 <= len(ENTRY) <= 180 and ENTRY.strip() and "\n" not in ENTRY, "entry fails the 1-180 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
