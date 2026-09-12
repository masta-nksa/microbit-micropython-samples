# zahl-anzeigen

Bauteil: [TM1637 4-Digit-Anzeige](../README.md) · Kategorie: output

Grundfunktion: ein paar Zahlen nacheinander auf der 4-stelligen Anzeige
darstellen. Nutzt die fertige Bibliothek
[mcauser/microbit-tm1637](https://github.com/mcauser/microbit-tm1637) als
zweite Projektdatei - wird in den weiteren Samples wiederverwendet.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | TM1637 4-Digit-Anzeige |
| 4 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/output/tm1637-4digit/](../../../../hardware/output/tm1637-4digit/)

## Verkabelung

```
   micro:bit          TM1637-Modul
  +---------+        +------------+
  |      P1 |--------| CLK        |
  |      P2 |--------| DIO        |
  |      3V |--------| VCC        |
  |     GND |--------| GND        |
  +---------+        +------------+
```

Nach der Beschriftung auf dem Modul anschliessen, nicht nach der Position -
die Pin-Reihenfolge ist von Modul zu Modul unterschiedlich. Kein externes
Netzteil noetig (anders als der WS2812B-Strip). Details:
[Bauteil-README](../README.md#anschluss-an-den-micro-bit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Bibliothek: tm1637.py

Zweite Datei im Projekt - MIT-lizenziert von Mike Causer, genau fuer den
micro:bit geschrieben (nutzt `pinX.write_digital()`, kein `machine.Pin`).
Original: [mcauser/microbit-tm1637](https://github.com/mcauser/microbit-tm1637).
Wie man eine zweite Datei im Online-Editor anlegt:
[docs/setup.md](../../../../docs/setup.md#zweite-datei-hinzufuegen-z-b-eine-mitgelieferte-bibliothek).

<!-- CODE:START:tm1637.py -->
```python
"""
MicroPython for micro:bit TM1637 quad 7-segment LED display driver
https://github.com/mcauser/microbit-tm1637

MIT License
Copyright (c) 2017 Mike Causer

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

from microbit import sleep

_SEG = bytearray(b'\x3F\x06\x5B\x4F\x66\x6D\x7D\x07\x7F\x6F\x77\x7C\x39\x5E\x79\x71\x3D\x76\x06\x1E\x76\x38\x55\x54\x3F\x73\x67\x50\x6D\x78\x3E\x1C\x2A\x76\x6E\x5B\x00\x40\x63')

class TM1637(object):
	def __init__(self, clk, dio, brightness=7):
		self._c = clk
		self._d = dio
		self._b = max(0, min(brightness, 7))
		self._data_cmd()
		self._dsp_ctrl()

	def _start(self):
		self._d.write_digital(0)
		self._c.write_digital(0)

	def _stop(self):
		self._d.write_digital(0)
		self._c.write_digital(1)
		self._d.write_digital(1)

	def _data_cmd(self):
		self._start()
		self._write_byte(0x40)
		self._stop()

	def _dsp_ctrl(self):
		self._start()
		self._write_byte(0x88 | self._b)
		self._stop()

	def _write_byte(self, b):
		for i in range(8):
			self._d.write_digital((b >> i) & 1)
			self._c.write_digital(1)
			self._c.write_digital(0)
		self._c.write_digital(0)
		self._c.write_digital(1)
		self._c.write_digital(0)

	def brightness(self, val=None):
		if val is None:
			return self._b
		self._b = max(0, min(val, 7))
		self._data_cmd()
		self._dsp_ctrl()

	def write(self, segments, pos=0):
		if not 0 <= pos <= 3:
			raise ValueError("Position out of range")
		self._data_cmd()
		self._start()
		self._write_byte(0xC0 | pos)
		for seg in segments:
			self._write_byte(seg)
		self._stop()
		self._dsp_ctrl()

	def encode_string(self, string):
		segments = bytearray(len(string))
		for i in range(len(string)):
			segments[i] = self.encode_char(string[i])
		return segments

	def encode_char(self, char):
		o = ord(char)
		if o == 32:
			return _SEG[36] # space
		if o == 42:
			return _SEG[38] # star/degrees
		if o == 45:
			return _SEG[37] # dash
		if o >= 65 and o <= 90:
			return _SEG[o-55] # uppercase A-Z
		if o >= 97 and o <= 122:
			return _SEG[o-87] # lowercase a-z
		if o >= 48 and o <= 57:
			return _SEG[o-48] # 0-9
		raise ValueError("Character out of range: {:d} '{:s}'".format(o, chr(o)))

	def hex(self, val):
		string = '{:04x}'.format(val & 0xffff)
		self.write(self.encode_string(string))

	def number(self, num):
		num = max(-999, min(num, 9999))
		string = '{0: >4d}'.format(num)
		self.write(self.encode_string(string))

	def numbers(self, num1, num2, colon=True):
		num1 = max(-9, min(num1, 99))
		num2 = max(-9, min(num2, 99))
		segments = self.encode_string('{0:0>2d}{1:0>2d}'.format(num1, num2))
		if colon:
			segments[1] |= 0x80 # colon on
		self.write(segments)

	def temperature(self, num):
		if num < -9:
			self.write([0x38, 0x3F]) # LO
		elif num > 99:
			self.write([0x76, 0x06]) # HI
		else:
			string = '{0: >2d}'.format(num)
			self.write(self.encode_string(string))
		self.write([_SEG[38], _SEG[12]], 2) # degrees C

	def show(self, string, colon=False):
		segments = self.encode_string(string)
		if len(segments) > 1 and colon:
			segments[1] |= 128
		self.write(segments[:4])

	def scroll(self, string, delay=250):
		segments = string if isinstance(string, list) else self.encode_string(string)
		data = [0] * 8
		data[4:0] = list(segments)
		for i in range(len(segments) + 5):
			self.write(data[0+i:4+i])
			sleep(delay)
```
<!-- CODE:END -->

## Wie der Code funktioniert

- `TM1637(clk=pin1, dio=pin2, brightness=3)` erstellt das Anzeige-Objekt.
- `tm.number(zahl)` stellt eine Zahl -999..9999 rechtsbuendig dar - genau das,
  was wir vorher von Hand nachgebaut hatten (fuehrende Leerstellen statt Nullen).
- Weitere Methoden der Bibliothek (`numbers()`, `show()`, `scroll()`, `hex()`,
  `temperature()`, `brightness()`): siehe
  [Bauteil-README](../README.md#bibliothek-statt-eigenbau-mcausermicrobit-tm1637).

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: zahl-anzeigen  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein paar Zahlen auf der 4-stelligen Anzeige darstellen. Nutzt die
#       fertige Bibliothek tm1637.py (2. Datei im Projekt) statt eines
#       selbst geschriebenen Treibers - siehe README.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Anzeige CLK   ->  P1
#   Anzeige DIO   ->  P2
#   Anzeige VCC   ->  3V     (TM1637 laeuft mit 3.3-5.5 V - der 3V-Pin reicht,
#                             anders als beim WS2812B-Strip!)
#   Anzeige GND   ->  GND
#
#   Nach der Beschriftung auf dem Modul anschliessen, nicht nach der Position -
#   die Reihenfolge der 4 Pins ist von Modul zu Modul unterschiedlich.
# --------------------------------------------------------------------------

from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2, brightness=3)   # Helligkeit 0 (dunkel) .. 7 (hell)

# ----- Demo: ein paar Zahlen nacheinander zeigen -----
for zahl in (0, 7, 42, 1234, 9999):
    tm.number(zahl)
    sleep(1500)

while True:
    sleep(1000)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

1. `tm1637.py` als **zweite Datei** anlegen (siehe oben) und den
   Bibliotheks-Code hineinkopieren.
2. Inhalt von `main.py` in die Hauptdatei kopieren.
3. <https://python.microbit.org/v/beta> -> **Connect** -> **Send to micro:bit**.

Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Nacheinander erscheinen `0`, `7`, `42`, `1234`, `9999`, je 1,5 Sekunden
- Nichts leuchtet: Verkabelung (v. a. CLK/DIO nicht vertauscht) und `3V`/`GND` pruefen
- Zufaellige/blinkende Segmente: Pins CLK und DIO vertauschen

## Moegliche Erweiterungen

- `tm.show("HALLO")` oder `tm.scroll("HALLO MICROBIT")` ausprobieren
- Helligkeit per Encoder einstellen ([ec11-encoder](../../../input/ec11-encoder/))
- eine negative Zahl anzeigen (`tm.number(-5)`)
