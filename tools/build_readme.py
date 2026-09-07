#!/usr/bin/env python3
"""Fuegt den Inhalt jeder main.py in die zugehoerige README.md ein.

Fuer jede Datei code-samples/**/README.md, die die beiden Marker

    <!-- CODE:START -->
    <!-- CODE:END -->

enthaelt, wird der Bereich dazwischen durch einen ```python-Block mit dem
aktuellen Inhalt der daneben liegenden main.py ersetzt. So ist der Code in
der README immer identisch zu main.py, ohne ihn von Hand zu pflegen.

Aufruf (vom Repo-Wurzelverzeichnis):
    python tools/build_readme.py            READMEs aktualisieren
    python tools/build_readme.py --check    nur pruefen, Exit 1 wenn veraltet
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = ROOT / "code-samples"
START = "<!-- CODE:START -->"
END = "<!-- CODE:END -->"


def build_block(code: str) -> str:
    return f"{START}\n```python\n{code.rstrip()}\n```\n{END}"


def process(readme: Path, check: bool) -> str:
    """Gibt 'skip', 'ok' oder 'stale' zurueck."""
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return "skip"

    main_py = readme.parent / "main.py"
    if not main_py.exists():
        # z. B. eine Doku-Seite, die die Marker nur als Beispiel zeigt - ignorieren
        return "skip"

    code = main_py.read_text(encoding="utf-8")
    new_text = text.split(START)[0] + build_block(code) + text.split(END, 1)[1]

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
