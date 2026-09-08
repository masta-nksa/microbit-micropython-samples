# Sample: erste-farben  (WS2812B / NeoPixel LED-Strip)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den LED-Strip zum Leuchten bringen und die ersten LEDs einfaerben.
#
# --------------------------------------------------------------------------
# Verkabelung  (WS2812B braucht ~5 V - NICHT den 3V-Pin!)
# --------------------------------------------------------------------------
#   Strip DIN / DI / DATA  ->  P0
#   Strip 5V / VCC / +      ->  + der Batteriebox (3x 1.5 V = 4.5 V) oder 5V-Netzteil
#   Strip GND / -          ->  - der Batteriebox  UND  micro:bit GND (gemeinsame Masse!)
#
#   Am Strip-Ende anschliessen, wo die Pfeile WEG zeigen (Dateneingang).
#   Nach den Pad-Beschriftungen gehen, nicht nach der Kabelfarbe.
# --------------------------------------------------------------------------

from microbit import *
import neopixel

ANZAHL = 8          # <-- Anzahl LEDs auf DEINEM Strip eintragen
np = neopixel.NeoPixel(pin0, ANZAHL)     # Datenleitung an P0

# Farbe = (rot, gruen, blau), je 0..255.
# STROM: eine LED auf (255,255,255) zieht ~60 mA. Fuer Tests klein halten.
farben = [
    (60, 0, 0),     # rot
    (0, 60, 0),     # gruen
    (0, 0, 60),     # blau
    (60, 60, 0),    # gelb
    (60, 0, 60),    # magenta
    (0, 60, 60),    # cyan
    (40, 40, 40),   # weiss (gedimmt)
]

for i in range(ANZAHL):
    np[i] = farben[i % len(farben)]

np.show()           # erst show() schickt die Farben an den Strip

while True:
    sleep(1000)
