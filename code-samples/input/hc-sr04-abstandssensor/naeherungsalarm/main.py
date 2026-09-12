# Sample: naeherungsalarm  (HC-SR04 Ultraschall-Abstandssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Piept schneller, je naeher ein Hindernis ist - wie eine Einparkhilfe.
#       Weit weg: Stille. Ganz nah: schnelles Dauerpiepsen.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "abstand-messen")
#   Sensor Trig -> P1     Sensor Echo -> P2
#   Sensor Vcc  -> 3V     Sensor Gnd  -> GND
# --------------------------------------------------------------------------

import machine
import music
from microbit import *

TRIG = pin1
ECHO = pin2

NAH_CM = 5      # ab hier: schnellstes Piepsen
FERN_CM = 60    # ab hier: Stille


def abstand_cm():
    TRIG.write_digital(0)
    sleep(2)
    TRIG.write_digital(1)
    sleep(1)
    TRIG.write_digital(0)
    dauer_us = machine.time_pulse_us(ECHO, 1, 30000)
    if dauer_us < 0:
        return None
    return dauer_us / 58.0


letzter_beep = 0

while True:
    cm = abstand_cm()
    jetzt = running_time()

    if cm is not None and cm < FERN_CM:
        cm = max(NAH_CM, cm)
        # naeher -> kuerzeres Intervall (50 ms ganz nah .. 500 ms an der Grenze)
        intervall = int(50 + (cm - NAH_CM) / (FERN_CM - NAH_CM) * 450)
        if jetzt - letzter_beep >= intervall:
            music.pitch(1500, 40, pin=None)   # ueber den eingebauten Lautsprecher
            letzter_beep = jetzt
        display.show(Image.TARGET)
    else:
        display.clear()

    sleep(20)
