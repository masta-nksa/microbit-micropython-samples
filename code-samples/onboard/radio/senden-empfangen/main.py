# Sample: senden-empfangen  (Funk zwischen zwei micro:bits)
# Board:   BBC micro:bit V2.2  (zwei Stueck)
# Sprache: MicroPython
#
# Ziel: Dasselbe Programm laeuft auf BEIDEN micro:bits. Knopf A zaehlt einen
#       Wert hoch und funkt ihn zum anderen Board. Wer eine Nachricht
#       empfaengt, zeigt die Zahl an und piept kurz.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Funk ist eingebaut. Nur brauchst du zwei
#   micro:bits, beide mit diesem Programm. Beide muessen dieselbe GRUPPE
#   benutzen (unten). Reichweite offen ca. 10..20 m.
# --------------------------------------------------------------------------

from microbit import *
import radio
import music

GRUPPE = 23   # auf beiden Boards gleich! Andere Teams: andere Zahl waehlen.

radio.on()
radio.config(group=GRUPPE)

zaehler = 0
display.show(Image.ARROW_N)

while True:
    # --- Senden ---
    if button_a.was_pressed():
        zaehler = zaehler + 1
        radio.send(str(zaehler))      # radio.send braucht Text
        display.show(str(zaehler % 10))

    # --- Empfangen ---
    nachricht = radio.receive()       # None, wenn nichts da ist
    if nachricht is not None:
        display.show(nachricht[-1])   # letzte Ziffer der empfangenen Zahl
        music.pitch(880, 80, pin=None)
        print("empfangen:", nachricht)

    sleep(20)
