# Sample: beruehr-toene  (Pins P0/P1/P2 als Beruehrungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein winziges Klavier. P0 antippen spielt einen tiefen Ton, P1 einen
#       mittleren, P2 einen hohen. Der Ton laeuft ueber den eingebauten
#       Lautsprecher (V2).
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - beim micro:bit V2 sind P0/P1/P2 kapazitive
#   Beruehrungssensoren. Einfach mit dem Finger auf das Pad tippen.
#   (Fuers "Fruechte-Klavier": Krokoklemmen von P0/P1/P2 an je ein Stueck
#    Obst, eine weitere Klemme von GND selbst festhalten.)
# --------------------------------------------------------------------------

from microbit import *
import music

# Pin -> Tonhoehe (Hz)
toene = [(pin0, 262), (pin1, 330), (pin2, 392)]   # c', e', g'

while True:
    for pin, frequenz in toene:
        if pin.is_touched():
            music.pitch(frequenz, 150, pin=None)   # pin=None -> interner Lautsprecher

    sleep(20)
