# melodie-und-sound

Bauteil: [Lautsprecher (V2)](../README.md) · Kategorie: onboard

Drei Wege zum Klang: **A** spielt eine Melodie, **B** einen Soundeffekt,
das **goldene Logo** einen einzelnen Ton.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit **V2**.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Lautsprecher auf der Rueckseite (nur V2).
Bei V1: Kopfhoerer/Lautsprecher an P0 + GND.

## Wie der Code funktioniert

- `import music` und `import audio` - zwei getrennte Module.
- `music.play(music.NYAN)` spielt ein fertiges Stueck. Eigene Noten gehen mit
  `music.play(["c4:4", "e4", "g4"])`.
- `audio.play(Sound.GIGGLE)` spielt einen der fertigen V2-Soundeffekte
  (`Sound.HAPPY`, `Sound.SAD`, `Sound.HELLO`, ...).
- `music.pitch(880, 200)` = 880 Hz fuer 200 ms. Ohne `pin=`-Angabe laeuft der
  Ton ueber den eingebauten Lautsprecher.
- `pin_logo.is_touched()` erkennt die Beruehrung des goldenen Logos (V2).

Alle drei blockieren kurz, solange sie spielen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: melodie-und-sound  (eingebauter Lautsprecher, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Drei Arten, Klang zu erzeugen:
#       Knopf A  -> fertige Melodie (music)
#       Knopf B  -> Soundeffekt (audio)
#       Logo     -> einzelner Ton (music.pitch)
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Lautsprecher (V2) sitzt auf der Rueckseite.
#   Bei V1 stattdessen Kopfhoerer/Lautsprecher an P0 + GND.
# --------------------------------------------------------------------------

from microbit import *
import music
import audio

display.show(Image.MUSIC_QUAVER)

while True:
    if button_a.was_pressed():
        music.play(music.NYAN)          # fertige Melodie

    if button_b.was_pressed():
        audio.play(Sound.GIGGLE)        # Soundeffekt (nur V2)

    if pin_logo.is_touched():           # goldenes Logo beruehren (V2)
        music.pitch(880, 200)           # 880 Hz fuer 200 ms

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- A -> die "Nyan Cat"-Melodie
- B -> ein kurzer Lach-Effekt
- Logo antippen -> ein hoher Piepton

## Moegliche Erweiterungen

- `import speech` und `speech.say("hello micro bit")` - Sprachausgabe
- eigene Melodie aus Noten zusammenbauen
- Lautstaerke mit `music.set_volume(0..255)` einstellen
