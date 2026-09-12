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
