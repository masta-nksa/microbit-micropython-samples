# farbflaechen

Bauteil: [1.8" TFT SPI Display (ST7735)](../README.md) · Kategorie: output

Grundfunktion: Display initialisieren, den ganzen Bildschirm nacheinander in
ein paar Farben fuellen, dann drei Rechtecke zeichnen. Nutzt die eigene
Portierung [st7735.py](../README.md#bibliothek-eigene-portierung-st7735py)
als zweite Projektdatei - wird in [zahlen-zaehler](../zahlen-zaehler/)
wiederverwendet.

> **Status: noch nicht auf echter Hardware getestet.** Erstes Sample zum
> Ausprobieren - siehe [Erwartetes Verhalten](#erwartetes-verhalten).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | 1.8" TFT SPI Display (ST7735) |
| 7 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/output/st7735-tft-1-8-spi/](../../../../hardware/output/st7735-tft-1-8-spi/)

## Verkabelung

```
   micro:bit          ST7735-Modul
  +---------+        +------------+
  |     13  |--------| SCK        |
  |     15  |--------| SDA / MOSI |
  |     12  |--------| A0 / DC    |
  |     16  |--------| RESET      |
  |      8  |--------| CS         |
  |      3V |--------| LED        |
  |      3V |--------| VCC        |
  |     GND |--------| GND        |
  +---------+        +------------+
```

`SCK`/`SDA` sind die festen Hardware-SPI-Pins des micro:bit, der Rest frei
waehlbar. Details: [Bauteil-README](../README.md#anschluss-an-den-microbit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Bibliothek: st7735.py

Zweite Datei im Projekt - eigene Portierung der Init-Sequenz und
Pixel-Logik aus
[adafruit/micropython-adafruit-rgb-display](https://github.com/adafruit/micropython-adafruit-rgb-display)
(MIT-Lizenz, Radomir Dopieralski) auf `microbit.spi` + `write_digital()`.
Details und Warum-kein-Framebuffer: [Bauteil-README](../README.md#bibliothek-eigene-portierung-st7735py).
Wie man eine zweite Datei im Online-Editor anlegt:
[docs/setup.md](../../../../docs/setup.md#zweite-datei-hinzufuegen-z-b-eine-mitgelieferte-bibliothek).

<!-- CODE:START:st7735.py -->
```python
"""
Minimaler MicroPython-Treiber fuer 1.8" ST7735(R)-SPI-Displays (128x160,
"red tab") auf dem BBC micro:bit.

Portiert auf das microbit-Modul (Hardware-SPI + write_digital-Pins statt
machine.SPI/machine.Pin) auf Basis von Radomir Dopieralskis
micropython-adafruit-rgb-display (rgb.py + st7735.py):
https://github.com/adafruit/micropython-adafruit-rgb-display

Bewusst ohne Framebuffer: der micro:bit hat zu wenig RAM fuer ein volles
128x160-Bild (2 Byte/Pixel = 40960 Byte). fill_rect() schreibt die Pixel
stattdessen in Bloecken direkt per SPI.

MIT License
Copyright (c) 2016 Radomir Dopieralski
Copyright (c) 2026 Portierung fuer micro:bit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from microbit import spi, sleep

_SWRESET = 0x01
_SLPOUT = 0x11
_INVOFF = 0x20
_DISPON = 0x29
_CASET = 0x2A
_RASET = 0x2B
_RAMWR = 0x2C
_MADCTL = 0x36
_COLMOD = 0x3A
_FRMCTR1 = 0xB1
_FRMCTR2 = 0xB2
_FRMCTR3 = 0xB3
_INVCTR = 0xB4
_PWCTR1 = 0xC0
_PWCTR2 = 0xC1
_PWCTR3 = 0xC2
_PWCTR4 = 0xC3
_PWCTR5 = 0xC4
_VMCTR1 = 0xC5
_GMCTRP1 = 0xE0
_GMCTRN1 = 0xE1

_INIT = (
    (_SWRESET, None),
    (_SLPOUT, None),
    (_MADCTL, b'\xC8'),
    (_COLMOD, b'\x05'),
    (_INVCTR, b'\x07'),
    (_FRMCTR1, b'\x01\x2c\x2d'),
    (_FRMCTR2, b'\x01\x2c\x2d'),
    (_FRMCTR3, b'\x01\x2c\x2d\x01\x2c\x2d'),
    (_PWCTR1, b'\x02\x02\x84'),
    (_PWCTR2, b'\xc5'),
    (_PWCTR3, b'\x0a\x00'),
    (_PWCTR4, b'\x8a\x2a'),
    (_PWCTR5, b'\x8a\xee'),
    (_VMCTR1, b'\x0e'),
    (_INVOFF, None),
    (_GMCTRP1, b'\x02\x1c\x07\x12\x37\x32\x29\x2d\x29\x25\x2b\x39\x00\x01\x03\x10'),
    (_GMCTRN1, b'\x03\x1d\x07\x06\x2e\x2c\x29\x2d\x2e\x2e\x37\x3f\x00\x00\x02\x10'),
)


def color565(r, g, b):
    return (r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3


BLACK = 0x0000
WHITE = 0xFFFF
RED = color565(255, 0, 0)
GREEN = color565(0, 255, 0)
BLUE = color565(0, 0, 255)
YELLOW = color565(255, 255, 0)
CYAN = color565(0, 255, 255)
MAGENTA = color565(255, 0, 255)


class ST7735:
    def __init__(self, cs, dc, rst, width=128, height=160, baudrate=4000000):
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.width = width
        self.height = height
        self.cs.write_digital(1)
        self.dc.write_digital(0)
        self.rst.write_digital(1)
        spi.init(baudrate=baudrate, bits=8, mode=0)
        self._reset()
        for command, data in _INIT:
            self._write(command, data)
        self._write(_DISPON, None)

    def _reset(self):
        self.rst.write_digital(0)
        sleep(50)
        self.rst.write_digital(1)
        sleep(50)

    def _write(self, command=None, data=None):
        if command is not None:
            self.dc.write_digital(0)
            self.cs.write_digital(0)
            spi.write(bytes([command]))
            self.cs.write_digital(1)
        if data is not None:
            self.dc.write_digital(1)
            self.cs.write_digital(0)
            spi.write(data)
            self.cs.write_digital(1)

    def _set_window(self, x0, y0, x1, y1):
        self._write(_CASET, bytes([0, x0, 0, x1]))
        self._write(_RASET, bytes([0, y0, 0, y1]))

    def fill_rect(self, x, y, w, h, color):
        # Nur das angegebene Rechteck wird neu gezeichnet - fuer ein
        # bewegtes Element (Zahl, Balken, ...) immer NUR dessen eigenes
        # Rechteck neu fuellen statt jedes Mal fill() auf dem ganzen
        # Bildschirm. Das ist bei 128x160 Pixeln der Unterschied zwischen
        # ein paar hundert und 20480 uebertragenen Pixeln pro Update.
        x = max(0, min(self.width - 1, x))
        y = max(0, min(self.height - 1, y))
        w = max(1, min(self.width - x, w))
        h = max(1, min(self.height - y, h))
        self._set_window(x, y, x + w - 1, y + h - 1)
        self._write(_RAMWR, None)

        hi, lo = (color >> 8) & 0xFF, color & 0xFF
        pixel = bytes([hi, lo])
        n = w * h
        block = pixel * min(n, 512)

        self.dc.write_digital(1)
        self.cs.write_digital(0)
        while n > 0:
            count = min(n, 512)
            spi.write(block if count == 512 else pixel * count)
            n -= count
        self.cs.write_digital(1)

    def fill(self, color):
        self.fill_rect(0, 0, self.width, self.height, color)

    def pixel(self, x, y, color):
        self.fill_rect(x, y, 1, 1, color)
```
<!-- CODE:END -->

## Wie der Code funktioniert

- `ST7735(cs=pin8, dc=pin12, rst=pin16)` erstellt das Display-Objekt und
  fuehrt die Init-Sequenz aus (Standard: 128x160 Pixel, 4 MHz SPI).
- `display.fill(farbe)` faerbt den **ganzen** Bildschirm ein - fuer ein
  einmaliges Umschalten ok, siehe [Performance-Hinweis](../README.md#performance-nicht-bei-jedem-update-alles-neu-zeichnen).
- `display.fill_rect(x, y, breite, hoehe, farbe)` faerbt nur ein Rechteck -
  das Werkzeug fuer alles, was sich spaeter aendern soll.
- `color565(r, g, b)` baut aus drei 0-255-Werten eine eigene Farbe.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: farbflaechen  (1.8" TFT SPI Display, ST7735)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Grundfunktion pruefen - Display initialisieren, ganzen Bildschirm
#       nacheinander in ein paar Farben fuellen, dann drei Rechtecke.
#       Nutzt die Bibliothek st7735.py (2. Datei im Projekt) - siehe README.
#
#       fill() beschreibt hier bewusst den GANZEN Bildschirm (128x160 =
#       20480 Pixel) - fuer einen einmaligen Test ok, aber spuerbar
#       langsamer als ein kleines fill_rect(). Im naechsten Sample
#       (zahlen-zaehler) wird nur noch das veraenderte Rechteck neu
#       gezeichnet statt bei jedem Update der ganze Screen.
#
# --------------------------------------------------------------------------
# Verkabelung
#   Display SCK  -> P13 (Hardware-SPI, fix)   Display SDA/MOSI -> P15 (fix)
#   Display A0/DC -> P12                      Display RESET    -> P16
#   Display CS   -> P8                        Display LED      -> 3V
#   Display VCC  -> 3V (am eigenen Modul pruefen, manche wollen 5V)
#   Display GND  -> GND
# --------------------------------------------------------------------------

from microbit import pin8, pin12, pin16, sleep
from st7735 import ST7735, color565, BLACK, WHITE, RED, GREEN, BLUE

display = ST7735(cs=pin8, dc=pin12, rst=pin16)

# ----- Demo 1: ganzen Bildschirm der Reihe nach einfaerben -----
for farbe in (RED, GREEN, BLUE, WHITE, BLACK):
    display.fill(farbe)
    sleep(800)

# ----- Demo 2: ein paar Rechtecke, eigene Farbe per color565(r, g, b) -----
orange = color565(255, 140, 0)
display.fill_rect(10, 10, 40, 40, RED)
display.fill_rect(60, 10, 40, 40, GREEN)
display.fill_rect(10, 60, 90, 20, orange)

while True:
    sleep(1000)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

1. `st7735.py` als **zweite Datei** anlegen (siehe oben) und den
   Bibliotheks-Code hineinkopieren.
2. Inhalt von `main.py` in die Hauptdatei kopieren.
3. <https://python.microbit.org/v/beta> -> **Connect** -> **Send to micro:bit**.

Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Bildschirm faerbt sich nacheinander rot, gruen, blau, weiss, schwarz
  (je 0,8 Sekunden), danach bleiben ein rotes und ein gruenes Quadrat sowie
  ein oranger Balken stehen.
- Bildschirm bleibt weiss/leer: `RESET` und `CS` pruefen.
- Bildschirm zeigt Streifen/Datenmuell statt Farbflaechen: `A0`/`DC` und
  `SDA`/`SCK` nicht vertauscht? Manche Module brauchen eine andere
  `MADCTL`-Einstellung in `st7735.py` (Bildausrichtung/Spiegelung) -
  siehe Kommentar bei `_INIT`.
- Farben vertauscht (z. B. Rot und Blau): Modul nutzt BGR statt RGB - in
  `_INIT` das `_MADCTL`-Byte anpassen (Bit fuers Farbformat).

## Moegliche Erweiterungen

- Weitere Formen mit mehreren `fill_rect()`-Aufrufen zusammensetzen
- Mit `color565()` eigene Farbverlaeufe (Zeile fuer Zeile) ausprobieren
- Weiter zu [zahlen-zaehler](../zahlen-zaehler/): nur noch das veraenderte
  Rechteck neu zeichnen statt des ganzen Bildschirms
