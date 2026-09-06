# EC11 Rotary Encoder (mit Push)

Drehgeber mit Rastung und eingebautem Taster (auf die Welle druecken).
Beim Drehen liefert er zwei um 90 Grad versetzte Signale (CLK und DT) -
aus deren Reihenfolge ergibt sich die Drehrichtung. Typisch 20 Rasten
pro Umdrehung.

## Anschluss am micro:bit

```
   micro:bit            EC11
  +---------+        +----------+
  |      P0 |--------| A  (CLK) |
  |     GND |--------| C  (COM) |   <- mittlerer Pin der 3er-Seite
  |      P1 |--------| B  (DT)  |
  |      P2 |--------| SW 1     |   <- Taster-Seite (2 Pins)
  |     GND |--------| SW 2     |
  +---------+        +----------+
```

- Interne Pull-ups fuer `P0`, `P1`, `P2` werden im Code aktiviert
  (`pinX.set_pull(pinX.PULL_UP)`). Kein externer Widerstand noetig.
- **Dreht der Zaehler falsch herum:** `P0` und `P1` tauschen.
- Ton (in Sample 3) laeuft ueber den eingebauten Lautsprecher (`pin=None`),
  darum bleibt `P0` fuer den Encoder frei.
- Masse fuers CAD (spaeter): [../../../hardware/input/ec11-encoder/](../../../hardware/input/ec11-encoder/)

## So liest der Code den Drehgeber

Kein Interrupt - der micro:bit fragt die Pins in einer schnellen Schleife ab
(`sleep(1)`). Bei einer **fallenden Flanke an CLK** (eine Raste) sagt der
Zustand von DT die Richtung:

```python
if clk != letzter_clk and clk == 0:
    if pin1.read_digital() == 1:
        wert += 1      # im Uhrzeigersinn
    else:
        wert -= 1      # gegen den Uhrzeigersinn
```

Sehr schnelles Drehen kann einzelne Schritte verlieren - fuer Bedienzwecke
(Menue, Lautstaerke) reicht es problemlos.

## Samples (Lernreihenfolge)

1. [drehen-zaehler/](drehen-zaehler/) - Wert 0..9 per Drehen, Ziffer auf der Matrix
2. [drehen-und-druck/](drehen-und-druck/) - zusaetzlich: Knopf druecken setzt auf 0 zurueck
3. [ton-hoehe-einstellen/](ton-hoehe-einstellen/) - Drehen = Tonhoehe, Druck = Ton an/aus
