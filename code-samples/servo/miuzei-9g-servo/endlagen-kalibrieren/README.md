# endlagen-kalibrieren

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Werkzeug-Sample: die **sicheren Endpunkte einer eigenen Mechanik** finden.
Der Servo wird in feinen 5-µs-Schritten bewegt; steht der Bolzen / die Klappe
am gewuenschten Punkt, zeigt **A+B** den aktuellen Puls-Wert an. Diesen Wert
notieren und in [bolzen-schalten](../bolzen-schalten/) eintragen.

Hintergrund: [Bauteil-README, "Servo an einer Mechanik mit Endanschlag"](../README.md#servo-an-einer-mechanik-mit-endanschlag).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 1 | deine Mechanik (am besten zuerst **entkoppelt** oder grob mittig montiert) |
| 3 | Jumperkabel |
| — | optional: Batteriebox 3x 1.5 V |

## Verkabelung

```
   P0  -> Signal (orange/gelb)
   3V  -> +      (rot)      (oder externe Batteriebox, GND gemeinsam)
   GND -> -      (braun/schwarz)
```

Details / Batteriebox: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `set_puls(us)` gibt einen Impuls von `us` Mikrosekunden aus
  (`write_analog(us / 20000 * 1023)`).
- `START_US` ist der Wert beim Einschalten. Der Servo springt beim ersten
  Tastendruck dorthin - darum vorher entkoppeln oder mittig montieren.
  Kennst du dein Fenster schon grob, `START_US` z. B. auf `950` setzen.
- Knopf **A** gedrueckt halten -> `us` sinkt in `SCHRITT`-Schritten (langsam,
  `sleep(30)`), Knopf **B** -> `us` steigt.
- `MIN_US` / `MAX_US` sind harte Grenzen (500 / 2500), damit der Servo nie
  ueberdreht.
- Jede Aenderung geht per `print()` auch auf die serielle Konsole
  (**Open Serial** im Editor).

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
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
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Kalibrier-Ablauf

1. Servo **entkoppelt** oder grob mittig montiert anschliessen, Sketch starten.
2. **Open Serial** oeffnen.
3. Mechanik ankoppeln (falls entkoppelt gestartet).
4. Mit **A** langsam Richtung erste Endlage fahren. **Stoppen, sobald der
   Servo anfaengt zu brummen oder haerter zu klingen** - das ist der Anschlag.
5. Ein kleines Stueck mit **B** zurueck (ca. 30 µs = 6 Schritte) = Sicherheitsmarge.
6. **A+B** druecken -> Wert vom Display / Serial ablesen und notieren
   (das ist `PULS_A`).
7. Dasselbe mit **B** Richtung zweite Endlage -> `PULS_B` notieren.
8. Beide Werte in [bolzen-schalten/main.py](../bolzen-schalten/main.py) eintragen.

## Erwartetes Verhalten

- A/B halten -> Servo wandert langsam, Werte laufen im Serial mit
- A+B -> aktueller µs-Wert scrollt ueber die LED-Matrix

## Moegliche Erweiterungen

- `SCHRITT` = 1 fuer noch feinere Kalibrierung
- zweite Taste am Pin fuer "grob / fein" umschalten
- den zuletzt mit A+B bestaetigten Wert dauerhaft anzeigen
