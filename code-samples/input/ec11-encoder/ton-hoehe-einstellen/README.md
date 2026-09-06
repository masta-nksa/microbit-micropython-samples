# ton-hoehe-einstellen

Bauteil: [EC11 Rotary Encoder](../README.md) · Kategorie: input

Kombiniert Drehen und Druck: am Knopf drehen aendert die **Tonhoehe** eines
Dauertons (200..2000 Hz), auf den Knopf druecken schaltet den Ton **an oder
aus**.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Rotary Encoder **EC11** (mit Push) |
| 1 | Steckbrett |
| 5 | Jumperkabel |

## Verkabelung

Identisch zu [drehen-und-druck](../drehen-und-druck/README.md#verkabelung):

```
   P0 -> A (CLK)     GND -> C (COM)     P1 -> B (DT)
   P2 -> SW 1        GND -> SW 2
```

Ton laeuft ueber den eingebauten Lautsprecher (`pin=None`), `P0` bleibt frei.

**CLK und DT (Pin A/B) sind vertauschbar** - Details siehe
[Bauteil-README](../README.md#clk-und-dt-sind-vertauschbar). Falsch herum:
`P0` und `P1` tauschen.

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Code

Siehe [`main.py`](main.py).

| Teil | Aufgabe |
|------|---------|
| Drehen | `frequenz` +/- 20 Hz pro Raste, begrenzt auf 200..2000 Hz |
| Druck (Flanke) | `ton_an` umschalten |
| `ton_aktualisieren()` | setzt den Dauerton neu (`music.pitch(f, -1, pin=None, wait=False)`) oder `music.stop()` |

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Knopf druecken -> Ton startet (Note-Symbol), nochmal druecken -> Ton aus (X-Symbol)
- Waehrend der Ton laeuft: drehen aendert hoerbar die Tonhoehe

## Moegliche Erweiterungen

- Frequenz in eine Tonleiter "einrasten" (nur echte Noten)
- Zweiter Encoder fuer die Lautstaerke (`volume()`)
- Aktuelle Frequenz als Balken auf der LED-Matrix
