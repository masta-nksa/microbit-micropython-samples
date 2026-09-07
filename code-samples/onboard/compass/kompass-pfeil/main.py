# Sample: kompass-pfeil  (eingebauter Kompass / Magnetometer)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Pfeil auf der LED-Matrix zeigt immer nach Norden, egal wie man
#       den micro:bit dreht.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Magnetsensor ist eingebaut.
#   Vor der ersten Messung MUSS kalibriert werden (siehe unten).
#   Abseits von Metall, Magneten und Netzteilen halten.
# --------------------------------------------------------------------------

from microbit import *

# Kalibrier-Spiel: den micro:bit kippen, bis der Rand voll ist.
# Laeuft nur, wenn noch nicht kalibriert.
if not compass.is_calibrated():
    compass.calibrate()

# Image.ALL_ARROWS: 0=N, 1=NO, 2=O, 3=SO, 4=S, 5=SW, 6=W, 7=NW
pfeile = Image.ALL_ARROWS

while True:
    richtung = compass.heading()   # 0..359 Grad, 0 = Norden

    # Norden relativ zur Blickrichtung des Boards -> passender Pfeil.
    # + 22.5 rundet auf das naechste der 8 Achtel.
    index = int((360 - richtung + 22.5) // 45) % 8
    display.show(pfeile[index])

    sleep(200)
