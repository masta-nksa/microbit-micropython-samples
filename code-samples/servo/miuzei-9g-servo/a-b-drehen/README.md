# a-b-drehen

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Knopf **A** gedrueckt halten dreht den Servo in die eine Richtung, Knopf **B**
in die andere. **A + B** zusammen bringt ihn zurueck auf 0 Grad. Erstes
Servo-Beispiel - die Verkabelung ist fuer alle Servo-Samples gleich.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 3 | Jumperkabel (oder Krokoklemmen + Servo-Adapter) |
| — | optional: Batteriebox 3x 1.5 V (siehe Stromversorgung) |

Masse fuers CAD: [../../../../hardware/servo/miuzei-9g-servo/](../../../../hardware/servo/miuzei-9g-servo/)

## Verkabelung

```
   micro:bit            Servo (3-poliges Kabel)
  +---------+        +---------------------+
  |      P0 |--------| orange/gelb  Signal |
  |      3V |--------| rot          +      |
  |     GND |--------| braun/schwarz -     |
  +---------+        +---------------------+
```

**Stromversorgung:** Ein einzelner unbelasteter Servo laeuft meist direkt am
`3V`-Pin. Zittert er oder startet der micro:bit neu -> externe Batteriebox
(3x 1.5 V = 4.5 V): `+` an Servo rot, `-` an Servo braun **und** an micro:bit
`GND` (gemeinsame Masse), Signal an `P0`, `3V` bleibt frei. Verdrahtung im
Detail: [Bauteil-README, "Anschluss mit externer Batteriebox"](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `pin0.set_analog_period(20)` + `servo_winkel(grad)` wie in allen Servo-Samples
  (rechnet 0..180 Grad in `write_analog(26..123)` um).
- **A + B zuerst pruefen** (`button_a.is_pressed() and button_b.is_pressed()`),
  sonst wuerde ein Druck auf beide nur hoch- oder runterdrehen.
- `is_pressed()` (nicht `was_pressed()`): solange der Knopf gehalten wird,
  aendert sich `winkel` jeden Durchlauf um `SCHRITT` Grad.
- `SCHRITT` und `sleep(20)` bestimmen zusammen das Dreh-Tempo.
- Die Anzeige wird nur bei Aenderung neu gesetzt - sonst flackert die Matrix.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: a-b-drehen  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A gedrueckt halten -> Servo dreht in die eine Richtung,
#       Knopf B gedrueckt halten -> in die andere Richtung.
#       A + B zusammen -> zurueck auf 0 Grad.
#
# --------------------------------------------------------------------------
# Verkabelung (3-poliges Servokabel)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V   (oder externe Batteriebox, dann GND
#                                          gemeinsam - siehe Bauteil-README)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)   # 20 ms = 50 Hz


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


SCHRITT = 3          # Grad pro Schleifendurchlauf (Tempo)
winkel = 0

servo_winkel(winkel)
letzte_anzeige = -1

while True:
    # A + B zuerst pruefen, sonst wuerde es nur hoch- oder runterzaehlen
    if button_a.is_pressed() and button_b.is_pressed():
        winkel = 0
    elif button_a.is_pressed():
        winkel = winkel + SCHRITT
    elif button_b.is_pressed():
        winkel = winkel - SCHRITT

    winkel = max(0, min(180, winkel))
    servo_winkel(winkel)

    # Anzeige nur bei Aenderung neu setzen (kein Flackern)
    if winkel != letzte_anzeige:
        display.show(str(winkel // 10))   # grobe Anzeige 0..18
        letzte_anzeige = winkel

    sleep(20)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: Servo auf 0 Grad, Matrix zeigt `0`
- A halten -> Servo dreht Richtung 180 Grad (Anzeige zaehlt hoch bis `18`)
- B halten -> Servo dreht zurueck Richtung 0 Grad
- A + B zusammen -> Servo springt auf 0 Grad

## Moegliche Erweiterungen

- `SCHRITT` groesser/kleiner fuer schnelleres/langsameres Drehen
- kurzer Tastendruck = kleiner Schritt, langer Druck = schnelles Drehen
- Endanschlaege enger setzen (z. B. 10..170 Grad), falls der Servo brummt
