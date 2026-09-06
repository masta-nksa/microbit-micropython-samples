# ton-solange-gedrueckt

Bauteil: [DS425 Pushbutton](../README.md) · Kategorie: input

Der Ton erklingt **durchgehend, solange der Taster gehalten wird**.
Loslassen -> Ton sofort aus. Aufbauend auf [ton-bei-druck](../ton-bei-druck/).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Pushbutton Switch **DS425 Momentary** |
| 1 | Steckbrett |
| 2 | Jumperkabel bzw. Krokoklemmen |

Masse fuers CAD: [../../../../hardware/input/ds425-pushbutton/](../../../../hardware/input/ds425-pushbutton/)

## Verkabelung

Identisch zu [ton-bei-druck](../ton-bei-druck/README.md#verkabelung):

```
   micro:bit                         DS425 (Momentary)
  +---------+                       +---------------+
  |      P0 |-----------------------| Bein A (Seite 1)
  |     GND |-----------------------| Bein B (Seite 2)
  +---------+                       +---------------+
```

Diagonal gegenueberliegende Beine. Kein externer Widerstand - Pull-up per Code.

## Foto der Verkabelung

Foto nach dem Test in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

| Ereignis | Aktion |
|----------|--------|
| Taster gedrueckt (Flanke) | `music.pitch(440, -1, pin=None, wait=False)` -> Dauerton startet |
| Taster losgelassen (Flanke) | `music.stop()` -> Ton endet |

- `duration=-1`: der Ton spielt endlos, bis `music.stop()` aufgerufen wird.
- `wait=False`: der Ton laeuft im Hintergrund, die Schleife arbeitet weiter
  und kann so das Loslassen erkennen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: ton-solange-gedrueckt  (DS425 Pushbutton)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Der Ton erklingt genau so lange, wie der Taster gedrueckt gehalten wird.
#       Loslassen -> Ton aus.
#
# --------------------------------------------------------------------------
# Verkabelung (identisch zu Sample "ton-bei-druck")
# --------------------------------------------------------------------------
#   Taster-Bein 1  ->  Pin  P0
#   Taster-Bein 2  ->  Pin  GND
#
#   Interner Pull-up von P0 aktiv:
#     - losgelassen:  P0 = 1
#     - gedrueckt:    P0 = 0
# --------------------------------------------------------------------------

from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)

war_gedrueckt = False

while True:
    gedrueckt = (pin0.read_digital() == 0)

    if gedrueckt and not war_gedrueckt:
        # Flanke: gerade gedrueckt -> Dauerton starten
        # duration=-1  -> spielt endlos weiter
        # wait=False   -> Programm laeuft weiter (Ton im Hintergrund)
        # pin=None     -> nur ueber den eingebauten Lautsprecher (V2)
        music.pitch(440, -1, pin=None, wait=False)
        display.show(Image.MUSIC_QUAVER)

    elif not gedrueckt and war_gedrueckt:
        # Flanke: gerade losgelassen -> Ton stoppen
        music.stop()
        display.clear()

    war_gedrueckt = gedrueckt
    sleep(10)   # kurze Pause = einfache Entprellung
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Taster druecken und halten -> Note-Symbol auf der Matrix + Dauerton (440 Hz)
- Taster loslassen -> Matrix aus, Ton stoppt sofort

## Moegliche Erweiterungen

- Tonhoehe von einem Poti an `P1` abhaengig machen
- Mehrere Taster = mehrere Toene (kleine Orgel)
- Beim Halten die Tonhoehe langsam ansteigen lassen
