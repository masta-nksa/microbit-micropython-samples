# Aufgabe 1 - Pushbutton an Pin P0
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein externer Taster (Pushbutton Switch DS425 Momentary) wird ueber
#       die Pins mit dem micro:bit verbunden. Beim Druecken erscheint ein Herz
#       auf der LED-Matrix und es ertoent ein kurzer Ton.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Taster-Bein 1  ->  Pin  P0
#   Taster-Bein 2  ->  Pin  GND
#
#   Der DS425 hat 4 Beine. Je zwei gegenueberliegende Beine sind fest
#   miteinander verbunden. Beim Druecken werden die beiden Seiten verbunden.
#   -> Ein Bein einer Seite an P0, ein Bein der ANDEREN Seite an GND
#      (am besten diagonal gegenueberliegende Beine verwenden).
#
#   Es wird KEIN externer Widerstand benoetigt: der interne Pull-up-Widerstand
#   von P0 wird per Software eingeschaltet.
#     - Taster losgelassen:  P0 = 1  (High, ueber Pull-up an 3V)
#     - Taster gedrueckt:     P0 = 0  (Low, direkt an GND)
# --------------------------------------------------------------------------

from microbit import *
import music

# P0 als Eingang mit internem Pull-up-Widerstand konfigurieren.
# Ohne Pull-up "schwebt" der Pin und liefert zufaellige Werte.
pin0.set_pull(pin0.PULL_UP)

war_gedrueckt = False

while True:
    # Taster schliesst gegen GND -> gedrueckt entspricht dem Wert 0
    gedrueckt = (pin0.read_digital() == 0)

    if gedrueckt and not war_gedrueckt:
        # Flanke: gerade eben gedrueckt
        display.show(Image.HEART)
        # 880 Hz fuer 120 ms. pin=None -> Ton nur ueber den
        # eingebauten Lautsprecher des micro:bit V2 (P0 bleibt frei fuer den Taster).
        music.pitch(880, 120, pin=None)

    elif not gedrueckt and war_gedrueckt:
        # Flanke: gerade losgelassen
        display.clear()

    war_gedrueckt = gedrueckt
    sleep(10)   # kurze Pause = einfache Entprellung
