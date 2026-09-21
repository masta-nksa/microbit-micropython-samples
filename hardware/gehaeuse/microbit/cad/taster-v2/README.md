# Taster Version 2 - Fuehrungshuelse mit Klemmmutter (3D-Druck)

Verlaengerung fuer die micro:bit-Taster **A** und **B**, damit man sie durch den
Holzdeckel mit dem Finger druecken kann. Anders als [Version 1](../taster-v1/README.md)
(Gewindebolzen im Holzloch) sitzt hier eine **Huelse fest im Holz**; der Stoessel gleitet
darin mit langer Fuehrung. Das Holz darf 4 bis 9 mm dick sein.

> **Status: nicht am echten Teil getestet.** Passung im Case, Holzloch, Stoessel und
> alle Gewinde sind in Fusion numerisch geprueft (siehe unten). Die Tasterflaeche ist
> aber **angenommen** (6 x 6 mm, Oberkante praktisch buendig zur Holzunterseite) -
> vor dem Serien-Druck einen Testdruck machen und die Annahmen nachmessen.

## Funktion

- **Huelse:** Rohr mit Aussengewinde Tr12x2, unten ein flacher L-Fuss (0,8 mm) mit
  Aussparung fuer den Taster, oben eine Lippe. Von unten durch das Holzloch gesteckt,
  zieht die **Klemmmutter** sie von oben gegen das Holz - die Huelse sitzt fest und
  wackelt nicht. Der Fuss ist das Gegenstueck zur Mutter (unter dem Holz ist fuer eine
  zweite Mutter kein Platz).
- **Stoessel:** Zylinder (Ø 6,8 mm, 11,75 mm lang) in der Huelsenbohrung (Ø 7,2 mm),
  unten ein Druckstift auf die Tastermitte, oben ein Hals durch die Lippe. Die Lippe
  verhindert, dass der Stoessel nach oben herausrutscht; die Feder des Tasters stellt
  ihn nach dem Druecken zurueck.
- **Knopf:** Drehknopf auf dem Gewindehals M5x0,8. Sein Abstand zur Huelsenoberkante ist
  der **Hub** und ueber das Gewinde einstellbar.
- **Holzdicke:** Nur die Klemmmutter laeuft weiter hoch oder runter. Huelse und Stoessel
  sind fuer jede Dicke bis 9 mm gleich.

## Teile

| Datei | Anzahl (fuer A und B) | Beschreibung |
|---|---|---|
| [`huelse_links.stl`](huelse_links.stl) | 1x | Huelse fuer den Taster nahe der linken Rahmenwand |
| [`huelse_rechts.stl`](huelse_rechts.stl) | 1x | gespiegelte Variante fuer die rechte Seite |
| [`stoessel.stl`](stoessel.stl) | 2x | Stoessel, fuer beide Seiten gleich |
| [`knopf.stl`](knopf.stl) | 2x | Drehknopf |
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
groesser.

## Drucken

- Material PLA oder PETG, Duese 0,4 mm, Schichthoehe 0,15 - 0,2 mm, **ohne Stuetzen**,
  3 Wandlinien, Fuellung >= 40 %.
- **Die STL-Dateien sind schon druckfertig ausgerichtet:**
  - **Huelse:** kopfueber, die Lippe liegt auf dem Bett, der Fuss wird zuletzt gedruckt.
  - **Stoessel:** Gewindehals auf dem Bett, Stift oben. Kleine Aufstandsflaeche (Ø 5 mm),
    deshalb **Brim (5 mm)** verwenden.
  - **Knopf:** Dach (glatte Seite) auf dem Bett, Gewindeoeffnung oben.
  - **Klemmmutter:** flach.
- Innengewinde (Mutter, Knopf) haben je 0,15 mm Druckspiel eingerechnet. Klemmt es, kurz
  aufschrauben und wieder abdrehen; bei zu viel Spiel `gew_spiel` / `gew_spiel_m5` in
  `taster_bauen.py` verkleinern.
- Der Stoessel muss in der Huelsenbohrung leicht gleiten. Wenn nicht: Bohrung mit einem
  7-mm-Bohrer von Hand nachziehen oder `koerper_d` verkleinern.

## Einbauen

1. Case **noch nicht** ans Holz schrauben.
2. **Stoessel von unten in die Huelse schieben**: Stift zuerst nach unten, der Hals kommt
   oben durch die Lippe (Stoessel liegt nach oben im Rohr).
3. **Huelse mit Stoessel von unten durch das Holzloch stecken** (Fuss unter dem Holz).
4. **Klemmmutter** von oben aufschrauben und handfest anziehen (Huelse dabei am Fuss
   festhalten).
5. **Knopf** auf den Gewindehals schrauben, zunaechst bis ca. 0,7 mm Luft zur Huelse.
6. Case mit den beiden Schrauben an das Holz schrauben, micro:bit einschieben. Der Taster
   faehrt dabei in die Aussparung im Fuss.

## Hub einstellen

1. Den **Knopf** so drehen, dass zwischen Knopf-Unterseite und Huelsenoberkante etwa
   0,5 - 0,8 mm Luft bleiben (ca. eine halbe Umdrehung Gewinde = 0,4 mm).
2. Testen. Klickt der Taster nicht, mehr Luft (Knopf aufdrehen). Wird der Taster nie
   losgelassen oder schaltet dauernd, stimmt die Stiftlaenge nicht - siehe naechster
   Abschnitt.
3. Mit einem Tropfen Sekundenkleber oder Nagellack am Knopfgewinde sichern, wenn der Knopf
   nicht mehr verstellt werden soll.

**Bekanntes Restspiel:** In Ruhe hat der Stoessel etwa 0,4 mm Auf-und-ab-Spiel (er liegt
nur auf dem Taster). Das ist Absicht als Toleranz fuer einen etwas hoeheren Taster als
angenommen. Seitlich fuehrt die 11,75 mm lange Bohrung; das Spiel dort betraegt 0,2 mm je
Seite bei ~12 mm Fuehrungslaenge (in Version 1 waren es 6 mm).

## Wenn der Stift nicht passt

Die Laenge des Druckstifts (`stift_l`, 0,9 mm) gilt fuer einen Taster, dessen Oberkante
0,05 mm unter der Holzunterseite liegt. Liegt der Taster tatsaechlich hoeher, presst der
Stift ihn schon in Ruhe (Dauerdruck): `stift_l` kleiner machen und den Stoessel neu drucken
(`taster_bauen.py`). Liegt er tiefer, den Knopf weiter aufdrehen oder `stift_l` groesser
machen.

## Was in Fusion geprueft wurde

Gegen das echte Case-Modell (`Microbit_V2_Case`), einen 6-mm-Holzdeckel mit rundem
Ø 12,4 mm-Loch an den Positionen aus `deck_mit_microbit.dxf` und einen angenommenen
6 x 6 mm-Taster:

| Pruefung | Ergebnis |
|---|---|
| Huelse im Case, im Holzloch, gegen Taster | 0 mm3 Durchdringung |
| dasselbe mit Lageabweichung +-0,5 mm in X und Y (Handmass-Toleranz) | 0 mm3 |
| Seitliches Spiel der Huelse im Holzloch | ca. 0,2 mm je Seite |
| Stoessel in der Huelse: Ruhe / oben an der Lippe / 0,25 mm gedrueckt / 0,9 mm gedrueckt | 0 mm3 |
| Wandstaerke der Huelse am Gewindegrund | 1,07 mm |
| Klemmmutter auf der Huelse bei 4 mm und 9 mm Holz | 0,000 mm3 (Gewinde greift) |
| Knopf auf dem Hals bei 0 / 0,7 / 1,5 mm Luft | 0,000 mm3 |
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
| Holzdicke | bis 9 mm, Huelse 15 mm lang | `huelse_l` (= Holzdicke + 6) |

Die Tasterhoehe (Rahmenhoehe 14,55 mm) folgt aus dem Fusion-Parameter `d110` und der
micro:bit-Angabe "Taster 4,55 mm ueber der Platine"
([tech.microbit.org](https://tech.microbit.org/hardware/)).

**Bauhoehe:** Bei 6 mm Holz steht die Huelse 9 mm ueber dem Holz, der Knopf oben etwa
18 mm. Fuer duennes Holz die Huelse kuerzen (`huelse_l` = Holzdicke + 6); Stoessel und
Knopfhals passen sich im Skript automatisch an.

## Neu erzeugen

[`taster_bauen.py`](taster_bauen.py) ist die parametrische Definition. In Fusion ein
**leeres** Design oeffnen, Skript ausfuehren (Dienstprogramme > Add-Ins > Skripte);
es baut die fuenf Koerper, prueft auf Streukoerper und schreibt die STL-Dateien
neben das Skript (Huelse und Stoessel kopfueber fuer den Druck). Parameter stehen im
Block `P` am Anfang.
