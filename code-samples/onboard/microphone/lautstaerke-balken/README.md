# lautstaerke-balken

Bauteil: [Mikrofon (V2)](../README.md) · Kategorie: onboard

Die LED-Matrix zeigt die Lautstaerke als Balken von unten nach oben.
Reden = ein paar Reihen, Klatschen = volle Matrix.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit **V2**.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Nur micro:bit V2 (V1 hat kein Mikrofon).
Bei aktiver Messung leuchtet die kleine Mikrofon-LED auf der Vorderseite.

## Wie der Code funktioniert

- `microphone.sound_level()` liefert die Lautstaerke als Zahl **0..255**.
- `pegel // 51` rechnet das in 0..5 leuchtende Reihen um (255 // 51 = 5).
- Die Matrix wird Zeile fuer Zeile gefuellt: `y = 0` ist oben, `y = 4` unten,
  darum die Bedingung `(5 - y) <= reihen` (von unten her).
- `display.clear()` vor jedem Neuzeichnen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: lautstaerke-balken  (eingebautes Mikrofon, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Die LED-Matrix zeigt die aktuelle Lautstaerke als Balken, der von
#       unten nach oben waechst. Leise = eine Reihe, laut (z. B. Klatschen)
#       = die ganze Matrix.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - das Mikrofon ist beim micro:bit V2 eingebaut
#   (kleines Loch auf der Vorderseite, daneben die Mikrofon-LED).
# --------------------------------------------------------------------------

from microbit import *

while True:
    # sound_level(): aktuelle Lautstaerke als Zahl 0..255
    pegel = microphone.sound_level()

    # In 0..5 leuchtende Reihen umrechnen
    reihen = min(5, pegel // 51)

    display.clear()
    for y in range(5):
        # y = 0 ist oben, y = 4 unten -> von unten her fuellen
        if (5 - y) <= reihen:
            for x in range(5):
                display.set_pixel(x, y, 9)

    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Stille -> Matrix fast dunkel (0..1 Reihen)
- normales Reden -> 2..3 Reihen
- Klatschen / lautes Rufen -> volle Matrix

## Moegliche Erweiterungen

- `microphone.was_event(SoundEvent.LOUD)`: bei Klatschen ein Licht ein-/ausschalten
- den Hoechstwert kurz "stehen" lassen (Peak-Anzeige)
- Klatsch-Zaehler: bei jedem lauten Ereignis +1
