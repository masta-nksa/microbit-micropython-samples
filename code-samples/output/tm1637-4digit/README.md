# TM1637 4-Digit-Anzeige

4-stellige 7-Segment-Anzeige mit eingebautem **TM1637**-Treiberchip. Statt
vieler Segment-Leitungen braucht sie nur **zwei** Datenleitungen (CLK, DIO) -
der Chip uebernimmt das Multiplexen der vier Ziffern selbst.

## Anschluesse am Modul

| Pin (Beschriftung auf dem Modul) | Bedeutung |
|---|---|
| `CLK` | Takt |
| `DIO` | Daten (in beide Richtungen) |
| `VCC` | Plus |
| `GND` | Masse |

Die **Reihenfolge der 4 Pins ist von Modul zu Modul unterschiedlich** - nach
der Beschriftung anschliessen, nicht nach der Position.

**Konkretes Beispiel** (ein tatsaechlich verwendetes Modul, Beschriftung auf
der Rueckseite von links nach rechts): `GND` `VCC` `DIO` `CLK`. Also nicht
automatisch von "erster Pin = CLK" ausgehen - immer selbst nachsehen.

Manche Module zeigen die 4 Ziffern **untereinander statt nebeneinander**
(die Anzeige-Einheit ist auf der Platine um 90 Grad gedreht). Elektrisch und
im Code macht das keinen Unterschied - die Zahl laeuft dann nur von oben nach
unten statt von links nach rechts. Mit [zahl-anzeigen](zahl-anzeigen/) testen,
in welcher Reihenfolge und wo bei deinem Modul der Doppelpunkt sitzt.

## Anschluss an den micro:bit

Anders als der WS2812B-Strip braucht die TM1637-Anzeige **keine externe
Stromquelle**: der Chip laeuft mit 3.3-5.5 V, der micro:bit-`3V`-Pin reicht.

```
   micro:bit          TM1637-Modul
  +---------+        +------------+
  |      P1 |--------| CLK        |
  |      P2 |--------| DIO        |
  |      3V |--------| VCC        |
  |     GND |--------| GND        |
  +---------+        +------------+
```

- Bei **voller Helligkeit mit allen Segmenten aller 4 Ziffern** kann der
  Strom spuerbar werden. In den Samples ist `HELLIGKEIT` niedrig voreingestellt
  (3 von 0-7). Flackert die Anzeige oder startet der micro:bit neu: `HELLIGKEIT`
  senken oder wie beim Servo/Strip eine externe 4,5-5-V-Quelle mit gemeinsamer
  Masse verwenden.
- Kein Level-Shifter noetig - anders als beim WS2812B ist das TM1637-Protokoll
  bit-gebanged und tolerant gegenueber 3,3-V-Pegeln.

## Das Protokoll (kurz)

TM1637 spricht ein I2C-aehnliches, aber eigenes Protokoll: **Start** = DIO
faellt, waehrend CLK hoch ist. **Stop** = DIO steigt, waehrend CLK hoch ist.
Dazwischen werden Bytes LSB-zuerst getaktet. Ein fertiges MicroPython-Modul
gibt es im micro:bit-Editor nicht eingebaut - darum bringt jedes Sample einen
**kompletten, kleinen Treiber direkt mit** (Funktionen `_start`, `_stop`,
`_write_byte`, `anzeige`). Nichts extra zu installieren, einfach den ganzen
Code kopieren.

Wichtige Befehle:

| Byte | Bedeutung |
|---|---|
| `0x40` | Datenbefehl: Adresse zaehlt beim Schreiben automatisch weiter |
| `0xC0` | Adressbefehl: Startadresse 0 (erste Ziffer) |
| `0x88 \| HELLIGKEIT` | Anzeige an, Helligkeit 0-7 |

`anzeige(d0, d1, d2, d3, doppelpunkt=False)` nimmt vier Ziffern (`0-9` oder
`None` fuer eine leere Stelle). Der **Doppelpunkt** haengt bei den meisten
Modulen am Bit `0x80` der **zweiten** Ziffer - bei manchen Modulen kann das
abweichen, dann im Code die Stelle (`i == 1`) anpassen.

## Samples (Lernreihenfolge)

1. [zahl-anzeigen/](zahl-anzeigen/) - Grundfunktion, ein paar Zahlen zeigen (enthaelt den Treiber)
2. [zaehler/](zaehler/) - Knopf A/B zaehlen 0..9999, A+B = Reset
3. [stoppuhr/](stoppuhr/) - MM:SS, Start/Pause, Reset, blinkender Doppelpunkt

Masse fuers CAD (spaeter): [../../../hardware/output/tm1637-4digit/](../../../hardware/output/tm1637-4digit/)
