# Sample: lautstaerke-balken  (eingebautes Mikrofon, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Die LED-Matrix zeigt die aktuelle Lautstaerke als Balken, der von
#       unten nach oben waechst. Leise = eine Reihe, laut (z. B. Klatschen)
#       = die ganze Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - das Mikrofon ist beim micro:bit V2 eingebaut
#   (kleines Loch auf der Vorderseite, daneben die Mikrofon-LED).
# --------------------------------------------------------------------------

from microbit import *

while True:
    # sound_level(): aktuelle Lautstaerke als Zahl 0..255
    pegel = microphone.sound_level()

    # In 0..5 leuchtende Reihen umrechnen
    reihen = min(5, pegel // 51)

    display.clear()
    for y in range(5):
        # y = 0 ist oben, y = 4 unten -> von unten her fuellen
        if (5 - y) <= reihen:
            for x in range(5):
                display.set_pixel(x, y, 9)

    sleep(50)
