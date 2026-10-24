# Taster Version 2 - Fuehrungshuelse mit Klemmmutter (3D-Druck)

Verlaengerung fuer die micro:bit-Taster **A** und **B**, damit man sie durch den
Holzdeckel mit dem Finger druecken kann. Anders als [Version 1](../taster-v1/README.md)
(Gewindebolzen im Holzloch) sitzt hier eine **Huelse fest im Holz**; der Stoessel gleitet
darin mit langer Fuehrung.

> **Status: am echten Teil getestet und bestaetigt funktionierend** (Holzdicke 6 mm,
> Grundversion ohne Fuehrungsring am Knopf). Der Fuehrungsring am Knopf und die duennere
> Klemmmutter (unten, "Aenderungen nach dem Test") sind neu und nur in Fusion numerisch
> geprueft - vor dem naechsten Druck kurz kontrollieren, ob der Ring wirklich fuehrt und
> nicht klemmt. Diese Version ist auf **6 mm Holz zugeschnitten** (Parameter `holz`),
> nicht mehr auf einen Dickenbereich.

## Funktion

- **Huelse:** Rohr mit Aussengewinde Tr12x2, unten ein flacher L-Fuss (0,8 mm) mit
  Aussparung fuer den Taster, oben eine Lippe. Von unten durch das Holzloch gesteckt,
  zieht die **Klemmmutter** sie von oben gegen das Holz - die Huelse sitzt fest und
  wackelt nicht. Der Fuss ist das Gegenstueck zur Mutter (unter dem Holz ist fuer eine
  zweite Mutter kein Platz).
- **Stoessel:** Zylinder (Ø 6,8 mm) in der Huelsenbohrung (Ø 7,2 mm), unten ein
  Druckstift auf die Tastermitte, oben ein Hals durch die Lippe. Die Lippe verhindert,
  dass der Stoessel nach oben herausrutscht; die Feder des Tasters stellt ihn nach dem
  Druecken zurueck.
- **Knopf mit Fuehrungsring:** Drehknopf auf dem Gewindehals M5x0,8. Zusaetzlich hat der
  Knopf einen Ring (Innendurchmesser Ø 12,4 mm), der beim Aufschrauben ueber den freien
  Rundstab der Huelse (oberhalb der Klemmmutter) greift. Das fuehrt den Knopf beim
  Druecken auf dem grossen Huelsendurchmesser statt nur ueber den duennen Gewindehals -
  deutlich weniger Wackeln als bei der reinen Stift-Fuehrung.
- **Klemmmutter:** haelt nicht nur die Huelse fest, sondern begrenzt jetzt auch, wie tief
  sich der Ring aufschrauben laesst (der Ring stoesst nicht an ihr an, siehe Pruefung
  unten - aber der freie Rundstab dazwischen ist endlich).

## Teile

| Datei | Anzahl (fuer A und B) | Beschreibung |
|---|---|---|
| [`huelse_links.stl`](huelse_links.stl) | 1x | Huelse fuer den Taster nahe der linken Rahmenwand |
| [`huelse_rechts.stl`](huelse_rechts.stl) | 1x | gespiegelte Variante fuer die rechte Seite |
| [`stoessel.stl`](stoessel.stl) | 2x | Stoessel, fuer beide Seiten gleich |
| [`knopf.stl`](knopf.stl) | 2x | Drehknopf mit Fuehrungsring |
| [`klemmmutter.stl`](klemmmutter.stl) | 2x | Sechskantmutter Tr12x2 |
| [`deck_mit_microbit_taster_v2.dxf`](deck_mit_microbit_taster_v2.dxf) | - | Deckel-DXF mit runden Loechern |

Woran man links/rechts erkennt: Der flache **Fuss zeigt immer von der naechsten
Rahmenwand weg zur Mitte** (zum LED-Fenster). Im Zweifel probeweise einlegen - die
falsche Huelse stoesst an der Rahmenwand an.

## Holz: rundes Loch

[`deck_mit_microbit_taster_v2.dxf`](deck_mit_microbit_taster_v2.dxf) ist deine
`deck_mit_microbit.dxf` mit einer einzigen Aenderung: die beiden 10 x 10 mm-Quadrate fuer
A/B sind durch **Kreise Ø 12,4 mm** an derselben Mitte ersetzt (r = 6,2). Die Huelse
(Ø 12) hat darin ca. 0,2 mm Spiel je Seite. Loecher zuerst an einem Reststueck schneiden
und mit der gedruckten Huelse pruefen - der Laserstrahl macht Loecher je nach Kerf etwas
groesser. **Unveraendert seit dem erfolgreichen Test.**

## Drucken

- Material PLA oder PETG, Duese 0,4 mm, Schichthoehe 0,15 - 0,2 mm, **ohne Stuetzen**,
  3 Wandlinien, Fuellung >= 40 %.
- **Die STL-Dateien sind schon druckfertig ausgerichtet:**
  - **Huelse:** kopfueber, die Lippe liegt auf dem Bett, der Fuss wird zuletzt gedruckt.
  - **Stoessel:** Gewindehals auf dem Bett, Stift oben. Kleine Aufstandsflaeche (Ø 5 mm),
    deshalb **Brim (5 mm)** verwenden.
  - **Knopf:** Dach (glatte Seite) auf dem Bett, Ring-Oeffnung oben.
  - **Klemmmutter:** flach.
- Innengewinde (Mutter, Knopf) haben je 0,15 mm Druckspiel eingerechnet. Klemmt es, kurz
  aufschrauben und wieder abdrehen; bei zu viel Spiel `gew_spiel` / `gew_spiel_m5` in
  `taster_bauen.py` verkleinern.
- Der Stoessel muss in der Huelsenbohrung leicht gleiten. Wenn nicht: Bohrung mit einem
  7-mm-Bohrer von Hand nachziehen oder `koerper_d` verkleinern. Ebenso sollte der Ring
  locker ueber die Huelse gehen, ohne zu klappern.

## Einbauen

1. Case **noch nicht** ans Holz schrauben.
2. **Stoessel von unten in die Huelse schieben**: Stift zuerst nach unten, der Hals kommt
   oben durch die Lippe (Stoessel liegt nach oben im Rohr).
3. **Huelse mit Stoessel von unten durch das Holzloch stecken** (Fuss unter dem Holz).
4. **Klemmmutter** von oben aufschrauben und handfest anziehen (Huelse dabei am Fuss
   festhalten).
5. **Knopf** auf den Gewindehals schrauben (siehe "Hub einstellen").
6. Case mit den beiden Schrauben an das Holz schrauben, micro:bit einschieben. Der Taster
   faehrt dabei in die Aussparung im Fuss.

## Hub einstellen

1. Den **Knopf aufschrauben, bis der Ring spuerbar ueber die Huelse rutscht** (ab da
   fuehrt er). Weiterdrehen, bis es merklich schwerer geht - das ist das Ende des
   nutzbaren Gewindes, kein Bauteil beruehrt sich dabei hart.
2. **Eine Vierteldrehung (0,5 mm) zurueckdrehen.** Das ist der Ausgangspunkt.
3. Testen. Klickt der Taster nicht, weiter zurueckdrehen (weniger Ring-Eingriff, mehr
   Abstand). Wird der Taster nie losgelassen oder schaltet dauernd, stimmt die
   Stiftlaenge nicht - siehe naechster Abschnitt.
4. Mit einem Tropfen Sekundenkleber oder Nagellack am Knopfgewinde sichern, wenn der Knopf
   nicht mehr verstellt werden soll.

**Bekanntes Restspiel:** In Ruhe hat der Stoessel etwa 0,4 mm Auf-und-ab-Spiel (er liegt
nur auf dem Taster). Das ist Absicht als Toleranz fuer einen etwas hoeheren Taster als
angenommen. Seitlich fuehrt die ca. 10 mm lange Bohrung; das Spiel dort betraegt 0,2 mm
je Seite. Der Ring am Knopf reduziert das Wackeln am Knopf selbst zusaetzlich, sobald er
eingeschraubt ist (Schritt 1).

## Wenn der Stift nicht passt

Die Laenge des Druckstifts (`stift_l`, 0,9 mm) gilt fuer einen Taster, dessen Oberkante
0,05 mm unter der Holzunterseite liegt. Liegt der Taster tatsaechlich hoeher, presst der
Stift ihn schon in Ruhe (Dauerdruck): `stift_l` kleiner machen und den Stoessel neu drucken
(`taster_bauen.py`). Liegt er tiefer, den Knopf weiter aufdrehen oder `stift_l` groesser
machen.

## Aenderungen nach dem Test (Fuehrungsring, duennere Mutter)

Nach dem erfolgreichen Test der Grundversion (ohne Ring) kamen zwei Aenderungen dazu:

- **Fuehrungsring am Knopf:** Der Knopf hat jetzt eine 4 mm tiefe, weite Bohrung
  (Ø 12,4 mm) zusaetzlich zur M5-Gewindebohrung. Beim Aufschrauben schiebt sie sich ueber
  den freien Rundstab der Huelse. Dafuer musste der Gewindebeginn am Stoessel-Hals naeher
  an die Lippe rutschen (`hals_gew_start` 1,0 -> 0,2 mm), sonst waere ein Teil des
  Knopf-Gewindes auf dem glatten Hals gelandet statt auf dem Gewinde - das haette
  geklemmt. In Fusion mit dem echten Case gegengeprueft: das M5-Gewinde greift ueber den
  gesamten nutzbaren Ring-Eingriff (0 bis 4 mm) sauber, keine Kollision mit Huelse oder
  Mutter.
- **Duennere Klemmmutter:** 4 mm -> **3 mm** (1,5 statt 2 Gewindegaenge bei Tr12x2). Sie
  haelt nur die Huelse leicht gegen das Holz, keine grosse Kraft - 1,5 Gaenge reichen fuer
  Handfestziehen; weniger als das wuerde ich beim gedruckten Gewinde nicht empfehlen.
- Dadurch ist die **Huelse jetzt 13,5 mm** lang (vorher 15,0 mm bei generischem
  Dickenbereich) - eingespart wurde die Reserve fuer Holz bis 9 mm, die es bei einer auf
  6 mm zugeschnittenen Huelse nicht mehr braucht, plus die duennere Mutter.

## Was in Fusion geprueft wurde

Gegen das echte Case-Modell (`Microbit_V2_Case`), einen 6-mm-Holzdeckel mit rundem
Ø 12,4 mm-Loch an den Positionen aus `deck_mit_microbit.dxf` und einen angenommenen
6 x 6 mm-Taster:

| Pruefung | Ergebnis |
|---|---|
| Huelse im Case, im Holzloch, gegen Taster | 0 mm3 Durchdringung |
| dasselbe mit Lageabweichung +-0,5 mm in X und Y (Handmass-Toleranz) | 0 mm3 |
| Seitliches Spiel der Huelse im Holzloch | ca. 0,2 mm je Seite |
| Stoessel in der Huelse: Ruhe / an der Lippe / 0,25 mm gedrueckt | 0 mm3 |
| Klemmmutter (3 mm) auf der Huelse bei 6 mm Holz | 0,000 mm3 (Gewinde greift) |
| M5-Gewinde Knopf <-> Stoessel-Hals bei Ring-Eingriff 0 / 1 / 2 / 3 / 3,8 / 4,1 mm | 0,000 mm3 (durchgaengig, auch ueber die volle Ringtiefe hinaus) |
| Fuehrungsring <-> Huelse und <-> Klemmmutter, gleiche Eingriffstiefen | 0,000 mm3 |
| STL-Netze | geschlossen, keine offenen Kanten |

Die rechte Huelse hat zur Rahmenwand hin nur zwischen 0,5 und 1 mm Reserve (bei +1 mm
Versatz Richtung Wand stoesst sie mit < 1 mm3 an).

## Annahmen, die nachgemessen werden sollten

| Annahme | Wert | Wo aendern |
|---|---|---|
| Tasterflaeche (X und Y) | 6,0 mm | `taster` |
| Taster-Oberkante | 0,05 mm unter der Holzunterseite (Rahmenhoehe 14,55 mm) | `d_taster`, `stift_l` |
| Tastermitte | Mitte des Holzlochs (X 8,2 / 48,4 mm, Y 9,74 mm im Case) | Loch im DXF |
| Loch im Holz | rund Ø 12,4 mm | `gew_d`, `loch_spiel` |
| Holzdicke | fest 6 mm (getestet) | `holz` - fuer anderes Holz aendern und neu ausfuehren |

Die Tasterhoehe (Rahmenhoehe 14,55 mm) folgt aus dem Fusion-Parameter `d110` und der
micro:bit-Angabe "Taster 4,55 mm ueber der Platine"
([tech.microbit.org](https://tech.microbit.org/hardware/)).

**Bauhoehe:** Bei 6 mm Holz steht die Huelse 7,5 mm ueber dem Holz. Mit Knopf, bei der
empfohlenen Kalibrierung (Ring-Eingriff ca. 3 mm), ragt die Oberseite des Knopfs
insgesamt etwa 15,5 mm ueber das Holz. Fuer andere Holzdicke `holz` in
`taster_bauen.py` aendern; Huelse, Stoessel und Knopfhals passen sich automatisch an.

## Neu erzeugen

[`taster_bauen.py`](taster_bauen.py) ist die parametrische Definition. In Fusion ein
**leeres** Design oeffnen, Skript ausfuehren (Dienstprogramme > Add-Ins > Skripte);
es baut die fuenf Koerper, prueft auf Streukoerper und schreibt die STL-Dateien
neben das Skript (Huelse und Stoessel kopfueber fuer den Druck). Parameter stehen im
Block `P` am Anfang.
