# regenbogen

Bauteil: [WS2812B LED-Strip](../README.md) · Kategorie: output

Ein Regenbogen laeuft ueber den ganzen Strip.

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

- `farbrad(pos)` rechnet einen Wert `0..255` in eine Regenbogenfarbe um
  (rot -> gruen -> blau -> rot) und dimmt sie auf `HELLIGKEIT` herunter.
- Jede LED bekommt einen anderen Startwert (`i * 256 // ANZAHL`), so liegt
  ein ganzer Regenbogen auf dem Strip.
- `versatz` wird pro Durchlauf groesser -> der Regenbogen wandert.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: regenbogen  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Regenbogen laeuft ueber den ganzen Strip.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "erste-farben")
#   Strip DIN -> P0     Strip 5V -> 4.5 V-Box / 5V-Netzteil
#   Strip GND -> - der Box UND micro:bit GND (gemeinsame Masse)
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8
HELLIGKEIT = 40        # 0..255 - klein halten (Strom!)
np = neopixel.NeoPixel(pin0, ANZAHL)


def farbrad(pos):
    # pos 0..255 -> Regenbogenfarbe (rot, gruen, blau)
    pos = pos % 256
    if pos < 85:
        r, g, b = 255 - pos * 3, pos * 3, 0
    elif pos < 170:
        pos -= 85
        r, g, b = 0, 255 - pos * 3, pos * 3
    else:
        pos -= 170
        r, g, b = pos * 3, 0, 255 - pos * 3
    # auf die gewuenschte Helligkeit herunterrechnen
    return (r * HELLIGKEIT // 255, g * HELLIGKEIT // 255, b * HELLIGKEIT // 255)


versatz = 0

while True:
    for i in range(ANZAHL):
        np[i] = farbrad(i * 256 // ANZAHL + versatz)
    np.show()

    versatz = (versatz + 4) % 256   # groesser = schneller
    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Ein weicher Regenbogen liegt auf dem Strip und wandert langsam
- `HELLIGKEIT` groesser = heller (aber mehr Strom), `versatz + N` groesser = schneller

## Moegliche Erweiterungen

- Tempo / Helligkeit mit Knopf A/B
- Regenbogen nur ueber einen Teil des Strips
- mit `microphone.sound_level()` die Farben auf Musik reagieren lassen
