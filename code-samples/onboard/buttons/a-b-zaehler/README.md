# a-b-zaehler

Bauteil: [Knoepfe A und B](../README.md) · Kategorie: onboard

Knopf **A** zaehlt hoch, Knopf **B** runter, **A+B** gemeinsam setzt auf 0.
Der Wert (0..9) steht auf der LED-Matrix.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Die Knoepfe A und B sitzen links und rechts
der LED-Matrix.

## Wie der Code funktioniert

- `button_a.is_pressed() and button_b.is_pressed()` wird **zuerst** geprueft -
  sonst wuerde ein Druck auf beide Knoepfe erst hoch-/runterzaehlen.
- `button_a.was_pressed()` liefert `True` genau einmal pro Druck (Flanke). Der
  micro:bit puffert das intern, darum verpasst die Schleife keinen Druck und
  es prellt nicht.
- `max(0, min(9, zaehler))` klemmt den Wert auf 0..9 fest.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: a-b-zaehler  (eingebaute Knoepfe A und B)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt einen Wert hoch, Knopf B zaehlt ihn runter,
#       beide zusammen setzen ihn auf 0 zurueck. Der Wert (0..9) steht
#       auf der LED-Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die Knoepfe A und B sind fest eingebaut
#   (links und rechts neben der LED-Matrix).
# --------------------------------------------------------------------------

from microbit import *

zaehler = 0
display.show(str(zaehler))

while True:
    # Beide Knoepfe gleichzeitig -> zuerst pruefen, sonst zaehlt es mit
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0

    # was_pressed(): reagiert einmal pro Druck (Flanke), kein Prellen
    elif button_a.was_pressed():
        zaehler = zaehler + 1

    elif button_b.was_pressed():
        zaehler = zaehler - 1

    # Auf den Bereich 0..9 begrenzen (eine Ziffer auf der Matrix)
    zaehler = max(0, min(9, zaehler))
    display.show(str(zaehler))

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: `0`
- A druecken -> `1`, `2`, ... bis `9` (dann stehen bleiben)
- B druecken -> wieder runter bis `0`
- A und B zusammen -> `0`

## Moegliche Erweiterungen

- `button_a.get_presses()` statt `was_pressed()` - zaehlt schnelle Mehrfachdruecke
- Bereich auf 0..99 erweitern und den Wert mit `display.scroll()` anzeigen
- langer Druck (mit `running_time()` messen) = Sprung um 10
