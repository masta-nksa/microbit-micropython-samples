# zahlen-zaehler

Bauteil: [1.8" TFT SPI Display (ST7735)](../README.md) · Kategorie: output

Knopf A zaehlt hoch, Knopf B runter, A+B setzt auf 0 zurueck - wie
[zaehler](../../tm1637-4digit/zaehler/) beim TM1637, aber auf dem
Farbdisplay mit einer selbstgebauten 4-stelligen Blockschrift.
**Performance-Beispiel:** anders als [farbflaechen](../farbflaechen/) wird
hier **nicht** bei jedem Update der ganze Bildschirm neu gezeichnet, sondern
nur die Ziffern, die sich seit dem letzten Mal veraendert haben.

> **Status: noch nicht auf echter Hardware getestet.**

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

Details: [Bauteil-README](../README.md#anschluss-an-den-microbit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Bibliothek: st7735.py

Gleiche Datei wie bei [farbflaechen](../farbflaechen/) - Details dort bzw.
im [Bauteil-README](../README.md#bibliothek-eigene-portierung-st7735py).

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

- `_FONT`: eine selbstgebaute 3x5-Punkte-Blockschrift fuer die Ziffern 0-9
  (und Leerzeichen), als String-Tupel - `"1"` = Pixel an. Jedes
  Blockschrift-Pixel wird als `SCALE`x`SCALE`-Quadrat (8x8) gezeichnet.
- `draw_digit(index, char)` zeichnet **eine einzelne Ziffernstelle**: zuerst
  das Zellen-Rechteck (`DIGIT_W`x`DIGIT_H`) schwarz loeschen, dann die
  "an"-Pixel der Ziffer als kleine weisse Quadrate darueber.
- **Der Performance-Trick:** `letzter_text` merkt sich die zuletzt
  angezeigten 4 Zeichen. Bei jedem Update wird `text` (der neue Wert)
  zeichenweise mit `letzter_text` verglichen - `draw_digit()` wird **nur**
  fuer die Stellen aufgerufen, die sich tatsaechlich geaendert haben. Zaehlt
  man z. B. von 122 auf 123 hoch, wird nur die letzte Ziffer neu gezeichnet,
  nicht alle vier.
- Vergleiche das mit [farbflaechen](../farbflaechen/), wo `display.fill()`
  jedes Mal den kompletten Bildschirm ueberschreibt - dort ist das ok, weil
  es nur ein paar Mal beim Start passiert, nicht in einer Dauerschleife.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: zahlen-zaehler  (1.8" TFT SPI Display, ST7735)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt hoch, Knopf B runter, A+B setzt auf 0 zurueck -
#       wie "zaehler" beim TM1637, aber auf dem Farbdisplay mit einer
#       selbstgebauten 4-stelligen Blockschrift.
#
#       Performance-Punkt: NICHT bei jedem Update display.fill() auf dem
#       ganzen Bildschirm aufrufen (128x160 Pixel dauern spuerbar). Stattdessen
#       wird jede der 4 Ziffern mit dem vorherigen Wert verglichen und nur
#       die tatsaechlich veraenderten Ziffern-Rechtecke neu gezeichnet.
#       Bei einem einfachen Hoch-/Runterzaehler aendert sich meistens nur
#       die letzte Ziffer - der Rest bleibt unangetastet.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle st7735-Samples)
#   Display SCK -> P13   Display SDA/MOSI -> P15   Display A0/DC -> P12
#   Display RESET -> P16   Display CS -> P8   Display LED/VCC -> 3V   GND -> GND
# --------------------------------------------------------------------------

from microbit import pin8, pin12, pin16, button_a, button_b, sleep
from st7735 import ST7735, BLACK, WHITE

display = ST7735(cs=pin8, dc=pin12, rst=pin16)

# 3x5-Punkte-Blockschrift, '1' = Pixel an
_FONT = {
    "0": ("111", "101", "101", "101", "111"),
    "1": ("010", "110", "010", "010", "111"),
    "2": ("111", "001", "111", "100", "111"),
    "3": ("111", "001", "111", "001", "111"),
    "4": ("101", "101", "111", "001", "001"),
    "5": ("111", "100", "111", "001", "111"),
    "6": ("111", "100", "111", "101", "111"),
    "7": ("111", "001", "010", "010", "010"),
    "8": ("111", "101", "111", "101", "111"),
    "9": ("111", "101", "111", "001", "111"),
    " ": ("000", "000", "000", "000", "000"),
}

SCALE = 8                       # ein Blockschrift-Pixel = 8x8 Bildschirm-Pixel
DIGIT_W = 3 * SCALE + 6         # Ziffernbreite + kleiner Abstand
DIGIT_H = 5 * SCALE
X0, Y0 = 4, 60                  # Startposition der 4-stelligen Anzeige


def draw_digit(index, char):
    x = X0 + index * DIGIT_W
    display.fill_rect(x, Y0, DIGIT_W, DIGIT_H, BLACK)  # nur DIESE Zelle loeschen
    rows = _FONT[char]
    for row in range(5):
        for col in range(3):
            if rows[row][col] == "1":
                display.fill_rect(x + col * SCALE, Y0 + row * SCALE, SCALE, SCALE, WHITE)


zaehler = 0
letzter_text = "    "  # erzwingt beim ersten Durchlauf, dass alle 4 Ziffern gezeichnet werden

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0
    elif button_a.was_pressed():
        zaehler = zaehler + 1
    elif button_b.was_pressed():
        zaehler = zaehler - 1
    zaehler = max(0, min(9999, zaehler))

    text = "{:>4d}".format(zaehler)
    for i in range(4):
        if text[i] != letzter_text[i]:
            draw_digit(i, text[i])
    letzter_text = text

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

1. `st7735.py` als **zweite Datei** anlegen (siehe oben) und den
   Bibliotheks-Code hineinkopieren.
2. Inhalt von `main.py` in die Hauptdatei kopieren.
3. <https://python.microbit.org/v/beta> -> **Connect** -> **Send to micro:bit**.

Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Beim Start erscheint `0` rechtsbuendig in der Blockschrift.
- Knopf A: Zahl zaehlt hoch (bis 9999), Knopf B: runter (bis 0), A+B
  gleichzeitig: zurueck auf 0.
- Beim Hoch-/Runterzaehlen "flackert" nur die Ziffer, die sich aendert - die
  anderen bleiben ruhig stehen (das ist der Sinn des Beispiels).
- Nichts erscheint: siehe [Erwartetes Verhalten bei farbflaechen](../farbflaechen/README.md#erwartetes-verhalten)
  fuer die grundlegende Fehlersuche (RESET/CS/DC, Farbformat).

## Moegliche Erweiterungen

- Blinkenden Doppelpunkt fuer eine Uhrzeit ergaenzen (wie beim
  [TM1637-Stoppuhr-Sample](../../tm1637-4digit/stoppuhr/))
- Farbe der Ziffern je nach Wert wechseln (z. B. rot bei 0)
- `SCALE` vergroessern/verkleinern und beobachten, wie sich die
  Update-Geschwindigkeit dabei veraendert
