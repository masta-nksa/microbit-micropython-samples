# drehen-zaehler

Bauteil: [EC11 Rotary Encoder](../README.md) · Kategorie: input

Am Drehknopf drehen -> ein Wert 0..9 wird groesser bzw. kleiner, die
LED-Matrix zeigt die aktuelle Ziffer. Der Taster im Knopf wird hier noch
nicht benutzt.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Rotary Encoder **EC11** (Standard-Bauform, mit Push) |
| 1 | Steckbrett |
| 3 | Jumperkabel |

## Verkabelung

```
   micro:bit            EC11 (nur Encoder-Seite)
  +---------+        +----------+
  |      P0 |--------| A  (CLK) |
  |     GND |--------| C  (COM) |
  |      P1 |--------| B  (DT)  |
  +---------+        +----------+
```

Interne Pull-ups fuer `P0` und `P1` per Code.

**CLK und DT (Pin A und Pin B) sind vertauschbar.** Die beiden Drehsignale
sind gleichwertig und je nach Encoder anders beschriftet - die Schaltung
funktioniert so oder so. Vertauscht man sie, dreht sich nur die
**Zaehlrichtung** um. Dreht der Zaehler also falsch herum: `P0` und `P1`
tauschen (oder im Code `+= 1` / `-= 1` vertauschen). Getestet: funktioniert.

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- Pull-ups fuer `P0` (CLK) und `P1` (DT) per Code.
- Die Schleife pollt `P0`. Bei einer **fallenden Flanke** (`clk` wechselt von
  1 auf 0 = eine Raste) entscheidet der Zustand von `P1` die Richtung:
  `P1 == 1` -> hoch, sonst runter.
- `wert` wird mit `max(0, min(9, wert))` auf 0..9 begrenzt und als Ziffer
  angezeigt. `print()` schreibt den Wert zusaetzlich auf die serielle Konsole.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: drehen-zaehler  (EC11 Rotary Encoder mit Push)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Am Drehknopf drehen -> ein Wert 0..9 wird groesser / kleiner.
#       Die LED-Matrix zeigt die aktuelle Ziffer. Der Taster wird hier
#       noch nicht benutzt (siehe Sample "drehen-und-druck").
#
# --------------------------------------------------------------------------
# Verkabelung (EC11, Standard-Bauform)
# --------------------------------------------------------------------------
#   Encoder-Seite (3 Pins):
#     Pin A  (CLK)  ->  P0
#     Pin C  (COM)  ->  GND      (mittlerer Pin)
#     Pin B  (DT)   ->  P1
#
#   Taster-Seite (2 Pins):  hier noch nicht angeschlossen
#
#   Interne Pull-ups fuer P0 und P1 werden per Code aktiviert.
#   Hinweis: Pin A (CLK) und Pin B (DT) sind gleichwertig und je nach
#            Encoder anders beschriftet - die Schaltung geht so oder so.
#            Vertauscht man sie, dreht sich nur die Zaehlrichtung um.
#            Dreht der Zaehler falsch herum -> P0 und P1 tauschen
#            (oder unten die +1 / -1 vertauschen).
# --------------------------------------------------------------------------

from microbit import *

pin0.set_pull(pin0.PULL_UP)   # CLK
pin1.set_pull(pin1.PULL_UP)   # DT

wert = 0
letzter_clk = pin0.read_digital()

display.show(str(wert))

while True:
    clk = pin0.read_digital()

    # Nur bei einer fallenden Flanke an CLK zaehlen = eine Raste pro Schritt
    if clk != letzter_clk and clk == 0:
        if pin1.read_digital() == 1:
            wert = wert + 1     # im Uhrzeigersinn
        else:
            wert = wert - 1     # gegen den Uhrzeigersinn

        # Auf den Bereich 0..9 begrenzen
        wert = max(0, min(9, wert))
        display.show(str(wert))
        print("Wert:", wert)

    letzter_clk = clk
    sleep(1)   # kurze Pause, damit der Pin nicht zu schnell gelesen wird
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Knopf im Uhrzeigersinn drehen -> Ziffer zaehlt hoch (max. 9)
- gegen den Uhrzeigersinn -> Ziffer zaehlt runter (min. 0)
- **Open Serial** im Editor zeigt zusaetzlich `Wert: ...`

## Moegliche Erweiterungen

- Wertebereich vergroessern und die Zahl mit `display.scroll()` anzeigen
- Wert als Balken (0..9 LEDs) statt als Ziffer darstellen
- Zwei Encoder = zwei unabhaengige Werte
