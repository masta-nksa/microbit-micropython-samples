# Sample: bilder-und-text  (eingebaute LED-Matrix 5x5)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A spielt eine Bilderfolge ab, Knopf B laesst einen Text ueber
#       die Matrix scrollen. Zeigt die drei haeufigsten display-Befehle.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - die 5x5-LED-Matrix ist die Vorderseite des micro:bit.
# --------------------------------------------------------------------------

from microbit import *

# Fertige Bilder aus dem Image-Katalog
bilder = [Image.HAPPY, Image.HEART, Image.DUCK, Image.GHOST, Image.ROCKET]

display.show(Image.ARROW_W)   # "druecke einen Knopf"

while True:
    if button_a.was_pressed():
        # Jedes Bild 400 ms zeigen
        for bild in bilder:
            display.show(bild)
            sleep(400)
        display.clear()

    if button_b.was_pressed():
        # scroll() schiebt den Text von rechts nach links durch
        display.scroll("Hallo NKSA")

    sleep(50)
