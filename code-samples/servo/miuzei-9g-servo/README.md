# Miuzei Micro Servo 9g (Metallgetriebe)

Kleiner Hobby-Servo, SG90-kompatibel, aber mit Metallzahnraedern (robuster).
Stellbereich ca. 0..180 Grad. 3-poliges Kabel:

| Ader | Bedeutung | an den micro:bit |
|------|-----------|------------------|
| orange oder gelb | Signal (PWM) | `P0` |
| rot | Plus (+) | `3V` bzw. externes Batteriefach |
| braun oder schwarz | Minus (-) / GND | `GND` |

## Ansteuerung

Ein Servo wird ueber ein **PWM-Signal** gestellt: alle 20 ms ein Impuls,
dessen **Laenge** den Winkel bestimmt.

| Impulslaenge | Winkel |
|-------------|--------|
| ca. 0.5 ms | 0 Grad |
| ca. 1.5 ms | 90 Grad |
| ca. 2.4 ms | 180 Grad |

In MicroPython:

```python
pin0.set_analog_period(20)                 # 20 ms Periode = 50 Hz
pin0.write_analog(duty)                     # duty 0..1023 = 0..20 ms
```

`write_analog(26)` ergibt ca. 0.5 ms, `write_analog(123)` ca. 2.4 ms - dazwischen
linear. Zittert der Servo an den Endlagen, den Bereich etwas verkleinern
(z. B. 34..115).

## Stromversorgung - wichtig

- Ein **einzelner unbelasteter** 9g-Servo laeuft meist direkt am `3V`-Pin.
- Unter Last, bei mehreren Servos oder wenn der micro:bit **neu startet /
  der Servo zittert**: **externes Batteriefach** (3x AA = 4.5 V, oder
  4x AA = 6 V laut Servo-Datenblatt) an rot/braun.
- Dann **unbedingt GND von Batterie und micro:bit verbinden** (gemeinsame
  Masse), sonst kommt kein sauberes Signal an. Das Signal bleibt an `P0`.

## Samples (Lernreihenfolge)

1. [zwei-stellungen/](zwei-stellungen/) - Knopf A = 0 Grad, Knopf B = 180 Grad
2. [sweep/](sweep/) - faehrt langsam hin und her, Knopf A haelt an
3. [winkel-mit-encoder/](winkel-mit-encoder/) - Drehknopf (EC11) stellt den Winkel

Masse fuers CAD (spaeter): [../../../hardware/servo/miuzei-9g-servo/](../../../hardware/servo/miuzei-9g-servo/)
