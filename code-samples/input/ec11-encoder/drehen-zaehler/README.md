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

## Code

Siehe [`main.py`](main.py).

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
