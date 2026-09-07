# servo

Servomotoren - per PWM-Signal auf einen Winkel gestellt.

## Bauteile

| Bauteil | Typ | Samples | Hardware |
|---------|-----|---------|----------|
| [miuzei-9g-servo/](miuzei-9g-servo/) | Micro-Servo 9g, Metallgetriebe, ~0..180 Grad | zwei-stellungen, sweep, winkel-mit-encoder | [hardware](../../hardware/servo/miuzei-9g-servo/) |

## Grundlagen

- PWM: `pin0.set_analog_period(20)` (20 ms = 50 Hz), dann `pin0.write_analog(duty)`
  mit `duty` von ca. 26 (0.5 ms, 0 Grad) bis 123 (2.4 ms, 180 Grad).
- Stromversorgung: einzelner unbelasteter Servo geht am `3V`-Pin; unter Last
  oder bei mehreren Servos externes Batteriefach (4.5-6 V) mit **gemeinsamer
  Masse** verwenden.
