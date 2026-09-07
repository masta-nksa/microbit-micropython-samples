# temperatur-anzeigen

Bauteil: [Temperatursensor](../README.md) · Kategorie: onboard

Knopf **A** -> die aktuelle Temperatur laeuft als Text ueber die Matrix.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Der Sensor sitzt im Prozessor - der Wert
liegt meist ein paar Grad ueber der Raumtemperatur und reagiert traege.

## Wie der Code funktioniert

- `temperature()` gibt die Temperatur in Grad Celsius als ganze Zahl zurueck.
- `str(grad) + "C"` macht daraus Text, den `display.scroll()` durchlaufen laesst.
  `scroll()` blockiert, bis der Text fertig ist - danach laeuft die Schleife weiter.
- `button_b` zeigt nur kurz `Image.YES` - Platz fuer eine eigene Idee.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: temperatur-anzeigen  (eingebauter Temperatursensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A druecken -> die aktuelle Temperatur laeuft als Text ueber
#       die LED-Matrix. Knopf B -> ein Thermometer-Bild als Erinnerung,
#       dass es der Chip-Wert ist (leicht zu hoch).
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Sensor sitzt im Prozessor des micro:bit.
#   Achtung: er misst die Chip-Temperatur, meist ein paar Grad ueber der
#   Raumtemperatur, und reagiert langsam.
# --------------------------------------------------------------------------

from microbit import *

while True:
    if button_a.was_pressed():
        grad = temperature()          # Grad Celsius als ganze Zahl
        display.scroll(str(grad) + "C")
        print("Temperatur:", grad, "C")

    if button_b.was_pressed():
        display.show(Image.YES)       # nur als kurze Rueckmeldung
        sleep(500)
        display.clear()

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- A druecken -> z. B. `24C` laeuft durch
- Hand um den micro:bit legen, kurz warten, wieder A -> Wert steigt langsam

## Moegliche Erweiterungen

- ohne Knopf: alle 5 Sekunden automatisch messen und anzeigen
- Warnung (Herz / Ton), wenn die Temperatur ueber einen Grenzwert steigt
- Min- und Max-Wert merken und mit B anzeigen
