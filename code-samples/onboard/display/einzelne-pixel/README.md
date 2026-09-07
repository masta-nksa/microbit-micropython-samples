# einzelne-pixel

Bauteil: [LED-Matrix 5x5](../README.md) · Kategorie: onboard

Einen Leuchtpunkt mit den Knoepfen bewegen: **A** nach rechts, **B** nach
unten, am Rand geht es auf der anderen Seite weiter.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig.

## Wie der Code funktioniert

- `display.set_pixel(x, y, h)` setzt **einen** Pixel: `x` = Spalte 0..4,
  `y` = Zeile 0..4, `h` = Helligkeit 0..9.
- `(x + 1) % 5` zaehlt 0,1,2,3,4,0,1,... - der Rest der Division durch 5
  laesst den Punkt am Rand umspringen.
- `display.clear()` vor jedem `set_pixel()`, sonst bleiben alte Punkte an.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: einzelne-pixel  (eingebaute LED-Matrix 5x5)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Einen einzelnen Leuchtpunkt mit den Knoepfen ueber die Matrix
#       bewegen. A schiebt nach rechts, B nach unten - am Rand geht es
#       auf der anderen Seite weiter.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die 5x5-LED-Matrix ist eingebaut.
#   Koordinaten: x = Spalte 0..4 (links->rechts), y = Zeile 0..4 (oben->unten).
# --------------------------------------------------------------------------

from microbit import *

x = 2
y = 2

while True:
    if button_a.was_pressed():
        x = (x + 1) % 5      # 4 -> 0 (Sprung an den linken Rand)

    if button_b.was_pressed():
        y = (y + 1) % 5      # 4 -> 0 (Sprung an den oberen Rand)

    display.clear()
    display.set_pixel(x, y, 9)   # Helligkeit 9 = maximal

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: Punkt in der Mitte (2,2)
- A -> Punkt wandert nach rechts, nach dem rechten Rand links weiter
- B -> Punkt wandert nach unten, nach unten oben weiter

## Moegliche Erweiterungen

- Bewegung ueber den Beschleunigungssensor statt der Knoepfe steuern
- gesetzte Pixel stehen lassen (nicht `clear()`) -> Zeichenbrett
- zweiter Punkt als "Ziel", Treffer -> Herz + Ton
