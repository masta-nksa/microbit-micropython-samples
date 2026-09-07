# bilder-und-text

Bauteil: [LED-Matrix 5x5](../README.md) · Kategorie: onboard

Knopf **A** spielt eine Bilderfolge, Knopf **B** scrollt einen Text.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig - die 5x5-Matrix ist die Vorderseite.

## Wie der Code funktioniert

- `display.show(bild)` zeigt ein einzelnes Bild oder Zeichen sofort an.
- Die `for`-Schleife geht die Liste `bilder` durch, jeweils mit `sleep(400)`
  dazwischen - so entsteht eine kleine Animation.
- `display.scroll("...")` schiebt Text von rechts nach links durch. Es
  **blockiert**, bis der Text fertig ist.
- `Image.HAPPY`, `Image.HEART`, ... sind fertige Bilder; die volle Liste
  steht in der micro:bit-Doku.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: bilder-und-text  (eingebaute LED-Matrix 5x5)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A spielt eine Bilderfolge ab, Knopf B laesst einen Text ueber
#       die Matrix scrollen. Zeigt die drei haeufigsten display-Befehle.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die 5x5-LED-Matrix ist die Vorderseite des micro:bit.
# --------------------------------------------------------------------------

from microbit import *

# Fertige Bilder aus dem Image-Katalog
bilder = [Image.HAPPY, Image.HEART, Image.DUCK, Image.GHOST, Image.ROCKET]

display.show(Image.ARROW_W)   # "druecke einen Knopf"

while True:
    if button_a.was_pressed():
        # Jedes Bild 400 ms zeigen
        for bild in bilder:
            display.show(bild)
            sleep(400)
        display.clear()

    if button_b.was_pressed():
        # scroll() schiebt den Text von rechts nach links durch
        display.scroll("Hallo NKSA")

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: Pfeil nach links
- A -> 5 Bilder nacheinander, dann Matrix aus
- B -> "Hallo NKSA" laeuft einmal durch

## Moegliche Erweiterungen

- eigenes Bild: `Image("09090:99999:99999:09990:00900")` (Herz)
- `display.scroll("...", loop=True, delay=80)` - endlos und schneller
- Bilderfolge mit `Image.ALL_CLOCKS` (fertige Uhr-Animation)
