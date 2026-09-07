# nachtlicht

Bauteil: [Umgebungslicht](../README.md) · Kategorie: onboard

Wird es dunkel, leuchtet die ganze Matrix auf. Wird es hell, geht sie aus.
Ein automatisches Nachtlicht.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Zum Testen den micro:bit mit der Hand abdecken.

## Wie der Code funktioniert

- `display.read_light_level()` misst mit den Matrix-LEDs die Umgebungshelligkeit
  (0..255, 0 = dunkel) und unterbricht dafuer die Anzeige ganz kurz.
- Ein fester Schwellwert `GRENZE` trennt "hell" von "dunkel". Passenden Wert
  ueber die serielle Ausgabe (`print`) ablesen und anpassen.
- `Image("99999:...")` ist ein selbst gebautes Bild: 5 Zeilen mit je 5
  Helligkeitswerten, hier alle auf 9.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: nachtlicht  (LED-Matrix als Lichtsensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein automatisches Nachtlicht. Wird es im Raum dunkel, leuchtet die
#       ganze Matrix hell auf. Wird es wieder hell, geht sie aus.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - gemessen wird mit den LEDs der Matrix selbst.
#   Zum Testen den micro:bit mit der Hand abdecken.
# --------------------------------------------------------------------------

from microbit import *

GRENZE = 50   # darunter gilt es als "dunkel" (0..255)

while True:
    licht = display.read_light_level()

    if licht < GRENZE:
        display.show(Image("99999:99999:99999:99999:99999"))   # alles an
    else:
        display.clear()

    print("Licht:", licht)
    sleep(200)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- heller Raum -> Matrix aus
- micro:bit abdecken / Licht ausschalten -> Matrix leuchtet voll auf
- wieder aufdecken -> Matrix aus

## Moegliche Erweiterungen

- Helligkeit der Matrix stufenlos an den Lichtwert koppeln (je dunkler, desto heller)
- Grenze mit den Knoepfen A/B zur Laufzeit einstellen
- bei Dunkelheit zusaetzlich einen leisen Ton (nur V2)
