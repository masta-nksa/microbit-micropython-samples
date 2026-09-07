# Sample: shake-wuerfel  (eingebauter Beschleunigungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den micro:bit schuetteln wie einen Wuerfelbecher. Nach dem Schuetteln
#       erscheint eine Zufallszahl 1..6 auf der LED-Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Beschleunigungssensor ist fest eingebaut.
#   Das Schuetteln erkennt der micro:bit selbst als fertige Geste "shake".
# --------------------------------------------------------------------------

from microbit import *
import random

display.show(Image.HAPPY)

while True:
    # was_gesture("shake"): True, wenn seit dem letzten Aufruf geschuettelt wurde
    if accelerometer.was_gesture("shake"):
        augen = random.randint(1, 6)   # ganze Zahl von 1 bis 6 (inklusive)
        display.show(str(augen))
        print("gewuerfelt:", augen)

    sleep(100)
