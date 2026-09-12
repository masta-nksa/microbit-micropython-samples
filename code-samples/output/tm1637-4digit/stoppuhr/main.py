# Sample: stoppuhr  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Stoppuhr im Format MM:SS. Knopf A startet/pausiert, Knopf B setzt
#       zurueck (nur wenn pausiert - laeuft die Uhr, tut B nichts). Der
#       Doppelpunkt blinkt im Sekundentakt.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle TM1637-Samples)
#   Anzeige CLK -> P1     Anzeige DIO -> P2
#   Anzeige VCC -> 3V     Anzeige GND -> GND
# --------------------------------------------------------------------------

from microbit import *

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


def zwei_stellen(n):
    n = max(0, min(99, n))
    return [n // 10, n % 10]


def zeit_in_ziffern(sekunden):
    sekunden = max(0, min(5999, sekunden))   # bis 99:59
    minuten = sekunden // 60
    sek = sekunden % 60
    return zwei_stellen(minuten) + zwei_stellen(sek)


# ----- Stoppuhr -----
laeuft = False
start_ms = 0        # running_time() beim letzten Start
vergangen_ms = 0    # bereits aufsummierte Zeit, waehrend pausiert

while True:
    if button_a.was_pressed():
        if laeuft:
            vergangen_ms += running_time() - start_ms
            laeuft = False
        else:
            start_ms = running_time()
            laeuft = True

    if button_b.was_pressed() and not laeuft:
        vergangen_ms = 0

    aktuell_ms = vergangen_ms + ((running_time() - start_ms) if laeuft else 0)
    sekunden = aktuell_ms // 1000

    doppelpunkt = (aktuell_ms // 500) % 2 == 0   # blinkt im Sekundentakt
    anzeige(*zeit_in_ziffern(sekunden), doppelpunkt=doppelpunkt)
    sleep(50)
