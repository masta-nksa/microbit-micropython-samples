# Sample: abstand-messen  (HC-SR04 Ultraschall-Abstandssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den Abstand zu einem Hindernis messen und als Balken auf der
#       LED-Matrix zeigen (naeher = mehr LEDs). Der Wert in cm geht
#       zusaetzlich ueber die serielle Konsole raus (Open Serial).
#
# --------------------------------------------------------------------------
# Verkabelung  (Betrieb an 3V - einfach und sicher, siehe Bauteil-README)
# --------------------------------------------------------------------------
#   Sensor Trig  ->  P1
#   Sensor Echo  ->  P2
#   Sensor Vcc   ->  3V   (statt der spezifizierten 5 V - reduziert die
#                          Reichweite, macht Echo aber ungefaehrlich fuer den Pin)
#   Sensor Gnd   ->  GND
#
#   Fuer mehr Reichweite (5V + Spannungsteiler an Echo): siehe Bauteil-README.
# --------------------------------------------------------------------------

import machine
from microbit import *

TRIG = pin1
ECHO = pin2

NAH_CM = 5     # ab hier: Balken komplett voll
FERN_CM = 40   # ab hier: Balken leer


def abstand_cm():
    TRIG.write_digital(0)
    sleep(2)
    TRIG.write_digital(1)
    sleep(1)                 # 1 ms Triggerimpuls (mehr als die geforderten 10 us)
    TRIG.write_digital(0)

    dauer_us = machine.time_pulse_us(ECHO, 1, 30000)   # auf HIGH-Puls warten, Timeout 30 ms
    if dauer_us < 0:
        return None           # kein Echo: zu nah, zu weit, oder nichts im Weg
    return dauer_us / 58.0     # Schallgeschwindigkeit -> cm


def balken(n):
    # n LEDs anzeigen (0..25), zeilenweise von oben
    n = max(0, min(25, n))
    display.clear()
    for i in range(n):
        display.set_pixel(i % 5, i // 5, 9)


while True:
    cm = abstand_cm()

    if cm is None:
        display.show(Image.NO)
        print("kein Echo")
    else:
        n = int(25 * (FERN_CM - cm) / (FERN_CM - NAH_CM))
        balken(n)
        print("Abstand:", round(cm, 1), "cm")

    sleep(100)   # >= 60 ms Pause zwischen Messungen (Datenblatt-Empfehlung)
