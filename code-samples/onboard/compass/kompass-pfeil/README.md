# kompass-pfeil

Bauteil: [Kompass / Magnetometer](../README.md) · Kategorie: onboard

Ein Pfeil auf der Matrix zeigt immer nach Norden - egal, wie man den
micro:bit dreht.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig. **Vor der ersten Messung kalibrieren:** beim
Start erscheint ein Punkt - den micro:bit langsam in alle Richtungen kippen,
bis der ganze Rand leuchtet. Abseits von Metall, Magneten, Lautsprechern
und Netzteilen arbeiten.

## Wie der Code funktioniert

- `compass.is_calibrated()` / `compass.calibrate()`: kalibriert wird nur beim
  ersten Mal. `calibrate()` blockiert, bis das Spiel fertig ist.
- `compass.heading()` liefert 0..359 Grad (0 = Norden), gemessen an der
  Blickrichtung der Oberkante.
- `Image.ALL_ARROWS` ist eine Liste mit 8 Pfeilbildern in der Reihenfolge
  N, NO, O, SO, S, SW, W, NW.
- `(360 - richtung + 22.5) // 45 % 8` waehlt daraus den Pfeil, der - vom
  gedrehten Board aus gesehen - nach Norden zeigt. Das `+ 22.5` rundet auf
  das naechste Achtel.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: kompass-pfeil  (eingebauter Kompass / Magnetometer)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Pfeil auf der LED-Matrix zeigt immer nach Norden, egal wie man
#       den micro:bit dreht.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Magnetsensor ist eingebaut.
#   Vor der ersten Messung MUSS kalibriert werden (siehe unten).
#   Abseits von Metall, Magneten und Netzteilen halten.
# --------------------------------------------------------------------------

from microbit import *

# Kalibrier-Spiel: den micro:bit kippen, bis der Rand voll ist.
# Laeuft nur, wenn noch nicht kalibriert.
if not compass.is_calibrated():
    compass.calibrate()

# Image.ALL_ARROWS: 0=N, 1=NO, 2=O, 3=SO, 4=S, 5=SW, 6=W, 7=NW
pfeile = Image.ALL_ARROWS

while True:
    richtung = compass.heading()   # 0..359 Grad, 0 = Norden

    # Norden relativ zur Blickrichtung des Boards -> passender Pfeil.
    # + 22.5 rundet auf das naechste der 8 Achtel.
    index = int((360 - richtung + 22.5) // 45) % 8
    display.show(pfeile[index])

    sleep(200)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Kalibrieren durchspielen -> kurz ein Smiley
- danach: der Pfeil zeigt beim Drehen des Boards stabil in eine Richtung
  (nach Norden)

## Moegliche Erweiterungen

- statt Pfeil die Gradzahl mit `display.scroll()` anzeigen
- "Schnitzeljagd": Pfeil wird zum Herz, wenn eine Zielrichtung getroffen ist
- `compass.get_field_strength()` nutzen, um Metall in der Naehe zu finden
