# Aufgabe 1 - Einfacher Pushbutton am Pin

Ein externer Taster wird ueber die Pins mit dem micro:bit verbunden.
Beim Druecken zeigt die LED-Matrix ein Herz und der eingebaute Lautsprecher
gibt einen kurzen Ton aus.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Pushbutton Switch **DS425 Momentary** (4-Bein-Taster, 6 mm) |
| 1 | Steckbrett (Breadboard) |
| 2 | Jumperkabel bzw. Krokoklemmen |

## Verkabelung

```
   micro:bit                         DS425 (Momentary)
  +---------+                       +---------------+
  |      P0 |-----------------------| Bein A        |
  |         |                       |   (Seite 1)   |
  |     GND |-----------------------| Bein B        |
  |         |                       |   (Seite 2)   |
  +---------+                       +---------------+

  losgelassen: P0 = 1  (interner Pull-up zieht auf 3V)
  gedrueckt:   P0 = 0  (Taster verbindet P0 mit GND)
```

**Wichtig zum DS425:** Der Taster hat 4 Beine. Je zwei gegenueberliegende
Beine sind fest verbunden. Beim Druecken werden die beiden Seiten kurz-
geschlossen. Deshalb **je ein Bein von zwei gegenueberliegenden Seiten**
verwenden (diagonal), nicht zwei Beine derselben Seite.

Ein externer Widerstand ist nicht noetig - der Pull-up wird im Code mit
`pin0.set_pull(pin0.PULL_UP)` aktiviert.

## Foto der Verkabelung

Nach dem Test ein Foto in [`verkabelung/`](verkabelung/) ablegen
(z. B. `verkabelung/foto.jpg`) und hier einbinden:

<!-- ![Verkabelung Aufgabe 1](verkabelung/foto.jpg) -->

## Code

Siehe [`main.py`](main.py).

## Auf den micro:bit uebertragen

Siehe [../../docs/setup.md](../../docs/setup.md). Kurz:

1. Editor oeffnen: <https://python.microbit.org/v/beta>
2. Inhalt von `main.py` in den Editor kopieren
3. micro:bit per USB anschliessen -> **Connect** -> **Send to micro:bit**

## Erwartetes Verhalten

- Taster druecken -> Herz auf der Matrix + Ton (880 Hz, kurz)
- Taster loslassen -> Matrix wird dunkel

## Moegliche Erweiterungen

- Statt Ton eine bestimmte LED oder ein Zaehler, der bei jedem Druck hochzaehlt
- Zweiten Taster an `P1` fuer eine zweite Funktion
- Langes vs. kurzes Druecken unterscheiden
