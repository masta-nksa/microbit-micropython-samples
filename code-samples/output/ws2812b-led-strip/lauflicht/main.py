# Sample: lauflicht  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein Leuchtpunkt wandert den Strip entlang und faengt vorne wieder an.
#       Knopf A / B machen ihn schneller / langsamer.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "erste-farben")
#   Strip DIN -> P0     Strip 5V -> 4.5 V-Box / 5V-Netzteil
#   Strip GND -> - der Box UND micro:bit GND (gemeinsame Masse)
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8
np = neopixel.NeoPixel(pin0, ANZAHL)

FARBE = (0, 40, 60)     # Farbe des Punkts
pause = 120             # ms pro Schritt (kleiner = schneller)

pos = 0

while True:
    np.clear()          # alle LEDs aus
    np[pos] = FARBE
    np.show()

    pos = (pos + 1) % ANZAHL   # weiter, am Ende zurueck auf 0

    if button_a.was_pressed():
        pause = max(20, pause - 30)
    if button_b.was_pressed():
        pause = min(500, pause + 30)

    sleep(pause)
