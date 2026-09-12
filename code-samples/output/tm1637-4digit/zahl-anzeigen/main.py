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
