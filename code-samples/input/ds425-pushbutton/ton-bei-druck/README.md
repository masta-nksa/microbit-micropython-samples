# ton-bei-druck

Bauteil: [DS425 Pushbutton](../README.md) · Kategorie: input

Beim Druecken zeigt die LED-Matrix ein Herz und der eingebaute Lautsprecher
gibt einen kurzen Ton aus. Loslassen -> Matrix aus.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Pushbutton Switch **DS425 Momentary** |
| 1 | Steckbrett |
| 2 | Jumperkabel bzw. Krokoklemmen |

Masse fuers CAD: [../../../../hardware/input/ds425-pushbutton/](../../../../hardware/input/ds425-pushbutton/)

## Verkabelung

```
   micro:bit                         DS425 (Momentary)
  +---------+                       +---------------+
  |      P0 |-----------------------| Bein A (Seite 1)
  |     GND |-----------------------| Bein B (Seite 2)
  +---------+                       +---------------+

  losgelassen: P0 = 1  (interner Pull-up zieht auf 3V)
  gedrueckt:   P0 = 0  (Taster verbindet P0 mit GND)
```

**Wichtig zum DS425:** 4 Beine, je zwei gegenueberliegende sind fest verbunden.
Beim Druecken werden die beiden Seiten kurzgeschlossen. Deshalb je ein Bein von
zwei gegenueberliegenden Seiten verwenden (diagonal). Kein externer Widerstand -
der Pull-up wird im Code mit `pin0.set_pull(pin0.PULL_UP)` aktiviert.

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `pin0.set_pull(pin0.PULL_UP)` schaltet den internen Pull-up ein -> `P0` ist
  im Ruhezustand `1`, beim Druecken `0`.
- Die Schleife merkt sich mit `war_gedrueckt` den letzten Zustand und reagiert
  nur auf die **Flanke** (Wechsel losgelassen -> gedrueckt), nicht auf das
  blosse Gedrueckt-Halten.
- `music.pitch(880, 120, pin=None)` spielt 880 Hz fuer 120 ms ueber den
  eingebauten Lautsprecher (`pin=None`), damit `P0` fuer den Taster frei bleibt.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: ton-bei-druck  (DS425 Pushbutton)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Ein externer Taster (Pushbutton Switch DS425 Momentary) wird ueber
#       die Pins mit dem micro:bit verbunden. Beim Druecken erscheint ein Herz
#       auf der LED-Matrix und es ertoent ein kurzer Ton.
#
# --------------------------------------------------------------------------
# Verkabelung
# --------------------------------------------------------------------------
#   Taster-Bein 1  ->  Pin  P0
#   Taster-Bein 2  ->  Pin  GND
#
#   Der DS425 hat 4 Beine. Je zwei gegenueberliegende Beine sind fest
#   miteinander verbunden. Beim Druecken werden die beiden Seiten verbunden.
#   -> Ein Bein einer Seite an P0, ein Bein der ANDEREN Seite an GND
#      (am besten diagonal gegenueberliegende Beine verwenden).
#
#   Es wird KEIN externer Widerstand benoetigt: der interne Pull-up-Widerstand
#   von P0 wird per Software eingeschaltet.
#     - Taster losgelassen:  P0 = 1  (High, ueber Pull-up an 3V)
#     - Taster gedrueckt:     P0 = 0  (Low, direkt an GND)
# --------------------------------------------------------------------------

from microbit import *
import music

# P0 als Eingang mit internem Pull-up-Widerstand konfigurieren.
# Ohne Pull-up "schwebt" der Pin und liefert zufaellige Werte.
pin0.set_pull(pin0.PULL_UP)

war_gedrueckt = False

while True:
    # Taster schliesst gegen GND -> gedrueckt entspricht dem Wert 0
    gedrueckt = (pin0.read_digital() == 0)

    if gedrueckt and not war_gedrueckt:
        # Flanke: gerade eben gedrueckt
        display.show(Image.HEART)
        # 880 Hz fuer 120 ms. pin=None -> Ton nur ueber den
        # eingebauten Lautsprecher des micro:bit V2 (P0 bleibt frei fuer den Taster).
        music.pitch(880, 120, pin=None)

    elif not gedrueckt and war_gedrueckt:
        # Flanke: gerade losgelassen
        display.clear()

    war_gedrueckt = gedrueckt
    sleep(10)   # kurze Pause = einfache Entprellung
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Taster druecken -> Herz auf der Matrix + Ton (880 Hz, kurz)
- Taster loslassen -> Matrix wird dunkel

## Moegliche Erweiterungen

- Zaehler, der bei jedem Druck hochzaehlt
- Zweiten Taster an `P1` fuer eine zweite Funktion
- Langes vs. kurzes Druecken unterscheiden
