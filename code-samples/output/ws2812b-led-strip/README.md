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

### Warum sind es 5 Kabel?

Elektrisch braucht der Strip nur **drei** Leitungen (`5V`, `GND`, Data).
Fuenf Kabel am Eingang sind trotzdem ueblich:

| Kabel | wohin |
|---|---|
| 3-poliger JST-SM-Stecker | `5V` + `DIN` + `GND` |
| extra rot (dick) | nochmal `5V` |
| extra weiss/schwarz (dick) | nochmal `GND` |

Der 3-polige Stecker ist zum **Weiterverbinden / fuer die Daten**, das dicke
rot/weiss-Paar ist die **Strom-Einspeisung** direkt an den `5V`/`GND`-Pads -
die duennen Steckerdraehte wuerden bei vielen LEDs zu heiss.

**So findest du raus, was was ist:** jedes Kabel bis zu seinem Pad verfolgen.
Zwei Kabel am selben `5V`-Pad = Stecker + Einspeisung (parallel, macht nichts).
Das **Datenkabel gibt es nur einmal** (Pad `DIN` am Eingang bzw. `DO` am Ausgang).

Fuer den Anschluss: alle `5V` zusammen an `+`, alle `GND` zusammen an `-`
(und an micro:bit `GND`), das eine Datenkabel an `P0`.

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

## Strip zuschneiden und Kabel anloeten

Der Strip laesst sich **nur an den markierten Linien** trennen - zwischen
je zwei LEDs verlaeuft eine Linie mit durchgehenden Kupfer-Pads (oft mit
Schere-Symbol). Fuer **5er-Gruppen** also nach jeder 5. LED schneiden.

Jedes Segment hat zwei Enden mit je drei Pads:

```
   Eingang  (Pfeil zeigt in das Segment)        Ausgang
   5V  DIN  GND   [ LED LED LED LED LED ]   5V  DO  GND
```

**Ein einzelnes Segment anschliessen:** 3 Litzen an die **Eingangs**-Pads
(`5V`, `DIN`, `GND`) - `DIN` an `P0`, `5V`/`GND` an die 4,5-V-Box (Masse
gemeinsam mit dem micro:bit).

**Segmente verketten:** vom **Ausgang** des einen zum **Eingang** des
naechsten je drei kurze Litzen:

```
   Segment A  Ausgang         Segment B  Eingang
        5V  ------------------------  5V
        DO  ------------------------  DIN
        GND ------------------------  GND
```

- Immer **Ausgang -> Eingang**, nie umgekehrt (Pfeilrichtung).
- Duenne Litze (26-28 AWG). Pad und Draht vorher verzinnen, dann kurz
  (1-2 s, ~320 Grad) loeten - die Pads loesen sich bei zu viel Hitze.
- **Zugentlastung:** ein Tropfen Heisskleber ueber jede Loetstelle.
- Wer es steckbar will: 3-polige JST-SM-Stecker an die Enden loeten.

**Strom:** `5V` und `GND` laufen ueber die ganze Kette mit. Bis ~50 LEDs
gesamt reicht die Einspeisung am Anfang; bei mehr zusaetzlich am Ende der
Kette `5V`/`GND` anschliessen.

**Im Code:** `ANZAHL` = **Summe aller LEDs** in der Kette (z. B. 4 Segmente
x 5 = 20). Die LEDs sind durchgehend `0 .. ANZAHL-1` nummeriert, egal wo die
Schnitte sind.

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
