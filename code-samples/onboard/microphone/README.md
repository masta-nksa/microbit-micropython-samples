# Mikrofon (nur V2)

Der micro:bit V2 hat ein Mikrofon auf der Vorderseite (kleines Loch neben dem
Logo, daneben eine rote LED, die bei aktiver Messung leuchtet). Es liefert
einen **Lautstaerkewert** und erkennt laute/leise **Ereignisse**.

- Eingebaut, kein Aufbau noetig
- Nur micro:bit **V2** (V1 hat kein Mikrofon)
- `microphone` und `SoundEvent` - verfuegbar ueber `from microbit import *`

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `microphone.sound_level()` | aktuelle Lautstaerke als Zahl **0..255** |
| `microphone.was_event(SoundEvent.LOUD)` | `True`, wenn es seit dem letzten Aufruf laut wurde |
| `microphone.was_event(SoundEvent.QUIET)` | dasselbe fuer "wieder leise" |
| `microphone.current_event()` | aktuelles Ereignis: `SoundEvent.LOUD` oder `SoundEvent.QUIET` |

## Samples (Lernreihenfolge)

1. [lautstaerke-balken/](lautstaerke-balken/) - die Matrix zeigt die Lautstaerke als Balken
