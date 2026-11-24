"""Absurd Micro-Startup Pitch-Off entry.

Writes one absurd micro-startup pitch (127 characters) to /output/entry.txt.
Standard library only.
"""

import os

PITCH = (
    "DreamBroker: we grade your dreams nightly and auction the five-star "
    "ones to people who can't dream. Sleep is now a side hustle."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print("wrote /output/entry.txt (%d characters)" % len(PITCH))


if __name__ == "__main__":
    main()
