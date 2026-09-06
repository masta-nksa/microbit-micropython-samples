# Sample: drehen-und-druck  (EC11 Rotary Encoder mit Push)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Drehen aendert einen Zaehler (0..9, LED-Matrix zeigt die Ziffer).
#       Auf den Knopf druecken -> Zaehler zurueck auf 0 + kurzer Ton.
#
# --------------------------------------------------------------------------
# Verkabelung (EC11, Standard-Bauform)
# --------------------------------------------------------------------------
#   Encoder-Seite (3 Pins):
#     Pin A  (CLK)  ->  P0
#     Pin C  (COM)  ->  GND      (mittlerer Pin)
#     Pin B  (DT)   ->  P1
#
#   Taster-Seite (2 Pins):
#     SW 1          ->  P2
#     SW 2          ->  GND
#
#   Interne Pull-ups fuer P0, P1 und P2 werden per Code aktiviert.
#     - Knopf losgelassen:  P2 = 1
#     - Knopf gedrueckt:     P2 = 0
#   Hinweis: Dreht der Zaehler falsch herum -> P0 und P1 tauschen.
# --------------------------------------------------------------------------

from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)   # CLK
pin1.set_pull(pin1.PULL_UP)   # DT
pin2.set_pull(pin2.PULL_UP)   # SW (Taster im Knopf)

zaehler = 0
letzter_clk = pin0.read_digital()
war_gedrueckt = False

display.show(str(zaehler))

while True:
    # ----- Drehen auswerten -----
    clk = pin0.read_digital()
    if clk != letzter_clk and clk == 0:
        if pin1.read_digital() == 1:
            zaehler = zaehler + 1
        else:
            zaehler = zaehler - 1
        zaehler = max(0, min(9, zaehler))
        display.show(str(zaehler))
        print("Zaehler:", zaehler)
    letzter_clk = clk

    # ----- Druck auswerten (Flanke) -----
    gedrueckt = (pin2.read_digital() == 0)
    if gedrueckt and not war_gedrueckt:
        zaehler = 0
        music.pitch(660, 80, pin=None)
        display.show(str(zaehler))
        print("Reset")
    war_gedrueckt = gedrueckt

    sleep(1)
