# bolzen-schalten

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Servo an einer Mechanik mit **Endanschlag** (zwei Bolzen ueber ein Zahnrad
rein/raus). Zwei Funktionen zum Aufrufen:

```python
bolzen_rein()    # Bolzen einfahren
bolzen_raus()    # Bolzen ausfahren
```

- Fahren nur von einer Endlage in die andere. Ein zweiter Aufruf in
  **dieselbe Richtung** wird ignoriert (`return False`) - sonst wuerde der
  Servo gegen den Anschlag druecken und kaputtgehen.
- Sanfte Rampe in kleinen µs-Schritten.
- Nach der Fahrt wird der Servo **stromlos** geschaltet (`write_analog(0)`);
  die Reibung des Bolzens haelt die Lage.

Endpunkte kommen aus [endlagen-kalibrieren](../endlagen-kalibrieren/).
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

Oben im Code stehen drei Dinge:

```python
PULS_REIN = 950      # Bolzen eingefahren  (gemessen)
PULS_RAUS = 1500     # Bolzen ausgefahren  <-- PLATZHALTER, noch messen!
START_ZUSTAND = "raus"
```

1. **`PULS_REIN`** - der mit [endlagen-kalibrieren](../endlagen-kalibrieren/)
   gemessene Wert fuer "Bolzen ganz eingefahren" (hier `950`, wie bei dir).
2. **`PULS_RAUS`** noch messen: `endlagen-kalibrieren` laden, `START_US = 950`
   setzen, mit **B** langsam ausfahren, kurz vor dem Anschlag stoppen,
   **A+B** druecken, Wert ablesen und hier eintragen.
3. **`START_ZUSTAND`** auf die Lage setzen, in der der Bolzen beim Einschalten
   wirklich steht (`"raus"`, `"rein"` oder `"unbekannt"`).
4. Brummt der Servo an einer Endlage: den betroffenen Wert 15-30 µs Richtung
   Mitte ruecken (etwas weniger weit fahren).

Wirken A/B verkehrt herum: `PULS_REIN` und `PULS_RAUS` tauschen (und
`START_ZUSTAND` anpassen).

## Wie der Code funktioniert

- `_fahre(ziel)` rampt den Puls in `SCHRITT`-µs-Stufen mit `PAUSE` ms Pause,
  klemmt jeden Wert auf `[PULS_REIN, PULS_RAUS]` und schaltet den Servo am
  Ende mit `write_analog(0)` ab.
- `_puls` startet auf der **Fenstermitte**. Der erste Aufruf macht darum
  eine kurze Bewegung zur Mitte und dann zum Ziel - das ist Absicht (sichere
  Ausgangslage, egal wo der Servo wirklich steht).
- `_zustand` merkt sich `"rein"` / `"raus"` / `"unbekannt"`. `bolzen_rein()`
  tut nichts, wenn `_zustand` schon `"rein"` ist - so kann kein Aufruf den
  Servo in den Anschlag schicken.
- **Demo im `while`-Loop:** Knopf A ruft `bolzen_rein()`, Knopf B
  `bolzen_raus()`, **A+B** faehrt langsam in die Mitte und setzt den Zustand
  auf `"unbekannt"` (Notfall / Neu-Synchronisieren).

Fuer dein eigenes Programm einfach den Block bis `bolzen_zustand()` kopieren
und die Funktionen aufrufen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
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
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Einschalten: Servo bleibt still (stromlos)
- Knopf A: Bolzen faehrt ein (Pfeil links). War er schon drin -> X, nichts passiert
- Knopf B: Bolzen faehrt aus (Pfeil rechts). War er schon draussen -> X
- Nach jeder Fahrt ist der Servo lautlos (kein Brummen), der Bolzen bleibt stehen
- A+B: Servo faehrt langsam in die Mitte, Display zeigt `?`

## Moegliche Erweiterungen

- eine Taste, die zwischen rein/raus umschaltet (Toggle)
- den Zustand mit `microbit`-Datei speichern, damit er einen Neustart uebersteht
- Ausloesen per Funk (`radio`) von einem zweiten micro:bit
- Zwischenstellung als dritte Position
