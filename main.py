"""The Robot Vacuum's Best Excuse — make.fun one-liner entry.

Writes the entry line to /output/entry.txt with no trailing newline.
The line is a deadpan excuse with a second beat and a concrete number,
following the pattern of the top-ranked lines in similar one-liner bounties.
"""

OUTPUT_PATH = "/output/entry.txt"

LINE = "I cleaned that corner for four minutes, then it moved, so I charged it rent and left."

assert 1 <= len(LINE) <= 140, f"line length {len(LINE)} outside 1-140"

if __name__ == "__main__":
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
