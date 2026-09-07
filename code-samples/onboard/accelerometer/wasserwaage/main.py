# Sample: wasserwaage  (eingebauter Beschleunigungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein einzelner Leuchtpunkt auf der LED-Matrix zeigt die Neigung des
#       micro:bit an. Liegt das Board flach, leuchtet die Mitte. Kippt man
#       es, wandert der Punkt in die Kipprichtung - wie eine Libelle.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Beschleunigungssensor ist fest eingebaut.
# --------------------------------------------------------------------------

from microbit import *

while True:
    # get_x(): quer zur Platine, get_y(): laengs. Einheit Milli-g.
    # Bei Neigung etwa -1000..1000. Teilen durch 300 -> Schritte -3..3.
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    spalte = 2 + x // 300
    zeile = 2 + y // 300

    # Auf die 5x5-Matrix begrenzen (Index 0..4)
    spalte = max(0, min(4, spalte))
    zeile = max(0, min(4, zeile))

    display.clear()
    display.set_pixel(spalte, zeile, 9)

    sleep(50)
