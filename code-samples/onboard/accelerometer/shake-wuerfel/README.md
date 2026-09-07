# shake-wuerfel

Bauteil: [Beschleunigungssensor](../README.md) · Kategorie: onboard

Den micro:bit schuetteln -> eine Zufallszahl 1..6 erscheint auf der Matrix.
Ein Wuerfel ohne Wuerfel.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig.

## Wie der Code funktioniert

- `accelerometer.was_gesture("shake")` liefert `True`, wenn seit dem letzten
  Aufruf geschuettelt wurde. Der micro:bit erkennt das Schuetteln selbst -
  man muss die Beschleunigung nicht auswerten.
- `random.randint(1, 6)` gibt eine ganze Zufallszahl von 1 bis 6 (beide
  Grenzen inklusive). Dafuer `import random`.
- `print(...)` erscheint in der seriellen Ausgabe (im Editor **Open Serial**).

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: shake-wuerfel  (eingebauter Beschleunigungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den micro:bit schuetteln wie einen Wuerfelbecher. Nach dem Schuetteln
#       erscheint eine Zufallszahl 1..6 auf der LED-Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Beschleunigungssensor ist fest eingebaut.
#   Das Schuetteln erkennt der micro:bit selbst als fertige Geste "shake".
# --------------------------------------------------------------------------

from microbit import *
import random

display.show(Image.HAPPY)

while True:
    # was_gesture("shake"): True, wenn seit dem letzten Aufruf geschuettelt wurde
    if accelerometer.was_gesture("shake"):
        augen = random.randint(1, 6)   # ganze Zahl von 1 bis 6 (inklusive)
        display.show(str(augen))
        print("gewuerfelt:", augen)

    sleep(100)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: lachendes Gesicht
- Schuetteln -> eine Ziffer 1..6
- nochmal schuetteln -> neue Ziffer

## Moegliche Erweiterungen

- statt der Ziffer das passende Wuerfelbild mit `display.set_pixel()` zeichnen
- zwei Wuerfel: zwei Zahlen kurz nacheinander scrollen und die Summe zeigen
- kurzer Ton beim Wuerfeln (`music.pitch(...)`, nur V2)
