# Sample: melodie-und-sound  (eingebauter Lautsprecher, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Drei Arten, Klang zu erzeugen:
#       Knopf A  -> fertige Melodie (music)
#       Knopf B  -> Soundeffekt (audio)
#       Logo     -> einzelner Ton (music.pitch)
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Lautsprecher (V2) sitzt auf der Rueckseite.
#   Bei V1 stattdessen Kopfhoerer/Lautsprecher an P0 + GND.
# --------------------------------------------------------------------------

from microbit import *
import music
import audio

display.show(Image.MUSIC_QUAVER)

while True:
    if button_a.was_pressed():
        music.play(music.NYAN)          # fertige Melodie

    if button_b.was_pressed():
        audio.play(Sound.GIGGLE)        # Soundeffekt (nur V2)

    if pin_logo.is_touched():           # goldenes Logo beruehren (V2)
        music.pitch(880, 200)           # 880 Hz fuer 200 ms

    sleep(50)
