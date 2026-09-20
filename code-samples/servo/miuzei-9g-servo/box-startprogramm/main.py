# Sample: box-startprogramm  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Startprogramm fuer die eigene Mysterybox. Knopf A oeffnet die Box,
#       Knopf B schliesst sie, A + B zusammen ist der Notfall (faehrt in die
#       Mitte). Danach kann man mit kleinen Ideen (siehe README) die Sensoren
#       des micro:bit einbauen.
#
#       Das Programm faehrt den Servo erst, wenn unter "1) Endlagen" beide
#       Werte eingetragen sind. Vorher zeigt die Matrix nur ein "?".
#
# --------------------------------------------------------------------------
# Verkabelung (wie alle Servo-Samples)
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  Batteriefach 3xAA (+)
#   Servo braun/schwarz (-)      ->  Batteriefach (-)  UND  micro:bit GND
# --------------------------------------------------------------------------

from microbit import *
import music        # nur fuer Ideen mit Ton - immer mit pin=None benutzen!

# ===== 1) Endlagen (Mikrosekunden) - mit "endlagen-kalibrieren" messen ====
PULS_AUF = None      # Box offen   (Beispiel: 950)
PULS_ZU = None       # Box zu      (Beispiel: 1500)
# Brummt der Servo an einer Endlage: den Wert 15-30 us Richtung Mitte ruecken.

# ===== 2) Startzustand: wie steht die Box beim Einschalten? ===============
#   "auf", "zu" oder "unbekannt" (dann darf der erste Befehl in beide
#   Richtungen fahren)
START_ZUSTAND = "unbekannt"

# ===== 3) Fahr-Verhalten ==================================================
SCHRITT = 8          # us pro Rampenschritt (kleiner = sanfter)
PAUSE = 15           # ms zwischen den Rampenschritten
# ========================================================================

pin0.set_analog_period(20)          # 20 ms = 50 Hz

_zustand = START_ZUSTAND
_puls = None                        # unbekannt, bis der Servo das erste Mal faehrt


def bereit():
    """True, sobald beide Endlagen eingetragen sind."""
    return PULS_AUF is not None and PULS_ZU is not None


def _schreibe(u):
    pin0.write_analog(int(u / 20000 * 1023))


def _fahre(ziel):
    global _puls
    lo = min(PULS_AUF, PULS_ZU)
    hi = max(PULS_AUF, PULS_ZU)
    ziel = max(lo, min(hi, ziel))           # nie ausserhalb des Fensters
    if _puls is None:
        _puls = (PULS_AUF + PULS_ZU) // 2   # erste Fahrt: sichere Mitte annehmen
    d = SCHRITT if ziel > _puls else -SCHRITT
    while abs(_puls - ziel) > SCHRITT:
        _puls += d
        _schreibe(_puls)
        sleep(PAUSE)
    _puls = ziel
    _schreibe(_puls)
    sleep(250)                              # ankommen lassen
    pin0.write_analog(0)                    # Servo stromlos -> Reibung haelt die Lage


def box_auf():
    """Box oeffnen. Gibt True zurueck, wenn sie gefahren ist."""
    global _zustand
    if not bereit() or _zustand == "auf":
        return False                        # schuetzt den Servo vor dem Anschlag
    _fahre(PULS_AUF)
    _zustand = "auf"
    return True


def box_zu():
    """Box schliessen. Gibt True zurueck, wenn sie gefahren ist."""
    global _zustand
    if not bereit() or _zustand == "zu":
        return False
    _fahre(PULS_ZU)
    _zustand = "zu"
    return True


def box_zustand():
    """Gibt 'auf', 'zu' oder 'unbekannt' zurueck."""
    return _zustand


def rueckmeldung(ok):
    """Haken (gefahren) oder Kreuz (nichts passiert) auf der Matrix."""
    if not bereit():
        display.show("?")                   # Endlagen fehlen -> erst messen
    else:
        display.show(Image.YES if ok else Image.NO)
    sleep(400)
    display.clear()


# ===== Hauptschleife ======================================================
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # Notfall: langsam in die Mitte, Zustand zuruecksetzen
        if bereit():
            _fahre((PULS_AUF + PULS_ZU) // 2)
            _zustand = "unbekannt"
        display.show("?")
        sleep(500)
        display.clear()

    elif button_a.was_pressed():
        rueckmeldung(box_auf())

    elif button_b.was_pressed():
        rueckmeldung(box_zu())

    # >>> IDEEN HIER EINFUEGEN (siehe README) <<<

    sleep(20)
