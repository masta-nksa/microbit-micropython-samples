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

## Code

Siehe [`main.py`](main.py).

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
