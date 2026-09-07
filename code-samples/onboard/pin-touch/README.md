# Pins P0/P1/P2 als Beruehrungssensor

Die drei grossen Pins am unteren Rand koennen Beruehrung erkennen. Beim
**V2** arbeiten sie standardmaessig **kapazitiv** - ein Finger auf dem Pad
reicht, ohne dass man GND anfassen muss.

- Kein Bauteil noetig; fuer ein "Fruechte-Klavier" spaeter Krokoklemmen an
  Obst -> gehoert dann eher zu [`../../input/`](../../input/)
- `pin0`, `pin1`, `pin2` - immer verfuegbar

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `pin0.is_touched()` | `True`, solange `P0` beruehrt wird |
| `pin0.set_touch_mode(pin0.CAPACITIVE)` | kapazitiv (V2-Standard) - ohne GND |
| `pin0.set_touch_mode(pin0.RESISTIVE)` | resistiv - Finger muss auch GND beruehren (V1-Verhalten) |

## Samples (Lernreihenfolge)

1. [beruehr-toene/](beruehr-toene/) - P0/P1/P2 antippen spielt je einen Ton
