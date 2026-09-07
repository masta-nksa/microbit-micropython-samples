# Sample: a-b-zaehler  (eingebaute Knoepfe A und B)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt einen Wert hoch, Knopf B zaehlt ihn runter,
#       beide zusammen setzen ihn auf 0 zurueck. Der Wert (0..9) steht
#       auf der LED-Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die Knoepfe A und B sind fest eingebaut
#   (links und rechts neben der LED-Matrix).
# --------------------------------------------------------------------------

from microbit import *

zaehler = 0
display.show(str(zaehler))

while True:
    # Beide Knoepfe gleichzeitig -> zuerst pruefen, sonst zaehlt es mit
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0

    # was_pressed(): reagiert einmal pro Druck (Flanke), kein Prellen
    elif button_a.was_pressed():
        zaehler = zaehler + 1

    elif button_b.was_pressed():
        zaehler = zaehler - 1

    # Auf den Bereich 0..9 begrenzen (eine Ziffer auf der Matrix)
    zaehler = max(0, min(9, zaehler))
    display.show(str(zaehler))

    sleep(50)
