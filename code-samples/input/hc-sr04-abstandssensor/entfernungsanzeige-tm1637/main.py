# Sample: entfernungsanzeige-tm1637
# (HC-SR04 Ultraschall-Abstandssensor + TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den gemessenen Abstand in cm auf der 4-stelligen Anzeige darstellen.
#       Verbindet zwei Bauteile aus diesem Repo. Die Anzeige laeuft ueber die
#       Bibliothek tm1637.py (2. Datei im Projekt) - siehe README.
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
from tm1637 import TM1637

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
tm = TM1637(clk=pin1, dio=pin2, brightness=3)

# ----- Hauptschleife -----
while True:
    cm = abstand_cm()
    if cm is None:
        tm.show("    ")           # nichts erkannt -> Anzeige leer
        print("kein Echo")
    else:
        tm.number(int(cm))
        print("Abstand:", int(cm), "cm")

    sleep(150)   # >= 60 ms Pause zwischen Messungen
