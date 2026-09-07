# Beschleunigungssensor

Misst die Beschleunigung in drei Achsen (X quer, Y laengs, Z senkrecht zur
Platine). Im Ruhezustand misst er nur die Erdanziehung - daraus laesst sich
die **Lage** (Neigung) ableiten. Ausserdem erkennt er fertige **Gesten** wie
Schuetteln oder Kippen.

- Eingebaut, kein Aufbau noetig
- `accelerometer` - Objekt, immer verfuegbar

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `accelerometer.get_x()` | Beschleunigung X in Milli-g (ca. -1000..1000 bei Neigung, -2000..2000 max) |
| `accelerometer.get_y()` / `get_z()` | dasselbe fuer Y- und Z-Achse |
| `accelerometer.get_values()` | Tupel `(x, y, z)` auf einmal |
| `accelerometer.was_gesture("shake")` | `True`, wenn seit dem letzten Aufruf geschuettelt wurde |
| `accelerometer.current_gesture()` | aktuelle Geste als Text |

Gesten: `"up"`, `"down"`, `"left"`, `"right"`, `"face up"`, `"face down"`,
`"freefall"`, `"3g"`, `"6g"`, `"8g"`, `"shake"`.

## Samples (Lernreihenfolge)

1. [wasserwaage/](wasserwaage/) - ein Leuchtpunkt zeigt die Neigung an
2. [shake-wuerfel/](shake-wuerfel/) - Schuetteln wuerfelt eine Zahl 1..6
