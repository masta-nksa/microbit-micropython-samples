# Knoepfe A und B

Zwei Taster links und rechts der LED-Matrix, fest eingebaut. Das goldene
Logo (V2) wirkt wie ein dritter Knopf - dazu [touch-logo/](../touch-logo/).

- Eingebaut, kein Aufbau noetig
- `button_a` / `button_b` - Objekte, immer verfuegbar (`from microbit import *`)

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `button_a.is_pressed()` | `True`, solange der Knopf **jetzt** gedrueckt ist |
| `button_a.was_pressed()` | `True`, wenn seit dem letzten Aufruf gedrueckt wurde (Flanke, gepuffert) |
| `button_a.get_presses()` | Anzahl Druecke seit dem letzten Aufruf, setzt den Zaehler zurueck |

`was_pressed()` ist meistens die richtige Wahl: kein Prellen, kein
Dauerfeuer beim Halten.

## Samples (Lernreihenfolge)

1. [a-b-zaehler/](a-b-zaehler/) - A zaehlt hoch, B runter, A+B setzt auf 0
