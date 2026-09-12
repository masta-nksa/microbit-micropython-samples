# Sample: entfernungsanzeige-tm1637
# (HC-SR04 Ultraschall-Abstandssensor + TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den gemessenen Abstand in cm auf der 4-stelligen Anzeige darstellen.
#       Verbindet zwei Bauteile aus diesem Repo.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   HC-SR04 Trig  ->  P8
#   HC-SR04 Echo  ->  P12
#   HC-SR04 Vcc   ->  3V      (Betrieb an 3V, siehe hc-sr04-Bauteil-README)
#   HC-SR04 Gnd   ->  GND
#
#   TM1637 CLK    ->  P1
#   TM1637 DIO    ->  P2
#   TM1637 VCC    ->  3V
#   TM1637 GND    ->  GND
#
#   P8/P12 sind schmale Pins - fuer diese Kombination ein Steckbrett benutzen.
# --------------------------------------------------------------------------

import machine
from microbit import *

# ----- HC-SR04 -----
TRIG = pin8
ECHO = pin12


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


# ----- TM1637 -----
CLK = pin1
DIO = pin2
HELLIGKEIT = 3

SEGMENTE = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]


def _start():
    CLK.write_digital(1)
    DIO.write_digital(1)
    DIO.write_digital(0)
    CLK.write_digital(0)


def _stop():
    DIO.write_digital(0)
    CLK.write_digital(1)
    DIO.write_digital(1)


def _write_byte(b):
    for i in range(8):
        CLK.write_digital(0)
        DIO.write_digital((b >> i) & 1)
        CLK.write_digital(1)
    CLK.write_digital(0)
    DIO.read_digital()
    CLK.write_digital(1)
    CLK.write_digital(0)


def anzeige(d0, d1, d2, d3, doppelpunkt=False):
    _start()
    _write_byte(0x40)
    _stop()

    _start()
    _write_byte(0xC0)
    for i, d in enumerate([d0, d1, d2, d3]):
        wert = SEGMENTE[d] if d is not None else 0x00
        if i == 1 and doppelpunkt:
            wert |= 0x80
        _write_byte(wert)
    _stop()

    _start()
    _write_byte(0x88 | HELLIGKEIT)
    _stop()


def zahl_in_ziffern(n):
    # MicroPython kennt kein str.rjust() - darum von Hand auffuellen.
    n = max(0, min(9999, n))
    text = str(n)
    while len(text) < 4:
        text = " " + text
    return [int(z) if z != " " else None for z in text]


# ----- Hauptschleife -----
while True:
    cm = abstand_cm()
    if cm is None:
        anzeige(None, None, None, None)   # nichts erkannt -> Anzeige leer
        print("kein Echo")
    else:
        anzeige(*zahl_in_ziffern(int(cm)))
        print("Abstand:", int(cm), "cm")

    sleep(150)   # >= 60 ms Pause zwischen Messungen
