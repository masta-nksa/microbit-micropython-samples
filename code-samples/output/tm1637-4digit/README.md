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
  Strom spuerbar werden. In den Samples ist die Helligkeit niedrig
  voreingestellt (3 von 0-7). Flackert die Anzeige oder startet der micro:bit
  neu: Helligkeit senken oder wie beim Servo/Strip eine externe 4,5-5-V-Quelle
  mit gemeinsamer Masse verwenden.
- Kein Level-Shifter noetig - anders als beim WS2812B ist das TM1637-Protokoll
  bit-gebanged und tolerant gegenueber 3,3-V-Pegeln.

## Bibliothek statt Eigenbau: mcauser/microbit-tm1637

Alle Samples nutzen die fertige, micro:bit-native Bibliothek
[**microbit-tm1637**](https://github.com/mcauser/microbit-tm1637) von Mike
Causer (MIT-Lizenz) als zweite Projektdatei `tm1637.py` - wie man die im
Online-Editor anlegt, steht in
[docs/setup.md](../../../docs/setup.md#zweite-datei-hinzufuegen-z-b-eine-mitgelieferte-bibliothek).

**Wichtig beim Suchen:** es gibt von Mike Causer **zwei** aehnlich benannte
Bibliotheken -

| Repo | fuer | passt hier? |
|------|------|-------------|
| [mcauser/**microbit-tm1637**](https://github.com/mcauser/microbit-tm1637) | micro:bit MicroPython (`microbit.pinX.write_digital()`) | **ja** - genau das wird verwendet |
| [mcauser/**micropython-tm1637**](https://github.com/mcauser/micropython-tm1637) | "grosses" MicroPython auf ESP32/Pico/Pyboard (`machine.Pin(nummer, Pin.OUT)`) | **nein** - der micro:bit hat kein `machine.Pin`, das Modul liefe so nicht |

Die micro:bit-Variante bringt mehr mit als unser fruehrer Eigenbau-Treiber:

```python
from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin1, dio=pin2, brightness=3)   # 0 (dunkel) .. 7 (hell)

tm.number(1234)              # -999..9999, rechtsbuendig
tm.numbers(12, 34, colon=True)   # zwei 2-stellige Zahlen + Doppelpunkt, z. B. Uhrzeit
tm.show("HELP")              # Text (0-9, A-Z, Leerzeichen, - und Grad-Symbol)
tm.scroll("HALLO MICROBIT")  # Text durchlaufen lassen
tm.hex(0x2A)                 # Hexadezimal
tm.temperature(temperature())    # mit automatischem Grad-Symbol, LO/HI bei Ueberlauf
tm.brightness(5)             # Helligkeit nachtraeglich aendern
```

## Das Protokoll (Hintergrund)

TM1637 spricht ein I2C-aehnliches, aber eigenes Protokoll: **Start** = DIO
faellt, waehrend CLK hoch ist. **Stop** = DIO steigt, waehrend CLK hoch ist.
Dazwischen werden Bytes LSB-zuerst getaktet, adressiert per Befehlsbyte
(`0x40` automatische Adresse, `0xC0` Startadresse 0, `0x88 | Helligkeit`
Anzeige an). Genau das erledigt `tm1637.py` intern - fuer die Samples reicht
der Blick auf die Bibliotheks-Methoden oben.

## Samples (Lernreihenfolge)

1. [zahl-anzeigen/](zahl-anzeigen/) - Grundfunktion, ein paar Zahlen zeigen
2. [zaehler/](zaehler/) - Knopf A/B zaehlen 0..9999, A+B = Reset
3. [stoppuhr/](stoppuhr/) - MM:SS, Start/Pause, Reset, blinkender Doppelpunkt

Masse fuers CAD (spaeter): [../../../hardware/output/tm1637-4digit/](../../../hardware/output/tm1637-4digit/)
