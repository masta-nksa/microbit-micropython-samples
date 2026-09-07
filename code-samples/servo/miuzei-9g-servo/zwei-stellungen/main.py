# Sample: zwei-stellungen  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A faehrt den Servo auf 0 Grad, Knopf B auf 180 Grad.
#       Beim Start steht der Servo auf 90 Grad (Mitte).
#       Anwendung: Klappe / Schranke / Schalter auf-zu.
#
# --------------------------------------------------------------------------
# Verkabelung (3-poliges Servokabel)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V     (siehe Hinweis unten!)
#   Servo braun/schwarz (-)      ->  GND
#
#   HINWEIS ZUR STROMVERSORGUNG:
#   Ein einzelner unbelasteter 9g-Servo laeuft meist direkt am 3V-Pin.
#   Zittert der Servo, macht der micro:bit einen Reset oder haengen mehrere
#   Servos dran -> externes Batteriefach (3x AA = 4.5 V) an rot/braun,
#   und GND von Batterie und micro:bit VERBINDEN (gemeinsame Masse).
#   Signal bleibt an P0.
# --------------------------------------------------------------------------

from microbit import *

# PWM fuer den Servo vorbereiten: 20 ms Periode = 50 Hz
pin0.set_analog_period(20)


def servo_winkel(grad):
    # grad 0..180 in einen Puls von ca. 0.5 ms bis 2.4 ms umrechnen.
    # write_analog(0..1023) entspricht 0..20 ms Puls.
    #   26  -> ca. 0.5 ms  (0 Grad)
    #   123 -> ca. 2.4 ms  (180 Grad)
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)
    pin0.write_analog(duty)
    # Zittert der Servo an den Endlagen: 26/123 naeher zusammen holen,
    # z. B. 34 und 115.


servo_winkel(90)   # Startstellung: Mitte

while True:
    if button_a.was_pressed():
        servo_winkel(0)
        display.show("A")
    if button_b.was_pressed():
        servo_winkel(180)
        display.show("B")
    sleep(10)
