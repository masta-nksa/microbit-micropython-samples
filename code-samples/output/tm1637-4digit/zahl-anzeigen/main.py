# Sample: zahl-anzeigen  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein paar Zahlen auf der 4-stelligen Anzeige darstellen. Enthaelt den
#       kompletten TM1637-Treiber (kein extra Modul noetig) - der wird in
#       den weiteren Samples einfach wiederverwendet.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Anzeige CLK   ->  P1
#   Anzeige DIO   ->  P2
#   Anzeige VCC   ->  3V     (TM1637 laeuft mit 3.3-5.5 V - der 3V-Pin reicht,
#                             anders als beim WS2812B-Strip!)
#   Anzeige GND   ->  GND
#
#   Nach der Beschriftung auf dem Modul anschliessen, nicht nach der Position -
#   die Reihenfolge der 4 Pins ist von Modul zu Modul unterschiedlich.
# --------------------------------------------------------------------------

from microbit import *

CLK = pin1
DIO = pin2

HELLIGKEIT = 3   # 0 (dunkel) .. 7 (hell)

# 7-Segment-Codes fuer die Ziffern 0-9
SEGMENTE = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]


def _start():
    CLK.write_digital(1)
    DIO.write_digital(1)
    DIO.write_digital(0)     # DIO faellt waehrend CLK hoch ist -> Startbedingung
    CLK.write_digital(0)


def _stop():
    DIO.write_digital(0)
    CLK.write_digital(1)
    DIO.write_digital(1)     # DIO steigt waehrend CLK hoch ist -> Stopbedingung


def _write_byte(b):
    for i in range(8):                  # LSB zuerst
        CLK.write_digital(0)
        DIO.write_digital((b >> i) & 1)
        CLK.write_digital(1)
    CLK.write_digital(0)
    DIO.read_digital()      # DIO kurz als Eingang freigeben (Bestaetigung der Anzeige)
    CLK.write_digital(1)
    CLK.write_digital(0)


def anzeige(d0, d1, d2, d3, doppelpunkt=False):
    # d0..d3: Ziffer 0..9 oder None fuer eine leere Stelle
    _start()
    _write_byte(0x40)        # Datenbefehl: Adresse zaehlt automatisch weiter
    _stop()

    _start()
    _write_byte(0xC0)        # Adresse 0 = erste Ziffer
    for i, d in enumerate([d0, d1, d2, d3]):
        wert = SEGMENTE[d] if d is not None else 0x00
        if i == 1 and doppelpunkt:
            wert |= 0x80     # Doppelpunkt haengt bei den meisten Modulen hier
        _write_byte(wert)
    _stop()

    _start()
    _write_byte(0x88 | HELLIGKEIT)   # Anzeige an, Helligkeit setzen
    _stop()


def zahl_in_ziffern(n):
    # Zahl 0..9999 in 4 Ziffern zerlegen - fuehrende Leerstellen statt Nullen.
    # MicroPython kennt kein str.rjust() - darum von Hand auffuellen.
    n = max(0, min(9999, n))
    text = str(n)
    while len(text) < 4:
        text = " " + text
    return [int(z) if z != " " else None for z in text]


# ----- Demo: ein paar Zahlen nacheinander zeigen -----
for zahl in (0, 7, 42, 1234, 9999):
    anzeige(*zahl_in_ziffern(zahl))
    sleep(1500)

while True:
    sleep(1000)
