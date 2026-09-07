# Sample: a-b-drehen  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A gedrueckt halten -> Servo dreht in die eine Richtung,
#       Knopf B gedrueckt halten -> in die andere Richtung.
#       A + B zusammen -> zurueck auf 0 Grad.
#
# --------------------------------------------------------------------------
# Verkabelung (3-poliges Servokabel)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V   (oder externe Batteriebox, dann GND
#                                          gemeinsam - siehe Bauteil-README)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)   # 20 ms = 50 Hz


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


SCHRITT = 3          # Grad pro Schleifendurchlauf (Tempo)
winkel = 0

servo_winkel(winkel)
letzte_anzeige = -1

while True:
    # A + B zuerst pruefen, sonst wuerde es nur hoch- oder runterzaehlen
    if button_a.is_pressed() and button_b.is_pressed():
        winkel = 0
    elif button_a.is_pressed():
        winkel = winkel + SCHRITT
    elif button_b.is_pressed():
        winkel = winkel - SCHRITT

    winkel = max(0, min(180, winkel))
    servo_winkel(winkel)

    # Anzeige nur bei Aenderung neu setzen (kein Flackern)
    if winkel != letzte_anzeige:
        display.show(str(winkel // 10))   # grobe Anzeige 0..18
        letzte_anzeige = winkel

    sleep(20)
