# winkel-mit-encoder

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Am Drehknopf ([EC11](../../../input/ec11-encoder/)) drehen stellt den
Servo-Winkel in 10-Grad-Schritten zwischen 0 und 180 Grad. Knopf **A** setzt
zurueck auf 90 Grad. Verbindet Servo-Ansteuerung und Encoder.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 1 | EC11 Rotary Encoder |
| 1 | Steckbrett |
| ~7 | Jumperkabel |
| — | optional: Batteriefach 3x AA |

Masse fuers CAD: [../../../../hardware/servo/miuzei-9g-servo/](../../../../hardware/servo/miuzei-9g-servo/)

## Verkabelung

```
   micro:bit          Servo                 EC11 (nur Drehteil)
  +---------+
  |      P0 |--------- Signal (orange/gelb)
  |      3V |--------- +      (rot)
  |     GND |--------- -      (braun) --+-- C (COM, Mittelpin)
  |         |                           |
  |      P1 |------------------------------- A (CLK)
  |      P2 |------------------------------- B (DT)
  +---------+
```

- Interne Pull-ups fuer `P1` und `P2` per Code. Der Taster im Encoder-Knopf
  wird hier nicht benutzt.
- Dreht der Winkel falsch herum -> `P1` und `P2` tauschen.
- **Stromversorgung:** wie bei den anderen Servo-Samples. Bewegt sich der
  Servo unter Last oder startet der micro:bit neu -> externe Batteriebox
  (3x 1.5 V = 4.5 V): `+` an Servo rot, `-` an Servo braun **und** an
  micro:bit `GND`. Der Encoder-COM bleibt am selben `GND`. `3V` frei lassen.
  Details: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- Servo an `P0` wie in den anderen Samples (`servo_winkel(grad)`).
- Encoder an `P1`/`P2`: bei einer fallenden Flanke an `P1` (eine Raste) sagt
  der Zustand von `P2` die Drehrichtung -> `grad` +/- 10.
- `grad` bleibt mit `max(0, min(180, grad))` im gueltigen Bereich.
- Die LED-Matrix zeigt `grad // 10` (0..18) als grobe Anzeige.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: winkel-mit-encoder  (Miuzei Micro Servo 9g + EC11 Rotary Encoder)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Am Drehknopf (EC11) drehen stellt den Servo-Winkel in 10-Grad-Schritten
#       zwischen 0 und 180 Grad. Knopf A setzt zurueck auf 90 Grad (Mitte).
#       Kombiniert das Servo-Ansteuern mit dem Encoder aus code-samples/input.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Servo:
#     orange/gelb (Signal)  ->  P0
#     rot         (+)        ->  3V    (bei Zittern/Reset: externes 4.5-V-Fach,
#                                       GND gemeinsam)
#     braun/schwarz (-)      ->  GND
#
#   EC11 Encoder (nur Drehteil, Taster im Knopf bleibt frei):
#     Pin A (CLK)  ->  P1
#     Pin B (DT)   ->  P2
#     Pin C (COM)  ->  GND   (mittlerer Pin der 3er-Seite)
#
#   Interne Pull-ups fuer P1 und P2 per Code.
#   Dreht der Winkel falsch herum -> P1 und P2 tauschen.
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)          # Servo-PWM: 20 ms = 50 Hz
pin1.set_pull(pin1.PULL_UP)         # Encoder CLK
pin2.set_pull(pin2.PULL_UP)         # Encoder DT


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


grad = 90
servo_winkel(grad)
display.show(str(grad // 10))

letzter_clk = pin1.read_digital()

while True:
    # ----- Encoder drehen -> Winkel aendern -----
    clk = pin1.read_digital()
    if clk != letzter_clk and clk == 0:        # fallende Flanke = eine Raste
        if pin2.read_digital() == 1:
            grad = grad + 10
        else:
            grad = grad - 10
        grad = max(0, min(180, grad))
        servo_winkel(grad)
        display.show(str(grad // 10))          # 0..18
        print("Winkel:", grad)
    letzter_clk = clk

    # ----- Knopf A -> zurueck auf 90 Grad -----
    if button_a.was_pressed():
        grad = 90
        servo_winkel(grad)
        display.show(str(grad // 10))
        print("Mitte")

    sleep(1)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Drehen im Uhrzeigersinn -> Servo-Winkel groesser, gegen den Uhrzeigersinn -> kleiner
- Knopf A -> Servo springt auf 90 Grad
- **Open Serial** zeigt `Winkel: ...`

## Moegliche Erweiterungen

- Encoder-Druck (an `P8` o. ae.) nutzen, um Schrittweite umzuschalten
- Zwei Servos mit einem Encoder abwechselnd steuern
- Servo dem Zielwinkel weich folgen lassen statt in Spruengen
