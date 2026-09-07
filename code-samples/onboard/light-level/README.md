# Umgebungslicht (LED-Matrix als Sensor)

Der micro:bit hat keinen eigenen Lichtsensor - er nutzt die **LEDs der Matrix
rueckwaerts** als Fotodioden. `display.read_light_level()` unterbricht die
Anzeige darum ganz kurz, um zu messen.

- Eingebaut, kein Aufbau noetig
- `display` - immer verfuegbar

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `display.read_light_level()` | Helligkeit der Umgebung als Zahl **0..255** (0 = dunkel) |

Der Wert schwankt und haengt vom Winkel ab - fuer "hell / dunkel" reicht er,
als Lux-Messgeraet nicht.

## Samples (Lernreihenfolge)

1. [nachtlicht/](nachtlicht/) - wird es dunkel, leuchtet die Matrix auf
