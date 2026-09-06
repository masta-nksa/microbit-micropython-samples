# Aufgabe 2 - Ton solange der Taster gedrueckt wird

Erweiterung von [Aufgabe 1](../01-pushbutton/). Statt eines kurzen Tons beim
Druecken erklingt der Ton **durchgehend, solange der Taster gehalten wird**.
Loslassen -> Ton sofort aus.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Pushbutton Switch **DS425 Momentary** |
| 1 | Steckbrett |
| 2 | Jumperkabel bzw. Krokoklemmen |

## Verkabelung

Identisch zu Aufgabe 1:

```
   micro:bit                         DS425 (Momentary)
  +---------+                       +---------------+
  |      P0 |-----------------------| Bein A (Seite 1)
  |     GND |-----------------------| Bein B (Seite 2)
  +---------+                       +---------------+
```

Diagonal gegenueberliegende Beine verwenden. Kein externer Widerstand -
der Pull-up wird im Code mit `pin0.set_pull(pin0.PULL_UP)` aktiviert.

## Foto der Verkabelung

Foto nach dem Test in [`verkabelung/`](verkabelung/) ablegen und hier einbinden:

<!-- ![Verkabelung Aufgabe 2](verkabelung/foto.jpg) -->

## Code

Siehe [`main.py`](main.py). Kernidee:

| Ereignis | Aktion |
|----------|--------|
| Taster gedrueckt (Flanke) | `music.pitch(440, -1, pin=None, wait=False)` -> Dauerton startet |
| Taster losgelassen (Flanke) | `music.stop()` -> Ton endet |

- `duration=-1`: der Ton spielt endlos, bis `music.stop()` aufgerufen wird.
- `wait=False`: der Ton laeuft im Hintergrund, die Schleife arbeitet weiter
  und kann so das Loslassen erkennen.

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../docs/setup.md](../../docs/setup.md).

## Erwartetes Verhalten

- Taster druecken und halten -> Note-Symbol auf der Matrix + Dauerton (440 Hz)
- Taster loslassen -> Matrix aus, Ton stoppt sofort

## Moegliche Erweiterungen

- Tonhoehe von einem zweiten Eingang (Poti an `P1`) abhaengig machen
- Mehrere Taster = mehrere Toene (kleine Orgel)
- Beim Halten die Tonhoehe langsam ansteigen lassen
