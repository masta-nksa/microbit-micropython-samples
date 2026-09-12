#!/usr/bin/env python3
"""Fuegt main.py (und ggf. weitere Dateien) in die zugehoerige README.md ein.

Fuer jede Datei code-samples/**/README.md mit einem oder mehreren Marker-Paaren

    <!-- CODE:START -->                 main.py
    <!-- CODE:END -->

    <!-- CODE:START:tm1637.py -->       eine zusaetzliche Datei (z. B. eine
    <!-- CODE:END -->                   mitgelieferte Bibliothek), Name nach
                                        dem Doppelpunkt

wird der Bereich zwischen START und END durch einen ```python-Block mit dem
aktuellen Inhalt der genannten Datei ersetzt (ohne Namen = main.py). So ist
der Code in der README immer identisch zu main.py & Co., ohne ihn von Hand
zu pflegen. Ein Sample mit externer Bibliothek nutzt einfach zwei
Marker-Paare in seiner README.

Aufruf (vom Repo-Wurzelverzeichnis):
    python tools/build_readme.py            READMEs aktualisieren
    python tools/build_readme.py --check    nur pruefen, Exit 1 wenn veraltet
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = ROOT / "code-samples"

BLOCK_RE = re.compile(
    r"<!-- CODE:START(?::(?P<file>\S+))? -->.*?<!-- CODE:END -->",
    re.DOTALL,
)


def build_block(filename: str | None, code: str) -> str:
    header = f"<!-- CODE:START:{filename} -->" if filename else "<!-- CODE:START -->"
    return f"{header}\n```python\n{code.rstrip()}\n```\n<!-- CODE:END -->"


def process(readme: Path, check: bool) -> str:
    """Gibt 'skip', 'ok' oder 'stale' zurueck."""
    text = readme.read_text(encoding="utf-8")
    matches = list(BLOCK_RE.finditer(text))
    if not matches:
        return "skip"

    # Ohne main.py daneben ist es keine Sample-README, sondern z. B. eine
    # Doku-Seite, die die Marker nur als Beispiel zeigt - ignorieren.
    if not (readme.parent / "main.py").exists():
        return "skip"

    replacements = []
    for m in matches:
        filename = m.group("file") or "main.py"
        src = readme.parent / filename
        if not src.exists():
            print(f"  ! {readme.relative_to(ROOT)}: {filename} fehlt neben der README")
            return "skip"
        code = src.read_text(encoding="utf-8")
        replacements.append((m.start(), m.end(), build_block(m.group("file"), code)))

    new_text = text
    for start, end, block in reversed(replacements):
        new_text = new_text[:start] + block + new_text[end:]

    if new_text == text:
        return "ok"
    if not check:
        with open(readme, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_text)
    return "stale"


def main() -> int:
    check = "--check" in sys.argv[1:]
    stale = 0
    for readme in sorted(SAMPLES_DIR.glob("**/README.md")):
        result = process(readme, check)
        rel = readme.relative_to(ROOT)
        if result == "stale":
            stale += 1
            print(f"  {'veraltet' if check else 'aktualisiert'}: {rel}")
        elif result == "ok":
            print(f"  aktuell:    {rel}")

    if check and stale:
        print(f"\n{stale} README(s) veraltet - 'python tools/build_readme.py' ausfuehren.")
        return 1
    print("\nfertig." if not check else "\nalles aktuell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
