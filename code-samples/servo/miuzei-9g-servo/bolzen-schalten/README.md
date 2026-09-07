# bolzen-schalten

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Servo an einer Mechanik mit **Endanschlag** (hier: zwei Bolzen ueber ein
Zahnrad rein/raus). Der Servo faehrt nur zwischen **zwei kalibrierten
Endpunkten** und nie gegen den Anschlag.

- Knopf **A** -> Stellung A, Knopf **B** -> Stellung B (sanfte Rampe)
- Beim Einschalten: sanft in die Mitte des kalibrierten Fensters

Die Endpunkte kommen aus [endlagen-kalibrieren](../endlagen-kalibrieren/).
Hintergrund: [Bauteil-README, "Servo an einer Mechanik mit Endanschlag"](../README.md#servo-an-einer-mechanik-mit-endanschlag).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 1 | deine Mechanik (Zahnrad + Bolzen) |
| 3 | Jumperkabel |
| — | optional: Batteriebox 3x 1.5 V (bei Last empfohlen) |

## Verkabelung

```
   P0  -> Signal (orange/gelb)
   3V  -> +      (rot)      (unter Last: externe Batteriebox, GND gemeinsam)
   GND -> -      (braun/schwarz)
```

Details / Batteriebox: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Einstellen (Pflicht vor dem ersten Lauf)

Im Code oben stehen zwei Werte:

```python
PULS_A = 950        # Knopf A
PULS_B = 1150       # Knopf B   <-- noch mit endlagen-kalibrieren ermitteln
```

- Beide Werte aus [endlagen-kalibrieren](../endlagen-kalibrieren/) uebernehmen,
  jeweils **mit ~30 µs Sicherheitsmarge** vom echten Anschlag weg.
- Wirken A und B verkehrt herum: die beiden Werte tauschen.
- `STROMLOS_NACH_BEWEGUNG = True` schaltet den Servo nach dem Fahren ab
  (kein Brummen, kein Dauerstrom) - nur nutzen, wenn die Mechanik die Lage
  selbst haelt. Sonst bei `False` lassen.

## Wie der Code funktioniert

- `set_puls(us)` klemmt jeden Wert auf `[PULS_MIN, PULS_MAX]` (die beiden
  kalibrierten Endpunkte) - so kann der Servo baulich nicht ueberdreht werden.
- `puls` startet auf `(PULS_A + PULS_B) // 2` -> immer innerhalb des Fensters,
  nie auf 1500 µs (das koennte schon am Anschlag sein).
- `fahre_zu(ziel)` bewegt den Servo in `SCHRITT`-µs-Stufen mit `PAUSE` ms
  Pause - langsam und ohne Ruck, das schont Getriebe und Stromversorgung.
- `button_x.was_pressed()` -> eine Fahrt pro Tastendruck.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
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
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Einschalten: Servo faehrt sanft in die Fenstermitte
- Knopf A -> faehrt langsam auf `PULS_A`, Matrix zeigt kurz "A"
- Knopf B -> faehrt langsam auf `PULS_B`, Matrix zeigt kurz "B"
- Der Servo laeuft nie hoerbar gegen einen Widerstand

## Moegliche Erweiterungen

- nur eine Taste, die zwischen A und B umschaltet (Toggle)
- Zwischenstellung als dritte Position (z. B. Knopf-Logo antippen)
- nach `fahre_zu` pruefen, ob der Servo die Lage haelt (kurze Wartezeit)
- Tempo (`SCHRITT` / `PAUSE`) an die Mechanik anpassen
