# Sample: winkel-mit-encoder  (Miuzei Micro Servo 9g + EC11 Rotary Encoder)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Am Drehknopf (EC11) drehen stellt den Servo-Winkel in 10-Grad-Schritten
#       zwischen 0 und 180 Grad. Knopf A setzt zurueck auf 90 Grad (Mitte).
#       Kombiniert das Servo-Ansteuern mit dem Encoder aus code-samples/input.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Servo:
#     orange/gelb (Signal)  ->  P0
#     rot         (+)        ->  3V    (bei Zittern/Reset: externes 4.5-V-Fach,
#                                       GND gemeinsam)
#     braun/schwarz (-)      ->  GND
#
#   EC11 Encoder (nur Drehteil, Taster im Knopf bleibt frei):
#     Pin A (CLK)  ->  P1
#     Pin B (DT)   ->  P2
#     Pin C (COM)  ->  GND   (mittlerer Pin der 3er-Seite)
#
#   Interne Pull-ups fuer P1 und P2 per Code.
#   Dreht der Winkel falsch herum -> P1 und P2 tauschen.
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)          # Servo-PWM: 20 ms = 50 Hz
pin1.set_pull(pin1.PULL_UP)         # Encoder CLK
pin2.set_pull(pin2.PULL_UP)         # Encoder DT


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


grad = 90
servo_winkel(grad)
display.show(str(grad // 10))

letzter_clk = pin1.read_digital()

while True:
    # ----- Encoder drehen -> Winkel aendern -----
    clk = pin1.read_digital()
    if clk != letzter_clk and clk == 0:        # fallende Flanke = eine Raste
        if pin2.read_digital() == 1:
            grad = grad + 10
        else:
            grad = grad - 10
        grad = max(0, min(180, grad))
        servo_winkel(grad)
        display.show(str(grad // 10))          # 0..18
        print("Winkel:", grad)
    letzter_clk = clk

    # ----- Knopf A -> zurueck auf 90 Grad -----
    if button_a.was_pressed():
        grad = 90
        servo_winkel(grad)
        display.show(str(grad // 10))
        print("Mitte")

    sleep(1)
