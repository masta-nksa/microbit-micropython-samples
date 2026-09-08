# Sample: regenbogen  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Regenbogen laeuft ueber den ganzen Strip.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "erste-farben")
#   Strip DIN -> P0     Strip 5V -> 4.5 V-Box / 5V-Netzteil
#   Strip GND -> - der Box UND micro:bit GND (gemeinsame Masse)
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8
HELLIGKEIT = 40        # 0..255 - klein halten (Strom!)
np = neopixel.NeoPixel(pin0, ANZAHL)


def farbrad(pos):
    # pos 0..255 -> Regenbogenfarbe (rot, gruen, blau)
    pos = pos % 256
    if pos < 85:
        r, g, b = 255 - pos * 3, pos * 3, 0
    elif pos < 170:
        pos -= 85
        r, g, b = 0, 255 - pos * 3, pos * 3
    else:
        pos -= 170
        r, g, b = pos * 3, 0, 255 - pos * 3
    # auf die gewuenschte Helligkeit herunterrechnen
    return (r * HELLIGKEIT // 255, g * HELLIGKEIT // 255, b * HELLIGKEIT // 255)


versatz = 0

while True:
    for i in range(ANZAHL):
        np[i] = farbrad(i * 256 // ANZAHL + versatz)
    np.show()

    versatz = (versatz + 4) % 256   # groesser = schneller
    sleep(50)
