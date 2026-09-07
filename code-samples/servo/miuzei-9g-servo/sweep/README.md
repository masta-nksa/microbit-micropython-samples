# sweep

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Der Servo faehrt langsam von 0 bis 180 Grad und wieder zurueck - endlos.
Knopf **A** haelt die Bewegung an und startet sie wieder.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe) |
| 3 | Jumperkabel |
| — | optional: Batteriefach 3x AA |

Masse fuers CAD: [../../../../hardware/servo/miuzei-9g-servo/](../../../../hardware/servo/miuzei-9g-servo/)

## Verkabelung

Identisch zu [zwei-stellungen](../zwei-stellungen/README.md#verkabelung):

```
   P0  -> Signal (orange/gelb)
   3V  -> +      (rot)
   GND -> -      (braun/schwarz)
```

Mit externer Batteriebox (3x 1.5 V) statt `3V`: `+` der Box an Servo rot,
`-` der Box an Servo braun **und** an micro:bit `GND`, Signal an `P0`, `3V`
frei lassen. Details: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `winkel` wird pro Durchlauf um 5 Grad veraendert, `richtung` (+1 / -1) kehrt
  sich an den Enden (0 und 180) um.
- `sleep(40)` bestimmt das Tempo: groesser = langsamer.
- `button_a.was_pressed()` schaltet die Variable `laeuft` um; ist sie `False`,
  wird kein neuer Winkel gesetzt.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: sweep  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Der Servo faehrt langsam von 0 bis 180 Grad und wieder zurueck.
#       Knopf A haelt die Bewegung an bzw. startet sie wieder.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie Sample "zwei-stellungen")
# --------------------------------------------------------------------------
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  3V   (bei Zittern/Reset: externes 4.5-V-Fach,
#                                          GND gemeinsam mit dem micro:bit)
#   Servo braun/schwarz (-)      ->  GND
# --------------------------------------------------------------------------

from microbit import *

pin0.set_analog_period(20)   # 20 ms = 50 Hz


def servo_winkel(grad):
    grad = max(0, min(180, grad))
    duty = int(26 + grad * (123 - 26) / 180)   # ca. 0.5 ms .. 2.4 ms
    pin0.write_analog(duty)


winkel = 0
richtung = 1        # +1 = aufwaerts, -1 = abwaerts
laeuft = True

servo_winkel(winkel)

while True:
    # Knopf A: Bewegung an / aus
    if button_a.was_pressed():
        laeuft = not laeuft
        display.show(Image.ARROW_E if laeuft else Image.SQUARE_SMALL)
        sleep(200)
        display.clear()

    if laeuft:
        winkel = winkel + richtung * 5     # Schrittweite 5 Grad
        if winkel >= 180:
            winkel = 180
            richtung = -1
        elif winkel <= 0:
            winkel = 0
            richtung = 1
        servo_winkel(winkel)

    sleep(40)   # bestimmt das Tempo der Bewegung
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Servo pendelt gleichmaessig zwischen 0 und 180 Grad
- Knopf A -> Bewegung stoppt (Quadrat-Symbol) bzw. laeuft weiter (Pfeil)

## Moegliche Erweiterungen

- Tempo mit Knopf B umschalten (schnell / langsam)
- Nur einen Teilbereich abfahren (z. B. 60..120 Grad)
- Am Umkehrpunkt kurz warten
