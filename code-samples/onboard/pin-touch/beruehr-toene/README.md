# beruehr-toene

Bauteil: [Pins P0/P1/P2 als Beruehrungssensor](../README.md) · Kategorie: onboard

Ein winziges Klavier: **P0** antippen = tiefer Ton, **P1** = mittel, **P2** = hoch.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit **V2**.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Beim V2 sind P0/P1/P2 kapazitiv - Finger aufs
Pad reicht. Fuer ein echtes Fruechte-Klavier: Krokoklemmen von P0/P1/P2 an je
ein Stueck Obst, eine weitere Klemme von GND selbst festhalten (dann wird es
zu einem `input/`-Aufbau).

## Wie der Code funktioniert

- `toene` ist eine Liste von Paaren `(pin, frequenz)`. Die `for`-Schleife
  prueft alle drei Pins der Reihe nach.
- `pin.is_touched()` ist beim V2 kapazitiv: es misst, wie viel Ladung der
  Finger aufnimmt - kein GND-Kontakt noetig.
- `music.pitch(frequenz, 150, pin=None)` spielt den Ton 150 ms lang ueber den
  eingebauten Lautsprecher. `pin=None` ist wichtig, sonst wuerde `music`
  versuchen, ueber `P0` auszugeben - genau den Pin, den wir abfragen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: beruehr-toene  (Pins P0/P1/P2 als Beruehrungssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein winziges Klavier. P0 antippen spielt einen tiefen Ton, P1 einen
#       mittleren, P2 einen hohen. Der Ton laeuft ueber den eingebauten
#       Lautsprecher (V2).
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - beim micro:bit V2 sind P0/P1/P2 kapazitive
#   Beruehrungssensoren. Einfach mit dem Finger auf das Pad tippen.
#   (Fuers "Fruechte-Klavier": Krokoklemmen von P0/P1/P2 an je ein Stueck
#    Obst, eine weitere Klemme von GND selbst festhalten.)
# --------------------------------------------------------------------------

from microbit import *
import music

# Pin -> Tonhoehe (Hz)
toene = [(pin0, 262), (pin1, 330), (pin2, 392)]   # c', e', g'

while True:
    for pin, frequenz in toene:
        if pin.is_touched():
            music.pitch(frequenz, 150, pin=None)   # pin=None -> interner Lautsprecher

    sleep(20)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- P0 antippen -> tiefer Ton (c')
- P1 -> mittlerer Ton (e')
- P2 -> hoher Ton (g')
- zusammen ergibt sich ein C-Dur-Dreiklang

## Moegliche Erweiterungen

- beim Ton das passende Bild / einen Buchstaben zeigen
- eine kleine Melodie vorgeben, die nachgespielt werden soll (Simon-Says)
- mit Krokoklemmen an Obst zum Fruechte-Klavier ausbauen
