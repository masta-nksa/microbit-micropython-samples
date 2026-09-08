# lauflicht

Bauteil: [WS2812B LED-Strip](../README.md) · Kategorie: output

Ein Leuchtpunkt wandert den Strip entlang und faengt vorne wieder an.
Knopf **A** macht ihn schneller, Knopf **B** langsamer.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | WS2812B LED-Strip (5 V) |
| 1 | Batteriebox 3x 1.5 V (4,5 V) oder 5-V-Netzteil |
| 3 | Jumperkabel / JST-SM-Pigtail |

Masse fuers CAD: [../../../../hardware/output/ws2812b-led-strip/](../../../../hardware/output/ws2812b-led-strip/)

## Verkabelung

Identisch zu [erste-farben](../erste-farben/README.md#verkabelung):

```
   P0 -> DIN      + der 4.5V-Box -> 5V      - der Box -> GND + micro:bit GND
```

Details: [Bauteil-README](../README.md#anschluss-an-den-micro-bit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `np.clear()` schaltet erst alle LEDs aus, dann wird nur `np[pos]` gesetzt.
- `pos = (pos + 1) % ANZAHL` schiebt den Punkt weiter und springt am Ende
  zurueck auf 0.
- `pause` (ms) bestimmt das Tempo; Knopf A/B veraendern es in 30-ms-Schritten.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: lauflicht  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Leuchtpunkt wandert den Strip entlang und faengt vorne wieder an.
#       Knopf A / B machen ihn schneller / langsamer.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "erste-farben")
#   Strip DIN -> P0     Strip 5V -> 4.5 V-Box / 5V-Netzteil
#   Strip GND -> - der Box UND micro:bit GND (gemeinsame Masse)
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8
np = neopixel.NeoPixel(pin0, ANZAHL)

FARBE = (0, 40, 60)     # Farbe des Punkts
pause = 120             # ms pro Schritt (kleiner = schneller)

pos = 0

while True:
    np.clear()          # alle LEDs aus
    np[pos] = FARBE
    np.show()

    pos = (pos + 1) % ANZAHL   # weiter, am Ende zurueck auf 0

    if button_a.was_pressed():
        pause = max(20, pause - 30)
    if button_b.was_pressed():
        pause = min(500, pause + 30)

    sleep(pause)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Ein Punkt laeuft wiederholt von der ersten zur letzten LED
- Knopf A -> schneller, Knopf B -> langsamer

## Moegliche Erweiterungen

- Schweif: die letzten 2-3 LEDs schwaecher nachleuchten lassen
- am Ende umkehren statt springen (hin und her)
- Farbe des Punkts mit dem Beschleunigungssensor aendern
