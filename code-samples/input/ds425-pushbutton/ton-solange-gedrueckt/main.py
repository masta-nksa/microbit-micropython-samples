# Sample: ton-solange-gedrueckt  (DS425 Pushbutton)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Der Ton erklingt genau so lange, wie der Taster gedrueckt gehalten wird.
#       Loslassen -> Ton aus.
#
# --------------------------------------------------------------------------
# Verkabelung (identisch zu Sample "ton-bei-druck")
# --------------------------------------------------------------------------
#   Taster-Bein 1  ->  Pin  P0
#   Taster-Bein 2  ->  Pin  GND
#
#   Interner Pull-up von P0 aktiv:
#     - losgelassen:  P0 = 1
#     - gedrueckt:    P0 = 0
# --------------------------------------------------------------------------

from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)

war_gedrueckt = False

while True:
    gedrueckt = (pin0.read_digital() == 0)

    if gedrueckt and not war_gedrueckt:
        # Flanke: gerade gedrueckt -> Dauerton starten
        # duration=-1  -> spielt endlos weiter
        # wait=False   -> Programm laeuft weiter (Ton im Hintergrund)
        # pin=None     -> nur ueber den eingebauten Lautsprecher (V2)
        music.pitch(440, -1, pin=None, wait=False)
        display.show(Image.MUSIC_QUAVER)

    elif not gedrueckt and war_gedrueckt:
        # Flanke: gerade losgelassen -> Ton stoppen
        music.stop()
        display.clear()

    war_gedrueckt = gedrueckt
    sleep(10)   # kurze Pause = einfache Entprellung
