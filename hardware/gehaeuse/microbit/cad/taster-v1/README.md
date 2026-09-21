# Taster Version 1 - Gewindebolzen mit Kontermutter (3D-Druck)

> **Version 1 (festgehalten).** Es gibt eine Weiterentwicklung mit fest verschraubter
> Fuehrungshuelse: [Version 2](../taster-v2/README.md). Version 1 bleibt als Alternative
> mit kleinerem Holzloch (Ø 10,4 mm) und 3 statt 4 Teilen pro Taster erhalten; ihr Nachteil
> ist das Wackeln des Bolzens im Loch (nur die Holzdicke fuehrt, ca. 0,25 mm Spiel je Seite).

Verlaengerung fuer die micro:bit-Taster **A** und **B**, damit man sie durch den
Holzdeckel mit dem Finger druecken kann - ohne Schraube. Die Hoehe ist ueber ein
Gewinde **stufenlos einstellbar**, der Taster funktioniert also auch mit anderer
Holzdicke (ausgelegt fuer **4 bis 9 mm**, aktuell 6 mm). Eine Kontermutter sichert
die eingestellte Hoehe, der Bolzen fuehrt im runden Loch.

> **Status: nicht am echten Teil getestet.** Passung im Case, Holzloch und
> Gewinde sind in Fusion numerisch geprueft (siehe unten). Die Tasterflaeche
> ist aber **angenommen** (6 x 6 mm, Oberkante buendig zur Holzunterseite) -
> vor dem Serien-Druck einen Testdruck machen und die Annahmen nachmessen.

## Teile (fuer beide Taster A und B)

| Datei | Anzahl | Beschreibung |
|---|---|---|
| [`stoessel_links.stl`](stoessel_links.stl) | 1x | Stoessel fuer den Taster nahe der linken Rahmenwand |
| [`stoessel_rechts.stl`](stoessel_rechts.stl) | 1x | gespiegelte Variante fuer die rechte Seite |
| [`kontermutter.stl`](kontermutter.stl) | 2x | Sechskantmutter Tr10x2: Anschlag und Sicherung |
| [`kappe.stl`](kappe.stl) | 2x | Drehknopf mit Innengewinde Tr10x2 |
| [`deck_mit_microbit_taster_rund.dxf`](deck_mit_microbit_taster_rund.dxf) | - | Deckel-DXF mit runden Loechern |

Woran man links/rechts erkennt: Der flache **Fuss zeigt immer von der naechsten
Rahmenwand weg zur Mitte** (zum LED-Fenster). Im Zweifel beide Stoessel
probeweise einlegen - der falsche stoesst an der Rahmenwand an.

Aufbau eines Stoessels (von unten nach oben): flacher Fuss (0,8 mm) unter dem Holz mit
Aussparung fuer den Taster, zwei Haltearme, Druckzapfen (drueckt auf die Tastermitte)
und der Gewindebolzen Tr10x2 mit glattem Fuehrungszapfen am Ende. Der Fuss ist groesser
als das Loch und haelt den Stoessel unter dem Holz; ueber dem Holz sitzen Kontermutter
und Kappe.

## Holz: rundes Loch statt Quadrat

[`deck_mit_microbit_taster_rund.dxf`](deck_mit_microbit_taster_rund.dxf) ist deine
`deck_mit_microbit.dxf` mit einer einzigen Aenderung: die beiden 10 x 10 mm-Quadrate
fuer A/B sind durch **Kreise Ø 10,4 mm** an derselben Mitte ersetzt (r = 5,2). Der
Bolzen (Ø 10) hat darin ca. 0,25 mm Spiel und wird auf der ganzen Holzdicke gefuehrt.
Loecher zuerst an einem Reststueck schneiden und mit dem gedruckten Bolzen pruefen -
der Laserstrahl macht Loecher je nach Kerf etwas groesser. Die Bolzen stellen das
Mass, nicht das Loch.

Warum nicht Ø 8,6 wie zuerst vorgeschlagen: Der Taster (6 x 6 mm, Diagonale 8,5 mm)
fuellt so ein Loch fast aus, fuer die Haltearme bliebe nichts uebrig.

## Drucken

- Material PLA oder PETG, Duese 0,4 mm, Schichthoehe 0,15 - 0,2 mm, **ohne Stuetzen**.
- **Stoessel:** Fuss flach auf dem Druckbett (so ist die STL ausgerichtet).
- **Kappe:** Dach (glatte Seite) auf dem Druckbett, Gewindeoeffnung nach oben.
- **Kontermutter:** flach, wie ausgerichtet.
- 3 Wandlinien, Fuellung >= 40 %.
- Die Innengewinde (Kappe, Mutter) haben 0,15 mm Druckspiel je Flanke eingerechnet.
  Klemmt es, kurz aufschrauben und wieder abdrehen; bei zu viel Spiel in
  `taster_bauen.py` `gew_spiel` verkleinern.

## Einbauen

1. Case **noch nicht** ans Holz schrauben.
2. Holz mit der Aussenseite nach oben legen. Stoessel **von unten** durch das
   runde Loch stecken (Bolzen nach oben).
3. Kontermutter von oben auf den Bolzen schrauben, bis sie auf dem Holz aufliegt.
   Sie haelt den Stoessel jetzt im Holz.
4. Case mit den beiden Schrauben an das Holz schrauben.
5. micro:bit in den Case schieben. Der Taster faehrt dabei in die Aussparung im
   Fuss des Stoessels.
6. Hoehe einstellen (naechster Abschnitt), dann Kappe aufschrauben.

## Hoehe einstellen

1. Die **Mutter** ist der Anschlag: auf das Holz zudrehen (der Stoessel liegt dabei
   auf dem Taster), dann **eine ganze Umdrehung aufdrehen**. Steigung 2 mm =
   2 mm Leerweg; der Taster schaltet schon nach wenigen Zehntelmillimetern.
2. **Kappe** von oben bis auf die Mutter schrauben und **fest gegen die Mutter
   kontern** (Mutter an den Flaechen festhalten, damit sie nicht mitdreht).
3. Testen. Klickt es nicht, Schritte 1-2 mit weniger Leerweg wiederholen; bleibt der
   Taster dauernd gedrueckt, mehr Leerweg (aufdrehen).

Bei anderer Holzdicke: Schritt 1 und 2 wiederholen, sonst ist nichts zu tun.
Bei 6 mm Holz ragt die Kappe insgesamt etwa 16 mm ueber das Holz (2 mm Leerweg +
3 mm Mutter + 11 mm Kappe) - das ist der Preis fuer den Verstellbereich.

## Was in Fusion geprueft wurde

Gegen das echte Case-Modell (`Microbit_V2_Case`), einen 6-mm-Holzdeckel mit rundem
Ø 10,4 mm-Loch an den Positionen aus `deck_mit_microbit.dxf` und einen angenommenen
6 x 6 mm-Taster:

| Pruefung | Ergebnis |
|---|---|
| Stoessel im Case, oben / in Ruhe / gedrueckt | 0 mm3 Durchdringung |
| dasselbe mit Lageabweichung +-0,5 mm in X und Y (Handmass-Toleranz) | 0 mm3 |
| Stoessel im Holzloch (6 mm Holz), Stoessel gegen Taster | 0 mm3 |
| Seitliches Spiel des Bolzens im Loch | ca. 0,25 mm je Seite |
| Gewinde Mutter und Kappe <-> Stoessel bei 4 / 6 / 9 mm Holz (beste Drehlage) | 0,000 mm3 |
| STL-Netze | geschlossen, keine offenen Kanten |

Die rechte Variante hat zur Rahmenwand hin nur zwischen 0,5 und 1 mm Reserve (bei
+1 mm Versatz Richtung Wand stoesst sie mit < 1 mm3 an) - bei dem handgemessenen
Ausschnitt kann das relevant werden.

## Annahmen, die nachgemessen werden sollten

| Annahme | Wert | Wo aendern |
|---|---|---|
| Tasterflaeche (X und Y) | 6,0 mm | `taster` |
| Taster-Oberkante | 0,05 mm unter der Holzunterseite (Rahmenhoehe 14,55 mm) | `d_taster`; Abweichungen gleicht die Mutter aus |
| Tastermitte | Mitte des Holzlochs (X 8,2 / 48,4 mm, Y 9,74 mm im Case) | Loch im DXF, `u_min`/`u_max` |
| Loch im Holz | rund Ø 10,4 mm | `loch_d`, `fuehr_r` |
| Holzdicke | 4 - 9 mm | `holz_min`, `holz_max` |

Falls der Taster groesser als 6 mm ist, stoesst er an der Fussaussparung an -
dann `taster` erhoehen. Die Tasterhoehe (Rahmenhoehe 14,55 mm) folgt aus dem
Fusion-Parameter `d110` und der micro:bit-Angabe "Taster 4,55 mm ueber der
Platine" ([tech.microbit.org](https://tech.microbit.org/hardware/)).

## Neu erzeugen

[`taster_bauen.py`](taster_bauen.py) ist die parametrische Definition. In Fusion ein
**leeres** Design oeffnen, Skript ausfuehren (Dienstprogramme > Add-Ins > Skripte);
es baut die vier Teile, prueft auf Streukoerper und schreibt die STL-Dateien neben
das Skript. Parameter stehen im Block `P` am Anfang.
