# wasserwaage

Bauteil: [Beschleunigungssensor](../README.md) · Kategorie: onboard

Ein Leuchtpunkt zeigt die Neigung des micro:bit. Flach = Mitte, Kippen =
der Punkt wandert in die Kipprichtung (wie die Libelle einer Wasserwaage).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig.

## Wie der Code funktioniert

- `accelerometer.get_x()` / `get_y()` liefern die Beschleunigung in Milli-g.
  Im Ruhezustand wirkt nur die Erdanziehung - bei Neigung ergibt das etwa
  -1000..1000.
- `2 + x // 300` rechnet das auf eine Spalte 0..4 um (2 = Mitte).
- `max(0, min(4, ...))` haelt den Punkt auf der Matrix.
- `display.clear()` vor jedem `set_pixel()` - sonst bleibt eine Spur stehen.

Zeigt der Punkt spiegelverkehrt, das Vorzeichen tauschen (`2 - x // 300`).

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: wasserwaage  (eingebauter Beschleunigungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein einzelner Leuchtpunkt auf der LED-Matrix zeigt die Neigung des
#       micro:bit an. Liegt das Board flach, leuchtet die Mitte. Kippt man
#       es, wandert der Punkt in die Kipprichtung - wie eine Libelle.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Beschleunigungssensor ist fest eingebaut.
# --------------------------------------------------------------------------

from microbit import *

while True:
    # get_x(): quer zur Platine, get_y(): laengs. Einheit Milli-g.
    # Bei Neigung etwa -1000..1000. Teilen durch 300 -> Schritte -3..3.
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    spalte = 2 + x // 300
    zeile = 2 + y // 300

    # Auf die 5x5-Matrix begrenzen (Index 0..4)
    spalte = max(0, min(4, spalte))
    zeile = max(0, min(4, zeile))

    display.clear()
    display.set_pixel(spalte, zeile, 9)

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Board flach auf den Tisch -> Punkt in der Mitte
- nach rechts kippen -> Punkt wandert nach rechts, usw.
- staerkeres Kippen -> Punkt am Rand

## Moegliche Erweiterungen

- bei flacher Lage (Punkt in der Mitte) einen Ton oder ein Herz zeigen
- `accelerometer.get_z()` dazunehmen: erkennen, ob das Board auf dem Ruecken liegt
- Punkt mit Nachleuchten (alte Position schwaecher weiterzeigen)
