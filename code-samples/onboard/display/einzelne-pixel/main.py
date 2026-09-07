# Sample: einzelne-pixel  (eingebaute LED-Matrix 5x5)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Einen einzelnen Leuchtpunkt mit den Knoepfen ueber die Matrix
#       bewegen. A schiebt nach rechts, B nach unten - am Rand geht es
#       auf der anderen Seite weiter.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die 5x5-LED-Matrix ist eingebaut.
#   Koordinaten: x = Spalte 0..4 (links->rechts), y = Zeile 0..4 (oben->unten).
# --------------------------------------------------------------------------

from microbit import *

x = 2
y = 2

while True:
    if button_a.was_pressed():
        x = (x + 1) % 5      # 4 -> 0 (Sprung an den linken Rand)

    if button_b.was_pressed():
        y = (y + 1) % 5      # 4 -> 0 (Sprung an den oberen Rand)

    display.clear()
    display.set_pixel(x, y, 9)   # Helligkeit 9 = maximal

    sleep(50)
