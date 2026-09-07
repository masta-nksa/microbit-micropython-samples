# Sample: bolzen-schalten  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Servo an einer Mechanik mit Endanschlag (hier: Bolzen ueber ein
#       Zahnrad rein/raus). Der Servo faehrt NUR zwischen zwei kalibrierten
#       Endpunkten und nie in den Anschlag.
#         Knopf A -> Stellung A     Knopf B -> Stellung B
#       Beim Einschalten faehrt er sanft in die Mitte des Fensters.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle Servo-Samples)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V  (oder externe Batteriebox, GND gemeinsam)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

# ===== HIER die kalibrierten Werte aus "endlagen-kalibrieren" eintragen =====
# Beide Werte MIT Sicherheitsmarge (ca. 30 us vom echten Anschlag weg)!
PULS_A = 950        # Knopf A  (z. B. Bolzen ausgefahren)
PULS_B = 1150       # Knopf B  (z. B. Bolzen eingefahren)   <-- PLATZHALTER, noch kalibrieren
# Falls A und B verkehrt herum wirken: die beiden Werte tauschen.
# ==========================================================================

SCHRITT = 8         # us pro Rampenschritt (kleiner = sanfter)
PAUSE   = 15        # ms zwischen den Rampenschritten
STROMLOS_NACH_BEWEGUNG = False   # True: Servo danach abschalten
                                 #       (nur wenn die Mechanik die Lage selbst haelt)

PULS_MIN = min(PULS_A, PULS_B)
PULS_MAX = max(PULS_A, PULS_B)

pin0.set_analog_period(20)   # 20 ms = 50 Hz


def set_puls(u):
    # nie ausserhalb des kalibrierten Fensters - schuetzt vor Tippfehlern
    u = max(PULS_MIN, min(PULS_MAX, u))
    pin0.write_analog(int(u / 20000 * 1023))


puls = (PULS_A + PULS_B) // 2      # Start: sichere Mitte des Fensters
set_puls(puls)
sleep(500)


def fahre_zu(ziel):
    global puls
    d = SCHRITT if ziel > puls else -SCHRITT
    while abs(puls - ziel) > SCHRITT:
        puls += d
        set_puls(puls)
        sleep(PAUSE)
    puls = ziel
    set_puls(puls)
    sleep(300)
    if STROMLOS_NACH_BEWEGUNG:
        pin0.write_analog(0)      # kein Dauerstrom, kein Brummen


while True:
    if button_a.was_pressed():
        display.show("A")
        fahre_zu(PULS_A)
        display.clear()
    if button_b.was_pressed():
        display.show("B")
        fahre_zu(PULS_B)
        display.clear()
