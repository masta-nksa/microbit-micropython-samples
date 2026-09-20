---
title: Workflow Einstieg
---

# Workflow: Schritt fuer Schritt zur Codeeingabe

Dieser Weg fuehrt in **fester Reihenfolge** durch Montag und Dienstagvormittag.
Am Ende oeffnet deine Box nur, wenn du einen Code eingegeben hast - mit dem
Servo, den Sensoren des micro:bit und der 4-Digit-Anzeige.

## So funktioniert der Workflow

- Immer **nur eine Station** auf einmal. Erst wenn **"Fertig, wenn"** stimmt,
  geht es zur naechsten.
- Jede Station hat denselben Aufbau: **Ziel** - **Material** - **So geht's** -
  **Fertig, wenn** - **Weiter mit**.
- Nichts ueberspringen. Die Zusatzaufgaben am Ende sind freiwillig.
- Klappt etwas nicht: zuerst die Tabelle
  [Wenn etwas nicht klappt](#wenn-etwas-nicht-klappt), dann die Lehrperson
  fragen (spaetestens nach 10 Minuten).
- Die Zeiten sind Richtwerte. Wichtig ist die Reihenfolge, nicht das Tempo.

## Uebersicht

| Nr | Station | Neu dazu | Sample / Aufgabe | Richtwert |
|---:|---------|----------|------------------|-----------|
| 1 | Editor und Kabel | micro:bit, USB-Kabel | [Setup](setup.md) | 10 min |
| 2 | Knoepfe A und B | nichts | [a-b-zaehler](../code-samples/onboard/buttons/a-b-zaehler/) | 10 min |
| 3 | Neigung messen | nichts | [wasserwaage](../code-samples/onboard/accelerometer/wasserwaage/) | 10 min |
| 4 | Servo auf dem Tisch (ohne Zahnrad) | Servo, Batteriefach 3xAA | [zwei-stellungen](../code-samples/servo/miuzei-9g-servo/zwei-stellungen/) | 20 min |
| 5 | Box und Schliessmechanismus zusammenbauen | Box, Mechanismus | Anleitung der Lehrperson | 45-90 min |
| 6 | Endlagen messen | Servo in der Mechanik | [endlagen-kalibrieren](../code-samples/servo/miuzei-9g-servo/endlagen-kalibrieren/) | 20 min |
| 7 | Box oeffnen und schliessen | nichts | [box-startprogramm](../code-samples/servo/miuzei-9g-servo/box-startprogramm/) | 15 min |
| 8 | 4-Digit-Anzeige anschliessen | 4-Digit-Anzeige | [zahl-anzeigen](../code-samples/output/tm1637-4digit/zahl-anzeigen/) | 20 min |
| 9 | Anzeige als Zaehler | nichts | [zaehler](../code-samples/output/tm1637-4digit/zaehler/) | 15 min |
| 10 | Codeeingabe, Stufe 1 | nichts | eigene Aufgabe (siehe unten) | 45 min |
| 11 | Codeeingabe, Stufe 2 | nichts | eigene Aufgabe (siehe unten) | 45 min |

Pins, die in diesem Workflow belegt werden - **alles bleibt immer angeschlossen**,
es wird nie umgesteckt:

| Pin am micro:bit | Belegung |
|------------------|----------|
| P0 | Servo (Signal) |
| P1 | 4-Digit-Anzeige (CLK) |
| P2 | 4-Digit-Anzeige (DIO) |
| 3V | 4-Digit-Anzeige (VCC) |
| GND | gemeinsame Masse: Servo, Batteriefach, Anzeige |

Die Knoepfe A und B, die Neigung und das Logo zum Antippen sind im
micro:bit eingebaut und brauchen keinen Pin.

---

## Teil A: Nur der micro:bit

### Station 1: Editor und Kabel

**Ziel:** Ein Programm vom Computer auf den micro:bit uebertragen.

**Material:** micro:bit, USB-Kabel (Datenkabel).

**So geht's:**

1. Editor oeffnen: <https://python.microbit.org/v/3> (Chrome oder Edge).
2. micro:bit per USB anschliessen.
3. **Connect** klicken, micro:bit auswaehlen.
4. Irgendein Beispielprogramm einfuegen, **Send to micro:bit** klicken.

Genauer Ablauf mit Bildern: [Setup](setup.md).

**Fertig, wenn:** der micro:bit das Programm ausfuehrt (z. B. etwas auf der
LED-Matrix erscheint).

**Weiter mit:** Station 2.

### Station 2: Knoepfe A und B

**Ziel:** Mit den Knoepfen A und B einen Wert zaehlen.

**Material:** nur der micro:bit.

**So geht's:**

1. Sample oeffnen: [a-b-zaehler](../code-samples/onboard/buttons/a-b-zaehler/).
2. Den Code in den Editor kopieren und auf den micro:bit senden.
3. Ausprobieren: A, B, A und B zusammen.

**Fertig, wenn:** A zaehlt hoch, B runter, A und B zusammen setzt auf 0.

**Weiter mit:** Station 3.

### Station 3: Neigung messen

**Ziel:** Den eingebauten Neigungssensor (Beschleunigungssensor) kennenlernen.

**Material:** nur der micro:bit.

**So geht's:**

1. Sample oeffnen: [wasserwaage](../code-samples/onboard/accelerometer/wasserwaage/).
2. Code kopieren, senden.
3. micro:bit langsam nach links, rechts, vorne und hinten kippen.

**Fertig, wenn:** der Leuchtpunkt in die Richtung wandert, in die du kippst.

**Weiter mit:** Station 4.

---

## Teil B: Servo und Box

### Station 4: Servo auf dem Tisch

**Ziel:** Den Servo anschliessen und steuern - **noch nicht in der Box**.

**Material:** micro:bit, Servo, Batteriefach 3xAA (4.5 V), 3 Kabel fuer den
Servo, 2 Kabel fuer die Masse-Bruecke.

**So geht's:**

1. Servo **frei auf den Tisch** legen, **ohne Zahnrad**. Nichts daran
   befestigen. Die Lehrperson bespricht diesen Schritt vorher mit der Klasse.
2. Verkabeln, **Batteriefach noch ausgeschaltet**:

```
  Batteriefach 3xAA          Servo                 micro:bit
  ----------------           -----                 ---------
  rot  (+)  ---------------> rot   (+)
  schwarz (-) --+----------> braun (-)
                |
                +--------------------------------> GND     (gemeinsame Masse!)
                       orange/gelb ---------------> P0      (Signal)

  3V am micro:bit bleibt frei.
```

3. Sample oeffnen: [zwei-stellungen](../code-samples/servo/miuzei-9g-servo/zwei-stellungen/).
4. Code kopieren, senden.
5. Batteriefach einschalten. micro:bit bleibt am USB-Kabel.
6. Knopf A und Knopf B druecken.

Mehr zur Stromversorgung: [Servo-Bauteil](../code-samples/servo/miuzei-9g-servo/#stromversorgung---wichtig).

**Fertig, wenn:** A den Servo auf 0 Grad und B auf 180 Grad dreht, ohne dass er
zittert.

**Weiter mit:** Station 5.

### Station 5: Box und Schliessmechanismus zusammenbauen

**Ziel:** Box, Schliessmechanismus und micro:bit-Halterung zusammenbauen.

**Material:** Box-Teile, Schliessmechanismus, micro:bit-Halterung, Servo.

**So geht's:** Die Lehrperson zeigt zuerst die einfache Beispielbox und gibt
dir danach die Aufbauanleitung fuer Box und Schliessmechanismus. Das Zahnrad
kommt erst nach dieser Anleitung auf den Servo. Den Servo **grob in
Mittelstellung** in den Mechanismus setzen (siehe
[endlagen-kalibrieren](../code-samples/servo/miuzei-9g-servo/endlagen-kalibrieren/)).
Ab jetzt darf der Servo **nie mehr auf 0 oder 180 Grad** gefahren werden -
nur noch mit den Programmen aus Station 6 und 7.

**Fertig, wenn:** Box steht, Mechanismus sitzt, Servo ist angeschlossen wie in
Station 4.

**Weiter mit:** Station 6.

### Station 6: Endlagen messen

**Ziel:** Die zwei Werte finden, zwischen denen dein Servo sicher faehrt.

**Material:** Box mit angeschlossenem Servo.

**So geht's:**

1. Sample oeffnen: [endlagen-kalibrieren](../code-samples/servo/miuzei-9g-servo/endlagen-kalibrieren/).
2. Code kopieren, senden. **Open Serial** im Editor anklicken.
3. Knopf **B** gedrueckt halten: der Wert steigt langsam, der Servo faehrt.
   Knopf **A**: der Wert sinkt.
4. Kurz **vor** dem Anschlag der Mechanik stoppen (Box ganz offen bzw. ganz zu). Nicht gegen den Anschlag
   druecken. Hoerst du ein Brummen: sofort loslassen.
5. **A und B zusammen** druecken: der Wert erscheint. Notieren.
6. Das Gleiche fuer die andere Endlage.

Deine Werte:

| Endlage | Wert (us) |
|---------|-----------|
| Box ganz offen (`PULS_AUF`) | |
| Box ganz zu (`PULS_ZU`) | |

Danach beide Werte um etwa 15 bis 30 us **Richtung Mitte** zuruecknehmen -
das ist die Sicherheitsreserve.

**Fertig, wenn:** beide Werte notiert sind.

**Weiter mit:** Station 7.

### Station 7: Box oeffnen und schliessen

**Ziel:** Die Box per Knopfdruck oeffnen und schliessen.

**Material:** wie Station 6.

**So geht's:**

1. Sample oeffnen: [box-startprogramm](../code-samples/servo/miuzei-9g-servo/box-startprogramm/).
2. Oben im Code `PULS_AUF` und `PULS_ZU` mit deinen Werten aus Station 6
   ersetzen. `START_ZUSTAND` auf die Lage setzen, in der die Box beim
   Einschalten steht.
3. Code kopieren, senden.
4. Knopf A: Box oeffnen. Knopf B: Box schliessen. A und B zusammen: Notfall
   (faehrt langsam in die Mitte).

Solange die zwei Werte fehlen, zeigt die Matrix nur ein `?` und der Servo
faehrt nicht.

**Fertig, wenn:** die Box sich 5-mal hintereinander per Knopf oeffnen und
schliessen laesst, ohne Brummen oder Zittern.

**Weiter mit:** Station 8.

---

## Teil C: Die 4-Digit-Anzeige

### Station 8: 4-Digit-Anzeige anschliessen

**Ziel:** Eine Zahl auf der 4-Digit-Anzeige anzeigen. Der Servo bleibt dabei
**angeschlossen**.

**Material:** 4-Digit-Anzeige (TM1637), 4 Kabel.

**So geht's:**

1. Kabel **nach der Beschriftung** auf dem Modul anschliessen, nicht nach der
   Position:

```
   Anzeige CLK -> P1      Anzeige DIO -> P2
   Anzeige VCC -> 3V      Anzeige GND -> GND
```

2. Sample oeffnen: [zahl-anzeigen](../code-samples/output/tm1637-4digit/zahl-anzeigen/).
3. Im Editor eine **zweite Datei** `tm1637.py` anlegen und die Bibliothek aus
   dem Sample hineinkopieren (Anleitung: [Setup](setup.md#zweite-datei-hinzufuegen-z-b-eine-mitgelieferte-bibliothek)).
4. Code in `main.py` kopieren, senden.

**Fertig, wenn:** die Anzeige die Zahl zeigt, die im Programm steht.

**Weiter mit:** Station 9.

### Station 9: Anzeige als Zaehler

**Ziel:** Mit den Knoepfen A und B eine Zahl auf der Anzeige einstellen.

**So geht's:**

1. Sample oeffnen: [zaehler](../code-samples/output/tm1637-4digit/zaehler/).
2. Code in `main.py` kopieren, senden. `tm1637.py` bleibt als zweite Datei.

**Fertig, wenn:** A hochzaehlt, B runterzaehlt, A und B zusammen auf 0 setzt.

**Weiter mit:** Station 10.

---

## Teil D: Codeeingabe

Ab hier schreibst du ein eigenes Programm. Du setzt es aus **Bausteinen** der
Stationen 6 bis 9 zusammen. Gehe **Teilschritt fuer Teilschritt** vor und
teste nach jedem Teilschritt.

### Station 10: Codeeingabe, Stufe 1

**Ziel:** Die Box oeffnet nur, wenn die richtige Zahl eingestellt und mit dem
Logo bestaetigt wurde.

**Bausteine:**

| Baustein | Woher |
|----------|-------|
| Zahl mit A und B einstellen, Anzeige | [zaehler](../code-samples/output/tm1637-4digit/zaehler/) |
| Box oeffnen und schliessen | [box-startprogramm](../code-samples/servo/miuzei-9g-servo/box-startprogramm/), die Funktionen `box_auf()`, `box_zu()`, `box_zustand()` |
| Logo antippen | [logo-schalter](../code-samples/onboard/touch-logo/logo-schalter/), `pin_logo.is_touched()` |

**So geht's:**

1. **Zusammenfuehren.** Den Code aus `zaehler` und die Funktionen aus
   `box-startprogramm` (von den Endlagen-Werten bis und mit
   `rueckmeldung()`, ohne die Hauptschleife) in **eine** `main.py` kopieren.
   `tm1637.py` bleibt die zweite Datei.
   *Test:* Die Anzeige zaehlt mit A und B, die Box bewegt sich noch nicht.
2. **Geheimzahl.** Oben im Programm eine Zeile einfuegen, z. B. `CODE = 42`.
3. **Bestaetigen.** Wird das Logo angetippt, vergleichst du die Zahl auf der
   Anzeige mit `CODE`.
   *Test:* Die LED-Matrix zeigt bei richtiger Zahl `Image.YES`, bei falscher
   `Image.NO`.
4. **Oeffnen.** Bei richtiger Zahl die Box mit `box_auf()` oeffnen. Bei
   falscher Zahl bleibt sie zu und die Anzeige geht auf 0.
5. **Schliessen.** A und B zusammen: Box mit `box_zu()` schliessen und
   Anzeige auf 0.

**Fertig, wenn:** die richtige Zahl mit Logo die Box oeffnet, eine falsche Zahl
nichts bewirkt und A+B sie wieder schliesst.

**Weiter mit:** Station 11.

### Station 11: Codeeingabe, Stufe 2

**Ziel:** Zwei Sicherungen hintereinander: **erst die Zahl, dann eine
Neigungsfolge**. Erst wenn beide stimmen, oeffnet die Box.

**Bausteine:**

| Baustein | Woher |
|----------|-------|
| Neigung erkennen | [wasserwaage](../code-samples/onboard/accelerometer/wasserwaage/), `accelerometer.get_x()` |
| Stufe 1 | dein Programm aus Station 10 |

**So geht's:**

1. **Neigung lesen.** In einem **neuen, kleinen Programm** die Neigung
   ausgeben, z. B. `print(accelerometer.get_x())` (im Editor **Open Serial**).
   Notiere den Wert bei "nach links kippen" und "nach rechts kippen".
2. **Eine Richtung erkennen.** Beispiel: `accelerometer.get_x() < -500` heisst
   "nach links". Alternativ gibt es `accelerometer.was_gesture("left")`.
   *Test:* Die Matrix zeigt `L`, wenn du nach links kippst, und `R` bei rechts.
3. **Folge speichern.** Jede erkannte Richtung an eine Liste `eingabe`
   anhaengen. Beispiel fuer die richtige Folge: `FOLGE = ["L", "R", "L"]`.
   *Test:* Nach drei Kippbewegungen zeigt die Matrix `Image.YES` (Folge
   richtig) oder `Image.NO`.
4. **Zusammenbauen.** In dein Programm aus Station 10 eine Variable `stufe`
   einfuehren: `stufe = 1` heisst "Zahl wird eingegeben", `stufe = 2` heisst
   "Neigungsfolge wird eingegeben". Bei richtiger Zahl geht es von 1 auf 2
   und die Box bleibt noch zu.
5. **Oeffnen.** Nur wenn in Stufe 2 die Folge stimmt, die Box oeffnen.
   Bei falscher Zahl **oder** falscher Folge: `stufe = 1`, Anzeige auf 0.

**Fertig, wenn:** richtige Zahl + richtige Folge die Box oeffnet und jeder
Fehler bei einer der beiden Stufen dich zurueck zum Anfang bringt.

**Geschafft.** Zeige die Box der Lehrperson.

---

## Zusatzaufgaben (freiwillig, erst nach Station 11)

| Aufgabe | Sample | Bemerkung |
|---------|--------|-----------|
| Ideen mit den Sensoren des micro:bit | [box-startprogramm](../code-samples/servo/miuzei-9g-servo/box-startprogramm/#ideen-zum-ausbauen) | sechs kleine Ideen, immer eine nach der anderen |
| Schuetteln als Code | [shake-wuerfel](../code-samples/onboard/accelerometer/shake-wuerfel/) | `accelerometer.was_gesture("shake")` |
| Richtung als Code | [kompass-pfeil](../code-samples/onboard/compass/kompass-pfeil/) | Kompass muss zuerst kalibriert werden |
| Logo als Schalter | [logo-schalter](../code-samples/onboard/touch-logo/logo-schalter/) | Logo antippen zum Ein- und Ausschalten |
| Melodie bei richtigem Code | [melodie-und-sound](../code-samples/onboard/speaker/melodie-und-sound/) | Lautsprecher ist eingebaut; mit Servo an P0 immer `pin=None` angeben, z. B. `music.pitch(880, 200, pin=None)` |
| Lichtsensor als Code | [nachtlicht](../code-samples/onboard/light-level/nachtlicht/) | Matrix abdecken |
| Zeit begrenzen | [stoppuhr](../code-samples/output/tm1637-4digit/stoppuhr/) | Code muss innerhalb von 30 Sekunden eingegeben werden |
| LED-Strip | [erste-farben](../code-samples/output/ws2812b-led-strip/erste-farben/) | siehe Hinweis unten |

**Hinweis LED-Strip:** Im Sample steht die Datenleitung an **P0**. P0 gehoert
aber dem Servo. Im Code `pin0` durch `pin1` ersetzen und die Datenleitung an P1
stecken. P1 gehoert dann nicht mehr der 4-Digit-Anzeige - **Servo, LED-Strip und
4-Digit-Anzeige zusammen gehen ohne Breakout-Board nicht.**

---

## Wenn etwas nicht klappt

| Problem | Loesung |
|---------|---------|
| micro:bit erscheint nicht bei **Connect** | Anderes USB-Kabel (Datenkabel, nicht nur Ladekabel), anderer USB-Port, Chrome oder Edge verwenden |
| Servo zittert oder micro:bit startet neu | Batteriefach eingeschaltet? Batterien frisch? Masse-Bruecke (GND) von Batteriefach zu micro:bit vorhanden? |
| Servo bewegt sich nicht | Signal an **P0**, nicht an einem anderen Pin? Batteriefach eingeschaltet? |
| Servo brummt an einer Endlage | Sofort Programm stoppen. Den Wert 15 bis 30 us Richtung Mitte setzen |
| Matrix zeigt nur ein `?` | `PULS_AUF` und `PULS_ZU` fehlen noch im Programm (Station 6) |
| Box faehrt in die falsche Richtung | `PULS_AUF` und `PULS_ZU` im Programm tauschen |
| Anzeige bleibt dunkel | CLK an **P1**, DIO an **P2**, VCC an **3V**? Datei `tm1637.py` als zweite Datei im Editor angelegt? Kabel nach der Beschriftung auf dem Modul angeschlossen? |
| Fehlermeldung im Editor | Zeilennummer notieren, Zeile genau ansehen (Einrueckung, Doppelpunkt, Schreibweise), dann die Lehrperson fragen |

Zurueck zur [Uebersicht](../README.md) oder zu den [Code-Samples](../code-samples/README.md).
