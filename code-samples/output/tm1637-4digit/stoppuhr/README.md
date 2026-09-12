# stoppuhr

Bauteil: [TM1637 4-Digit-Anzeige](../README.md) · Kategorie: output

Eine Stoppuhr im Format **MM:SS**. Knopf **A** startet/pausiert, Knopf **B**
setzt zurueck - aber nur, solange pausiert ist. Der Doppelpunkt blinkt im
Sekundentakt.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | TM1637 4-Digit-Anzeige |
| 4 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/output/tm1637-4digit/](../../../../hardware/output/tm1637-4digit/)

## Verkabelung

Identisch zu [zahl-anzeigen](../zahl-anzeigen/README.md#verkabelung):

```
   P1 -> CLK      P2 -> DIO      3V -> VCC      GND -> GND
```

Details: [Bauteil-README](../README.md#anschluss-an-den-micro-bit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Bibliothek: tm1637.py

Zweite Datei im Projekt, identisch zu
[zahl-anzeigen](../zahl-anzeigen/README.md#bibliothek-tm1637py) -
[mcauser/microbit-tm1637](https://github.com/mcauser/microbit-tm1637), MIT-Lizenz.

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

- `running_time()` liefert die Millisekunden seit dem Einschalten. `start_ms`
  merkt sich den Wert beim letzten **Start**, `vergangen_ms` die bereits
  aufsummierte Zeit aus fruegheren Laeufen.
- **Knopf A** schaltet zwischen Laufen und Pause um; beim Pausieren wird die
  seit dem Start vergangene Zeit zu `vergangen_ms` addiert.
- **Knopf B wirkt nur, wenn `laeuft` False ist** - ein Reset waehrend die Uhr
  laeuft wuerde sonst die laufende Zeit verwerfen (gleiche Idee wie die
  Zustandssperre bei [bolzen-schalten](../../../servo/miuzei-9g-servo/bolzen-schalten/)).
- `tm.numbers(minuten, sek, colon=doppelpunkt)` zeigt zwei 2-stellige Zahlen
  mit Doppelpunkt dazwischen - genau fuer MM:SS gemacht. `doppelpunkt` wird
  per Ganzzahldivision der Millisekunden (`// 500`, gerade/ungerade) im
  Sekundentakt umgeschaltet.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: stoppuhr  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Stoppuhr im Format MM:SS. Knopf A startet/pausiert, Knopf B setzt
#       zurueck (nur wenn pausiert - laeuft die Uhr, tut B nichts). Der
#       Doppelpunkt blinkt im Sekundentakt.
#       Nutzt die Bibliothek tm1637.py (2. Datei im Projekt) - siehe README.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle TM1637-Samples)
#   Anzeige CLK -> P1     Anzeige DIO -> P2
#   Anzeige VCC -> 3V     Anzeige GND -> GND
# --------------------------------------------------------------------------

from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2, brightness=3)

laeuft = False
start_ms = 0        # running_time() beim letzten Start
vergangen_ms = 0    # bereits aufsummierte Zeit, waehrend pausiert

while True:
    if button_a.was_pressed():
        if laeuft:
            vergangen_ms += running_time() - start_ms
            laeuft = False
        else:
            start_ms = running_time()
            laeuft = True

    if button_b.was_pressed() and not laeuft:
        vergangen_ms = 0

    aktuell_ms = vergangen_ms + ((running_time() - start_ms) if laeuft else 0)
    sekunden = min(aktuell_ms // 1000, 5999)   # bis 99:59
    minuten = sekunden // 60
    sek = sekunden % 60

    doppelpunkt = (aktuell_ms // 500) % 2 == 0   # blinkt im Sekundentakt
    tm.numbers(minuten, sek, colon=doppelpunkt)
    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

1. `tm1637.py` als **zweite Datei** anlegen und den Bibliotheks-Code hineinkopieren.
2. Inhalt von `main.py` in die Hauptdatei kopieren.
3. <https://python.microbit.org/v/beta> -> **Connect** -> **Send to micro:bit**.

Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: `00:00`, Doppelpunkt blinkt
- Knopf A -> Uhr laeuft, Anzeige zaehlt hoch
- Knopf A nochmal -> Uhr haelt an
- Knopf B (nur im Stand) -> zurueck auf `00:00`

## Moegliche Erweiterungen

- Millisekunden als 5. Stelle mitlaufen lassen (auf einer zweiten Anzeige)
- Rundenzeiten per Knopf-Logo speichern und durchscrollen
- Countdown statt Stoppuhr (rueckwaerts bis 0, dann Ton)
