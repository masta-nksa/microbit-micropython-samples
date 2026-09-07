# Sample: logo-schalter  (Touch-Logo, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Das goldene Logo wie einen Lichtschalter benutzen. Einmal antippen
#       -> Herz an. Nochmal antippen -> Herz aus. (Umschalter / Toggle)
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - das Logo ist beim micro:bit V2 ein Beruehrungssensor.
# --------------------------------------------------------------------------

from microbit import *

an = False              # aktueller Zustand
war_beruehrt = False    # Zustand im letzten Durchlauf

while True:
    beruehrt = pin_logo.is_touched()

    # Nur auf die Flanke reagieren: gerade eben angetippt
    if beruehrt and not war_beruehrt:
        an = not an     # umschalten
        if an:
            display.show(Image.HEART)
        else:
            display.clear()

    war_beruehrt = beruehrt
    sleep(20)           # kurze Pause = einfache Entprellung
