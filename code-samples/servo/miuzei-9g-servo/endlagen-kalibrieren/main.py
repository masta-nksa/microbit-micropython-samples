# Sample: endlagen-kalibrieren  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Die sicheren Endpunkte einer eigenen Mechanik herausfinden.
#       Der Servo wird in FEINEN Schritten bewegt, bis der Bolzen / die
#       Klappe genau am Anschlag steht - dort A+B druecken, der Sketch
#       zeigt den Puls-Wert (in Mikrosekunden). Diesen Wert notieren
#       und spaeter in "bolzen-schalten" eintragen.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle Servo-Samples)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V  (oder externe Batteriebox, GND gemeinsam)
#   Servo braun/schwarz (-)      ->  GND
#
#   WICHTIG: Am besten mit ENTKOPPELTEM Servo starten oder den Servo grob in
#   Mittelstellung montieren. Der Sketch startet bei START_US und springt
#   beim ersten Tastendruck genau dorthin.
# --------------------------------------------------------------------------

from microbit import *

START_US = 1500      # Startwert. Kennst du dein Fenster schon grob,
                     # hier z. B. 950 eintragen, dann startet er dort.
SCHRITT  = 5         # us pro Schritt - klein lassen, damit nichts anschlaegt
MIN_US   = 500       # harte Grenzen, damit der Servo nicht ueberdreht
MAX_US   = 2500

pin0.set_analog_period(20)   # 20 ms = 50 Hz

us = START_US


def set_puls(u):
    pin0.write_analog(int(u / 20000 * 1023))


set_puls(us)
print("Start bei", us, "us")

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # aktuellen Wert ablesen
        display.scroll(us)
        print("--> aktueller Puls:", us, "us")
        sleep(300)

    elif button_a.is_pressed():
        if us > MIN_US:
            us -= SCHRITT
            set_puls(us)
            print(us)
        sleep(30)          # langsam, damit man rechtzeitig loslassen kann

    elif button_b.is_pressed():
        if us < MAX_US:
            us += SCHRITT
            set_puls(us)
            print(us)
        sleep(30)
