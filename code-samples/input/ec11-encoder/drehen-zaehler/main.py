# Sample: drehen-zaehler  (EC11 Rotary Encoder mit Push)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Am Drehknopf drehen -> ein Wert 0..9 wird groesser / kleiner.
#       Die LED-Matrix zeigt die aktuelle Ziffer. Der Taster wird hier
#       noch nicht benutzt (siehe Sample "drehen-und-druck").
#
# --------------------------------------------------------------------------
# Verkabelung (EC11, Standard-Bauform)
# --------------------------------------------------------------------------
#   Encoder-Seite (3 Pins):
#     Pin A  (CLK)  ->  P0
#     Pin C  (COM)  ->  GND      (mittlerer Pin)
#     Pin B  (DT)   ->  P1
#
#   Taster-Seite (2 Pins):  hier noch nicht angeschlossen
#
#   Interne Pull-ups fuer P0 und P1 werden per Code aktiviert.
#   Hinweis: Pin A (CLK) und Pin B (DT) sind gleichwertig und je nach
#            Encoder anders beschriftet - die Schaltung geht so oder so.
#            Vertauscht man sie, dreht sich nur die Zaehlrichtung um.
#            Dreht der Zaehler falsch herum -> P0 und P1 tauschen
#            (oder unten die +1 / -1 vertauschen).
# --------------------------------------------------------------------------

from microbit import *

pin0.set_pull(pin0.PULL_UP)   # CLK
pin1.set_pull(pin1.PULL_UP)   # DT

wert = 0
letzter_clk = pin0.read_digital()

display.show(str(wert))

while True:
    clk = pin0.read_digital()

    # Nur bei einer fallenden Flanke an CLK zaehlen = eine Raste pro Schritt
    if clk != letzter_clk and clk == 0:
        if pin1.read_digital() == 1:
            wert = wert + 1     # im Uhrzeigersinn
        else:
            wert = wert - 1     # gegen den Uhrzeigersinn

        # Auf den Bereich 0..9 begrenzen
        wert = max(0, min(9, wert))
        display.show(str(wert))
        print("Wert:", wert)

    letzter_clk = clk
    sleep(1)   # kurze Pause, damit der Pin nicht zu schnell gelesen wird
