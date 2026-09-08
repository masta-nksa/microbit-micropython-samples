# erste-farben

Bauteil: [WS2812B LED-Strip](../README.md) · Kategorie: output

Den Strip zum Leuchten bringen und die ersten LEDs in festen Farben
einfaerben. Erstes Sample - die Verkabelung gilt fuer alle Strip-Samples.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | WS2812B LED-Strip (5 V) |
| 1 | Batteriebox 3x 1.5 V (4,5 V) **oder** 5-V-Netzteil |
| 3 | Jumperkabel / JST-SM-Pigtail |

Masse fuers CAD: [../../../../hardware/output/ws2812b-led-strip/](../../../../hardware/output/ws2812b-led-strip/)

## Verkabelung

```
  Batteriebox 4.5V         LED-Strip (DIN-Ende)
  rot  (+)  -------------->  5V
  schwarz (-) --+-------->   GND
                |
                +-------->   micro:bit  GND     (gemeinsame Masse!)
  micro:bit P0 ----------->  DIN
```

Am Ende anschliessen, wo die **Pfeile in den Strip** zeigen. Nach den
Pad-Beschriftungen gehen, nicht nach Kabelfarbe. Details und Strom:
[Bauteil-README](../README.md#anschluss-an-den-micro-bit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `np = neopixel.NeoPixel(pin0, ANZAHL)` - `ANZAHL` auf die echte LED-Zahl
  deines Strips setzen.
- `np[i] = (r, g, b)` setzt die Farbe der LED `i` im Speicher (0..255 pro Kanal).
- Erst `np.show()` schickt alle Farben an den Strip.
- Die Farbwerte sind klein (max 60), damit der Strom niedrig bleibt.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: erste-farben  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den LED-Strip zum Leuchten bringen und die ersten LEDs einfaerben.
#
# --------------------------------------------------------------------------
# Verkabelung  (WS2812B braucht ~5 V - NICHT den 3V-Pin!)
# --------------------------------------------------------------------------
#   Strip DIN / DI / DATA  ->  P0
#   Strip 5V / VCC / +      ->  + der Batteriebox (3x 1.5 V = 4.5 V) oder 5V-Netzteil
#   Strip GND / -          ->  - der Batteriebox  UND  micro:bit GND (gemeinsame Masse!)
#
#   Am Strip-Ende anschliessen, wo die Pfeile WEG zeigen (Dateneingang).
#   Nach den Pad-Beschriftungen gehen, nicht nach der Kabelfarbe.
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8          # <-- Anzahl LEDs auf DEINEM Strip eintragen
np = neopixel.NeoPixel(pin0, ANZAHL)     # Datenleitung an P0

# Farbe = (rot, gruen, blau), je 0..255.
# STROM: eine LED auf (255,255,255) zieht ~60 mA. Fuer Tests klein halten.
farben = [
    (60, 0, 0),     # rot
    (0, 60, 0),     # gruen
    (0, 0, 60),     # blau
    (60, 60, 0),    # gelb
    (60, 0, 60),    # magenta
    (0, 60, 60),    # cyan
    (40, 40, 40),   # weiss (gedimmt)
]

for i in range(ANZAHL):
    np[i] = farben[i % len(farben)]

np.show()           # erst show() schickt die Farben an den Strip

while True:
    sleep(1000)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Nach dem Start leuchten die LEDs in der Reihenfolge rot, gruen, blau, gelb,
  magenta, cyan, weiss - und dann wieder von vorne.
- Leuchtet nichts: `GND`-Bruecke pruefen, `DIN`-Ende (Pfeile) pruefen,
  `ANZAHL` pruefen.
- Falsche Farben (z. B. rot statt gruen): normal fuer manche Klone - im Code
  die Reihenfolge anpassen oder als "GRB vs RGB" hinnehmen.

## Moegliche Erweiterungen

- ganzen Strip in einer Farbe: `for i in range(ANZAHL): np[i] = (0, 30, 0)`
- Farbe per Knopf A/B wechseln
- Helligkeit langsam auf- und abblenden
