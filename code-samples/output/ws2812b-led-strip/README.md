# WS2812B LED-Strip (NeoPixel)

Adressierbarer RGB-LED-Streifen: jede LED (Chip **WS2812B**, Bauform 5050) hat
einen eigenen Controller und wird ueber **eine einzige Datenleitung** gesetzt.
Laut Beipackzettel: **DC 5 V**, ueber 5,5 V brennen die LEDs durch.

## Anschluesse am Strip

Der Strip hat **drei** Kontakte, an beiden Enden herausgefuehrt:

| Pad (Beschriftung auf der Platine) | Bedeutung |
|---|---|
| `5V` / `VCC` / `+` | Stromversorgung + |
| `GND` / `-` | Masse |
| `DIN` / `DI` / `DATA` / `SI` | Dateneingang |

- **Datenrichtung:** Auf dem Strip sind **Pfeile** aufgedruckt. Angeschlossen
  wird das Ende, wo die Pfeile **vom Anschluss weg** in den Strip zeigen
  (`DIN`). Am anderen Ende ist `DO` (Data Out) zum Weiterverbinden.
- **Kabelfarben pruefen, nicht raten.** Ueblich bei diesen Strips:
  rot = `5V`, gruen = `DIN`, weiss oder schwarz = `GND` - aber es zaehlt die
  **Pad-Beschriftung**, an die das Kabel geloetet ist.
- Steckverbinder: 3-poliger **JST-SM**. Die mitgelieferten Pigtails passen an
  die Buchse am Strip; die bunten Dupont-Kabel gehen an micro:bit-Pins bzw.
  Krokoklemmen.
- Der Strip kann an den markierten Stellen (Schere-Symbol) gekuerzt werden.

## Anschluss an den micro:bit

Der micro:bit kann den Strip **nicht** mit Strom versorgen: der `3V`-Pin hat
zu wenig Spannung **und** zu wenig Strom. Es braucht eine **externe 4,5-5 V
Quelle**.

Empfohlen fuer den Anfang die **Batteriebox 3x 1.5 V (= 4,5 V)** (die vom
Servo). 4,5 V sind fuer WS2812B ok und machen ausserdem das 3,3-V-Datensignal
des micro:bit zuverlaessig.

```
  Batteriebox 4.5V         LED-Strip (DIN-Ende, Pfeile zeigen in den Strip)
  ----------------         --------------------------------------------------
  rot  (+)  -------------->  5V / VCC / +
  schwarz (-) --+-------->   GND / -
                |
                +-------->   micro:bit  GND        (gemeinsame Masse - Pflicht!)
  micro:bit P0 ----------->  DIN / DI / DATA
```

Schritt fuer Schritt:

1. `+` der Box  ->  Strip `5V`
2. `-` der Box  ->  Strip `GND`
3. `-` der Box (oder Strip `GND`)  ->  micro:bit `GND`  (ohne diese Bruecke
   kommt kein sauberes Signal an)
4. micro:bit `P0`  ->  Strip `DIN`
5. micro:bit weiterhin per USB am Rechner. Box erst einschalten, wenn alles steckt.
6. **Niemals** `+` der Box an `3V` oder einen Pin. **Kein** 6-V-Fach (4x 1.5 V) -
   das brennt die LEDs.

### Statt der Box: das 5-V-Netzteil aus dem Set

Gleiche Verdrahtung, nur `5V` statt `4,5V`. Heller und fuer mehr LEDs geeignet.
Dann kann die **erste LED** wegen des 3,3-V-Signals zicken (Flackern, falsche
Farbe). Abhilfe: Strip mit 4,5 V betreiben, **330 Ohm** in Reihe in die
Datenleitung, oder einen Pegelwandler (74AHCT125) benutzen.

### Strom

Eine LED auf vollem Weiss zieht ~**60 mA**. Bei `ANZAHL` LEDs also bis zu
`ANZAHL x 60 mA` in der Spitze. Die 3x-AA-Box schafft locker ~8-15 LEDs bei
gedimmten Farben. In allen Beispielen sind die Farbwerte klein gehalten
(max ~60 statt 255).

## MicroPython

```python
import neopixel
np = neopixel.NeoPixel(pin0, ANZAHL)   # ANZAHL = Zahl der LEDs
np[0] = (rot, gruen, blau)             # je 0..255
np.show()                              # sendet die Daten an den Strip
np.clear()                             # alle aus (und sendet)
```

Die Reihenfolge GRB der WS2812B erledigt das Modul intern - du gibst `(r, g, b)`.

## Samples (Lernreihenfolge)

1. [erste-farben/](erste-farben/) - Strip zum Leuchten bringen, LEDs einfaerben
2. [lauflicht/](lauflicht/) - ein Punkt wandert, Knopf A/B = Tempo
3. [regenbogen/](regenbogen/) - Regenbogen laeuft ueber den Strip

Masse fuers CAD (spaeter): [../../../hardware/output/ws2812b-led-strip/](../../../hardware/output/ws2812b-led-strip/)
