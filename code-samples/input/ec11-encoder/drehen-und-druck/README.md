# drehen-und-druck

Bauteil: [EC11 Rotary Encoder](../README.md) · Kategorie: input

Wie [drehen-zaehler](../drehen-zaehler/), zusaetzlich der **Taster im Knopf**:
auf den Knopf druecken setzt den Zaehler zurueck auf 0 und gibt einen kurzen
Ton aus.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Rotary Encoder **EC11** (mit Push) |
| 1 | Steckbrett |
| 5 | Jumperkabel |

## Verkabelung

```
   micro:bit            EC11
  +---------+        +----------+
  |      P0 |--------| A  (CLK) |
  |     GND |--------| C  (COM) |
  |      P1 |--------| B  (DT)  |
  |      P2 |--------| SW 1     |
  |     GND |--------| SW 2     |
  +---------+        +----------+
```

Interne Pull-ups fuer `P0`, `P1`, `P2` per Code. Knopf gedrueckt -> `P2 = 0`.

**CLK und DT (Pin A und Pin B) sind vertauschbar** - die beiden Drehsignale
sind gleichwertig und je nach Encoder anders beschriftet. Vertauscht man sie,
dreht sich nur die Zaehlrichtung um. Falsch herum: `P0` und `P1` tauschen.
Die Taster-Pins sind davon nicht betroffen.

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

Zwei Dinge in einer Schleife:

| Teil | Aufgabe |
|------|---------|
| Drehen | fallende Flanke an CLK -> `zaehler` +/- 1 (auf 0..9 begrenzt) |
| Druck (Flanke) | `zaehler = 0`, kurzer Ton `music.pitch(660, 80, pin=None)` |

Der Druck wird - wie beim Pushbutton - ueber eine Flanke (`war_gedrueckt`)
erkannt, damit ein Reset nur einmal pro Druck ausgeloest wird.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: drehen-und-druck  (EC11 Rotary Encoder mit Push)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Drehen aendert einen Zaehler (0..9, LED-Matrix zeigt die Ziffer).
#       Auf den Knopf druecken -> Zaehler zurueck auf 0 + kurzer Ton.
#
# --------------------------------------------------------------------------
# Verkabelung (EC11, Standard-Bauform)
# --------------------------------------------------------------------------
#   Encoder-Seite (3 Pins):
#     Pin A  (CLK)  ->  P0
#     Pin C  (COM)  ->  GND      (mittlerer Pin)
#     Pin B  (DT)   ->  P1
#
#   Taster-Seite (2 Pins):
#     SW 1          ->  P2
#     SW 2          ->  GND
#
#   Interne Pull-ups fuer P0, P1 und P2 werden per Code aktiviert.
#     - Knopf losgelassen:  P2 = 1
#     - Knopf gedrueckt:     P2 = 0
#   Hinweis: Pin A (CLK) und Pin B (DT) sind gleichwertig / je nach Encoder
#            anders beschriftet. Vertauschen dreht nur die Zaehlrichtung um.
#            Dreht der Zaehler falsch herum -> P0 und P1 tauschen.
# --------------------------------------------------------------------------

from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)   # CLK
pin1.set_pull(pin1.PULL_UP)   # DT
pin2.set_pull(pin2.PULL_UP)   # SW (Taster im Knopf)

zaehler = 0
letzter_clk = pin0.read_digital()
war_gedrueckt = False

display.show(str(zaehler))

while True:
    # ----- Drehen auswerten -----
    clk = pin0.read_digital()
    if clk != letzter_clk and clk == 0:
        if pin1.read_digital() == 1:
            zaehler = zaehler + 1
        else:
            zaehler = zaehler - 1
        zaehler = max(0, min(9, zaehler))
        display.show(str(zaehler))
        print("Zaehler:", zaehler)
    letzter_clk = clk

    # ----- Druck auswerten (Flanke) -----
    gedrueckt = (pin2.read_digital() == 0)
    if gedrueckt and not war_gedrueckt:
        zaehler = 0
        music.pitch(660, 80, pin=None)
        display.show(str(zaehler))
        print("Reset")
    war_gedrueckt = gedrueckt

    sleep(1)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Drehen -> Ziffer 0..9 aendert sich
- Knopf druecken -> Ziffer springt auf 0, kurzer Ton

## Moegliche Erweiterungen

- Kurzer Druck = Reset, langer Druck = andere Funktion
- Druck schaltet zwischen zwei Modi um (z. B. Schrittweite 1 oder 5)
