# logo-schalter

Bauteil: [Touch-Logo (V2)](../README.md) · Kategorie: onboard

Das goldene Logo als Lichtschalter: antippen -> Herz an, nochmal antippen
-> Herz aus.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit **V2**.2 |

## Hardware

Eingebaut, kein Aufbau noetig. Nur micro:bit V2.

## Wie der Code funktioniert

- `pin_logo.is_touched()` ist `True`, **solange** das Logo beruehrt wird.
- Damit ein Antippen nur **einmal** umschaltet, merkt sich der Code mit
  `war_beruehrt` den letzten Zustand und reagiert nur auf die **Flanke**
  (nicht beruehrt -> beruehrt).
- `an = not an` kippt den Wahrheitswert - das ist der Umschalter (Toggle).
- `sleep(20)` entprellt die Beruehrung grob.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: logo-schalter  (Touch-Logo, nur V2)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Das goldene Logo wie einen Lichtschalter benutzen. Einmal antippen
#       -> Herz an. Nochmal antippen -> Herz aus. (Umschalter / Toggle)
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - das Logo ist beim micro:bit V2 ein Beruehrungssensor.
# --------------------------------------------------------------------------

from microbit import *

an = False              # aktueller Zustand
war_beruehrt = False    # Zustand im letzten Durchlauf

while True:
    beruehrt = pin_logo.is_touched()

    # Nur auf die Flanke reagieren: gerade eben angetippt
    if beruehrt and not war_beruehrt:
        an = not an     # umschalten
        if an:
            display.show(Image.HEART)
        else:
            display.clear()

    war_beruehrt = beruehrt
    sleep(20)           # kurze Pause = einfache Entprellung
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: Matrix dunkel
- Logo antippen -> Herz
- Logo nochmal antippen -> dunkel

## Moegliche Erweiterungen

- langes Halten (mit `running_time()` messen) = andere Funktion
- drei Zustaende durchschalten: aus -> Herz -> Smiley -> aus
- Logo + Knopf A gleichzeitig als "Geheim-Kombination"
