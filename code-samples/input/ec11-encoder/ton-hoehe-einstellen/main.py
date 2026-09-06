# Sample: ton-hoehe-einstellen  (EC11 Rotary Encoder mit Push)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Drehen aendert die Tonhoehe eines Dauertons (200..2000 Hz).
#       Auf den Knopf druecken -> Ton an / aus (Umschalter).
#       Kombiniert Drehen + Druck aus den vorherigen Samples.
#
# --------------------------------------------------------------------------
# Verkabelung (EC11, Standard-Bauform)  -  wie "drehen-und-druck"
# --------------------------------------------------------------------------
#   Pin A (CLK) -> P0        Pin C (COM) -> GND        Pin B (DT) -> P1
#   SW 1        -> P2        SW 2        -> GND
#
#   Interne Pull-ups fuer P0, P1, P2 per Code.
#   Ton laeuft ueber den eingebauten Lautsprecher (pin=None), P0 bleibt frei.
# --------------------------------------------------------------------------

from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)   # CLK
pin1.set_pull(pin1.PULL_UP)   # DT
pin2.set_pull(pin2.PULL_UP)   # SW

frequenz = 440          # Start-Tonhoehe in Hz
SCHRITT = 20            # Hz pro Raste
ton_an = False

letzter_clk = pin0.read_digital()
war_gedrueckt = False


def ton_aktualisieren():
    # Ton neu setzen, wenn er an ist; sonst Stille.
    if ton_an:
        music.pitch(frequenz, -1, pin=None, wait=False)
    else:
        music.stop()


while True:
    # ----- Drehen: Tonhoehe aendern -----
    clk = pin0.read_digital()
    if clk != letzter_clk and clk == 0:
        if pin1.read_digital() == 1:
            frequenz = frequenz + SCHRITT
        else:
            frequenz = frequenz - SCHRITT
        frequenz = max(200, min(2000, frequenz))
        print("Frequenz:", frequenz, "Hz")
        ton_aktualisieren()
    letzter_clk = clk

    # ----- Druck: Ton an / aus -----
    gedrueckt = (pin2.read_digital() == 0)
    if gedrueckt and not war_gedrueckt:
        ton_an = not ton_an
        display.show(Image.MUSIC_QUAVER if ton_an else Image.NO)
        sleep(150)
        display.clear()
        ton_aktualisieren()
    war_gedrueckt = gedrueckt

    sleep(1)
