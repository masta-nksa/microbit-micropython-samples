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

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Code

Siehe [`main.py`](main.py). Zwei Dinge in einer Schleife:

| Teil | Aufgabe |
|------|---------|
| Drehen | fallende Flanke an CLK -> `zaehler` +/- 1 (auf 0..9 begrenzt) |
| Druck (Flanke) | `zaehler = 0`, kurzer Ton `music.pitch(660, 80, pin=None)` |

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Drehen -> Ziffer 0..9 aendert sich
- Knopf druecken -> Ziffer springt auf 0, kurzer Ton

## Moegliche Erweiterungen

- Kurzer Druck = Reset, langer Druck = andere Funktion
- Druck schaltet zwischen zwei Modi um (z. B. Schrittweite 1 oder 5)
