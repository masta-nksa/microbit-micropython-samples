# Funk (radio)

Der micro:bit kann per 2,4-GHz-Funk **direkt mit anderen micro:bits** reden -
ohne WLAN, ohne Kopplung. Alle Boards mit derselben **Gruppe** (0..255) hoeren
sich gegenseitig.

- Eingebaut, kein Aufbau noetig - aber **zwei micro:bits** (oder mehr)
- `radio` - eigenes Modul, `import radio`
- Radio und Bluetooth koennen nicht gleichzeitig laufen (im Editor kein Problem)

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `radio.on()` | Funk einschalten (am Anfang noetig) |
| `radio.config(group=23)` | Gruppe waehlen - nur gleiche Gruppe hoert mit |
| `radio.send("text")` | Zeichenkette an alle in der Gruppe senden |
| `radio.receive()` | naechste empfangene Nachricht als Text, oder `None` |

## Samples (Lernreihenfolge)

1. [senden-empfangen/](senden-empfangen/) - dasselbe Programm auf beiden Boards: Knopf A schickt eine Zahl, das andere Board zeigt sie
