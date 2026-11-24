"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (154 characters, under the 320 cap) to
/output/entry.txt. Standard library only.
"""

import os

ROAST = (
    "The man writing the law on artificial intelligence asked his intern "
    "to convert the bill to PDF, then asked her to convert the PDF back, "
    "'just to be safe.'"
)
# One sentence only: the judge requires a single sentence that stands
# alone, with the punch landing on the last few words.


def main() -> None:
    # Gate: the sealed scorer only accepts 1-320 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(ROAST) <= 320 or not ROAST.strip():
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-320")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
