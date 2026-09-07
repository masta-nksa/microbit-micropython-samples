# zwei-stellungen

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Knopf **A** faehrt den Servo auf 0 Grad, Knopf **B** auf 180 Grad. Beim Start
steht er auf 90 Grad. Typische Anwendung: Klappe, Schranke oder Schalter
auf/zu.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 3 | Jumperkabel (oder Krokoklemmen + Servo-Adapter) |
| — | optional: Batteriefach 3x AA (siehe Stromversorgung) |

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
`3V`-Pin. Zittert er oder startet der micro:bit neu -> externes Batteriefach
(3x AA = 4.5 V) an rot/braun und **GND von Batterie und micro:bit verbinden**.
Signal bleibt an `P0`. Details: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `pin0.set_analog_period(20)` stellt die PWM-Periode auf 20 ms (50 Hz).
- `servo_winkel(grad)` rechnet 0..180 Grad in einen `write_analog`-Wert um
  (26 ≈ 0.5 ms, 123 ≈ 2.4 ms) und gibt ihn auf `P0` aus.
- `button_a.was_pressed()` / `button_b.was_pressed()` liefern `True`, wenn der
  Knopf seit der letzten Abfrage gedrueckt wurde.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: zwei-stellungen  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A faehrt den Servo auf 0 Grad, Knopf B auf 180 Grad.
#       Beim Start steht der Servo auf 90 Grad (Mitte).
#       Anwendung: Klappe / Schranke / Schalter auf-zu.
#
# --------------------------------------------------------------------------
# Verkabelung (3-poliges Servokabel)
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V     (siehe Hinweis unten!)
#   Servo braun/schwarz (-)      ->  GND
#
#   HINWEIS ZUR STROMVERSORGUNG:
#   Ein einzelner unbelasteter 9g-Servo laeuft meist direkt am 3V-Pin.
#   Zittert der Servo, macht der micro:bit einen Reset oder haengen mehrere
#   Servos dran -> externes Batteriefach (3x AA = 4.5 V) an rot/braun,
#   und GND von Batterie und micro:bit VERBINDEN (gemeinsame Masse).
#   Signal bleibt an P0.
# --------------------------------------------------------------------------

from microbit import *

# PWM fuer den Servo vorbereiten: 20 ms Periode = 50 Hz
pin0.set_analog_period(20)


def servo_winkel(grad):
    # grad 0..180 in einen Puls von ca. 0.5 ms bis 2.4 ms umrechnen.
    # write_analog(0..1023) entspricht 0..20 ms Puls.
    #   26  -> ca. 0.5 ms  (0 Grad)
    #   123 -> ca. 2.4 ms  (180 Grad)
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)
    pin0.write_analog(duty)
    # Zittert der Servo an den Endlagen: 26/123 naeher zusammen holen,
    # z. B. 34 und 115.


servo_winkel(90)   # Startstellung: Mitte

while True:
    if button_a.was_pressed():
        servo_winkel(0)
        display.show("A")
    if button_b.was_pressed():
        servo_winkel(180)
        display.show("B")
    sleep(10)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: Servo dreht in die Mitte (90 Grad)
- Knopf A -> Servo dreht auf 0 Grad, Matrix zeigt "A"
- Knopf B -> Servo dreht auf 180 Grad, Matrix zeigt "B"

## Moegliche Erweiterungen

- Nur ein Knopf, der zwischen zwei Stellungen umschaltet (Toggle)
- Servo langsam statt sofort in die Zielstellung fahren
- Endstellungen an dein Bauteil anpassen (z. B. 20 und 160 Grad)
