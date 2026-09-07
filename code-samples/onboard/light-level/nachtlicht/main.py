# Sample: nachtlicht  (LED-Matrix als Lichtsensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein automatisches Nachtlicht. Wird es im Raum dunkel, leuchtet die
#       ganze Matrix hell auf. Wird es wieder hell, geht sie aus.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - gemessen wird mit den LEDs der Matrix selbst.
#   Zum Testen den micro:bit mit der Hand abdecken.
# --------------------------------------------------------------------------

from microbit import *

GRENZE = 50   # darunter gilt es als "dunkel" (0..255)

while True:
    licht = display.read_light_level()

    if licht < GRENZE:
        display.show(Image("99999:99999:99999:99999:99999"))   # alles an
    else:
        display.clear()

    print("Licht:", licht)
    sleep(200)
