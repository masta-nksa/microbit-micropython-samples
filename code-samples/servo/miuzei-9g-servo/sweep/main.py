# Sample: sweep  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Der Servo faehrt langsam von 0 bis 180 Grad und wieder zurueck.
#       Knopf A haelt die Bewegung an bzw. startet sie wieder.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie Sample "zwei-stellungen")
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V   (bei Zittern/Reset: externes 4.5-V-Fach,
#                                          GND gemeinsam mit dem micro:bit)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)   # 20 ms = 50 Hz


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


winkel = 0
richtung = 1        # +1 = aufwaerts, -1 = abwaerts
laeuft = True

servo_winkel(winkel)

while True:
    # Knopf A: Bewegung an / aus
    if button_a.was_pressed():
        laeuft = not laeuft
        display.show(Image.ARROW_E if laeuft else Image.SQUARE_SMALL)
        sleep(200)
        display.clear()

    if laeuft:
        winkel = winkel + richtung * 5     # Schrittweite 5 Grad
        if winkel >= 180:
            winkel = 180
            richtung = -1
        elif winkel <= 0:
            winkel = 0
            richtung = 1
        servo_winkel(winkel)

    sleep(40)   # bestimmt das Tempo der Bewegung
