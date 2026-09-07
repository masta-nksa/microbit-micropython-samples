# Sample: bolzen-schalten  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Servo an einer Mechanik mit Endanschlag (2 Bolzen ueber ein Zahnrad).
#       Zwei Funktionen:
#         bolzen_rein()  - faehrt den Bolzen ein
#         bolzen_raus()  - faehrt den Bolzen aus
#       Ein zweiter Aufruf in DIESELBE Richtung wird ignoriert - sonst wuerde
#       der Servo gegen den Anschlag druecken (Stall -> Servo kaputt).
#       Nach jeder Fahrt wird der Servo stromlos geschaltet; die Reibung des
#       Bolzens haelt die Lage.
#
# --------------------------------------------------------------------------
# Verkabelung (wie alle Servo-Samples)
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V  (oder externe Batteriebox, GND gemeinsam)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

# ===== 1) Kalibrierte Endlagen (Mikrosekunden) ============================
PULS_REIN = 950      # Bolzen eingefahren - gemessen mit "endlagen-kalibrieren"
PULS_RAUS = 1500     # Bolzen ausgefahren - PLATZHALTER! Vor dem ersten
                     # bolzen_raus() unbedingt messen, sonst faehrt der Servo
                     # in den Anschlag.
# Brummt der Servo an einer Endlage: den Wert 15-30 us Richtung Mitte ruecken.

# ===== 2) Startzustand: wo steht der Bolzen beim Einschalten? =============
#   "raus"       Bolzen ausgefahren (z. B. Montagelage)
#   "rein"       Bolzen eingefahren
#   "unbekannt"  erster Aufruf darf in beide Richtungen
START_ZUSTAND = "raus"

# ===== 3) Fahr-Verhalten =================================================
SCHRITT = 8          # us pro Rampenschritt (kleiner = sanfter)
PAUSE   = 15         # ms zwischen den Rampenschritten
# ========================================================================

_PMIN = min(PULS_REIN, PULS_RAUS)
_PMAX = max(PULS_REIN, PULS_RAUS)
_MITTE = (PULS_REIN + PULS_RAUS) // 2

pin0.set_analog_period(20)          # 20 ms = 50 Hz

_zustand = START_ZUSTAND
_puls = _MITTE                      # Annahme fuer die erste Fahrt: sichere Mitte.
                                    # Der Servo bleibt bis zum ersten Aufruf stromlos.


def _schreibe(u):
    pin0.write_analog(int(u / 20000 * 1023))


def _fahre(ziel):
    global _puls
    ziel = max(_PMIN, min(_PMAX, ziel))     # nie ausserhalb des Fensters
    d = SCHRITT if ziel > _puls else -SCHRITT
    while abs(_puls - ziel) > SCHRITT:
        _puls += d
        _schreibe(_puls)
        sleep(PAUSE)
    _puls = ziel
    _schreibe(_puls)
    sleep(250)                              # ankommen lassen
    pin0.write_analog(0)                    # Servo stromlos -> Reibung haelt den Bolzen


def bolzen_rein():
    """Bolzen einfahren. Nur wirksam, wenn er nicht schon 'rein' ist."""
    global _zustand
    if _zustand == "rein":
        return False                        # schuetzt den Servo vor dem Anschlag
    _fahre(PULS_REIN)
    _zustand = "rein"
    return True


def bolzen_raus():
    """Bolzen ausfahren. Nur wirksam, wenn er nicht schon 'raus' ist."""
    global _zustand
    if _zustand == "raus":
        return False
    _fahre(PULS_RAUS)
    _zustand = "raus"
    return True


def bolzen_zustand():
    """Gibt 'rein', 'raus' oder 'unbekannt' zurueck."""
    return _zustand


# ===== Demo: Knopf A = einfahren, Knopf B = ausfahren ====================
# Dieser Teil darf weg, wenn du die Funktionen in dein eigenes Programm holst.

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # Notfall: langsam in die Mitte, Zustand zuruecksetzen
        _fahre(_MITTE)
        _zustand = "unbekannt"
        display.show("?")
        sleep(500)
        display.clear()

    elif button_a.was_pressed():
        display.show(Image.ARROW_W if bolzen_rein() else Image.NO)
        sleep(400)
        display.clear()

    elif button_b.was_pressed():
        display.show(Image.ARROW_E if bolzen_raus() else Image.NO)
        sleep(400)
        display.clear()
