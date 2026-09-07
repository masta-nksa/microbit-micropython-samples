# Sample: temperatur-anzeigen  (eingebauter Temperatursensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A druecken -> die aktuelle Temperatur laeuft als Text ueber
#       die LED-Matrix. Knopf B -> ein Thermometer-Bild als Erinnerung,
#       dass es der Chip-Wert ist (leicht zu hoch).
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Sensor sitzt im Prozessor des micro:bit.
#   Achtung: er misst die Chip-Temperatur, meist ein paar Grad ueber der
#   Raumtemperatur, und reagiert langsam.
# --------------------------------------------------------------------------

from microbit import *

while True:
    if button_a.was_pressed():
        grad = temperature()          # Grad Celsius als ganze Zahl
        display.scroll(str(grad) + "C")
        print("Temperatur:", grad, "C")

    if button_b.was_pressed():
        display.show(Image.YES)       # nur als kurze Rueckmeldung
        sleep(500)
        display.clear()

    sleep(50)
