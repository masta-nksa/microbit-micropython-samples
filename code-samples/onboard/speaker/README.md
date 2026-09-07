# Lautsprecher (nur V2)

Der micro:bit V2 hat einen kleinen Lautsprecher auf der Rueckseite. Drei
Wege, Klang zu erzeugen:

- `music` - Toene und Melodien (Noten, Frequenzen, fertige Stuecke)
- `audio` - kurze Soundeffekte (`Sound.GIGGLE`, `Sound.HAPPY`, ...)
- `speech` - Sprachausgabe (englische Aussprache)

Eigenschaften:

- Eingebaut, kein Aufbau noetig
- Nur micro:bit **V2** (bei V1: Kopfhoerer/Lautsprecher an P0 + GND)
- `pin=None` bei `music.pitch(...)` -> Ton nur ueber den eingebauten Lautsprecher

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `music.pitch(440, 300)` | 440 Hz fuer 300 ms |
| `music.play(music.NYAN)` | fertige Melodie abspielen |
| `music.play(["c4:4", "e4", "g4"])` | eigene Notenfolge |
| `audio.play(Sound.GIGGLE)` | Soundeffekt (V2) |
| `speech.say("hello")` | Sprachausgabe (`import speech`) |

## Samples (Lernreihenfolge)

1. [melodie-und-sound/](melodie-und-sound/) - A spielt eine Melodie, B einen Soundeffekt, Logo einen Ton
