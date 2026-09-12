# Sample: zaehler  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt hoch, Knopf B runter, A+B setzt auf 0 zurueck.
#       Wie das onboard-Sample "a-b-zaehler", nur mit der externen
#       4-stelligen Anzeige statt der LED-Matrix (Bereich 0..9999 statt 0..9).
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

zaehler = 0
tm.number(zaehler)

while True:
    # A + B zuerst pruefen, sonst wuerde es nur hoch- oder runterzaehlen
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0
    elif button_a.was_pressed():
        zaehler = zaehler + 1
    elif button_b.was_pressed():
        zaehler = zaehler - 1

    zaehler = max(0, min(9999, zaehler))
    tm.number(zaehler)
    sleep(50)
