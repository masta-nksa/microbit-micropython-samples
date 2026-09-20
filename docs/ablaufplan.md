---
title: Ablaufplan Impulswoche 2026
---

# Ablaufplan Impulswoche 2026

## Rahmen

Montag bis Donnerstag sind je 5,5 Stunden Kernarbeitszeit eingeplant (09:00 bis 11:45 und 13:15 bis 16:00), am Freitag bleibt rund eine Stunde zum Fertigstellen.

| Zeit (Mo bis Do) | Was | Verbindlich? |
| --- | --- | --- |
| 08:45 bis 09:00 | Gleitzeit: ankommen, Material holen, Laptop starten | nein |
| 09:00 bis 09:10 | Startrunde: Tagesziel, offene Fragen | ja |
| 09:10 bis 11:45 | Arbeitsblock 1 (Znueni-Pause frei, ca. 10:15) | ja |
| 11:45 bis 13:15 | Mittagspause |  |
| 13:15 bis 13:25 | Kurzrunde: Stand und Probleme | ja |
| 13:25 bis 15:40 | Arbeitsblock 2 | ja |
| 15:40 bis 16:00 | Aufraeumen und Tageslog; Zug um 16:00 moeglich, gehen ab 15:45 nach dem Aufraeumen | ja |

Inputs der Lehrperson gibt es nur in den Startrunden und bis 14:30, nie nach 15:30. So verpasst niemand etwas, der frueh zum Zug muss.

## Wochenuebersicht

Die Woche hat zwei Teile: ein Vorprojekt mit einer vorbereiteten Box (Montag bis Dienstagmittag) und danach das eigene Raetsel, das aus dem elektronischen Tresor eine Mysterybox macht. Jeder Tag endet mit einem Meilenstein.

| Tag | Vormittag | Nachmittag | Meilenstein am Abend |
| --- | --- | --- | --- |
| Montag | Einstieg mit Teaser, Sicherheit, Box zusammenbauen, Servo mit Taste A und B, ab dann Sensoren | Sensoren des micro:bit (z. B. Neigungsfolge), wer fertig ist, loetet den LED-Strip | Box steht, Servo oeffnet und schliesst per Code, Neigungsfolge ausprobiert |
| Dienstag | LED-Strip (wer noch nicht) oder 4-Digit-Anzeige dazunehmen, einfache Erweiterungsaufgabe | Vorprojekt abschliessen, eigene Raetselidee planen, Display, Drehregler oder Naeherungssensor fuer Interessierte | Vorprojekt fertig, Raetselidee skizziert |
| Mittwoch | Raetsel programmieren, Hardware einbauen | Raetsel programmieren, Erweiterung integrieren | Raetsel ist komplett spielbar |
| Donnerstag | Fehler beheben, Dauertest, Playtest bei einer anderen Gruppe | Doku, Praesentation vorbereiten, Generalprobe | Box und Praesentation stehen |
| Freitag | 09:00 bis 10:00 Fertigstellen, ab 10:00 Praesentationen | Abschluss ab 12:00 | Alle Boxen vorgestellt |

## Basis-Set und Kombinationen

Die Basis laeuft ohne Breakout-Board, T-Steckbrett oder Klemmen: Servo und LED-Strip (oder 4-Digit-Anzeige) belegen zwei bis drei der drei grossen Pads, Eingaben kommen von den Tasten und Sensoren des micro:bit selbst.

| Komponente | Rolle | Speisung |
| --- | --- | --- |
| micro:bit in gedruckter Halterung | Steuerung und Eingabe: Tasten A und B, Neigung, Kompass, Lichtsensor, Logo-Touch; Ausschnitt im Deckel liegt bereit | 2xAA-Fach direkt am Stecker |
| Servo mit Schliessmechanismus | Verschluss, immer angeschlossen | 3xAA-Fach (4,5 V) |
| LED-Strip | Anzeige, Anschlusspads und Kabel werden geloetet | 3xAA-Fach |
| 4-Digit-Anzeige | Alternative zum LED-Strip | 3V-Pad des micro:bit |

| Kombination | Belegung | Bemerkung |
| --- | --- | --- |
| Servo und LED-Strip | Servo P0, LED-Strip P1 (im Sample pin0 durch pin1 ersetzen), P2 bleibt frei | reicht mit einem Pad Reserve |
| Servo und 4-Digit-Anzeige | Servo P0, Anzeige CLK P1 und DIO P2 | reicht genau, die Samples laufen unveraendert |
| Servo, LED-Strip und 4-Digit-Anzeige | vier Signale | nicht ohne Breakout-Board |

Alle Speisungen brauchen eine gemeinsame Masse. Auf dem einen GND-Pad treffen dann micro:bit, Servo-Fach und LED-Strip zusammen, das geht mit mehreren Ringkabelschuhen auf einer M3-Schraube oder mehreren Krokoklemmen. Ein Elko (470 bis 1000 uF) am 3xAA-Fach faengt den Anlaufstoss des Servos ab. Externer Taster, Drehregler und Naeherungssensor brauchen weitere Pads und gehoeren zur Erweiterungsstufe ab Dienstagnachmittag.

## Fester Ablauf fuer Gruppen, die klare Schritte brauchen

Fuer Schuelerinnen und Schueler, die einen genauen, festen Ablauf brauchen, gibt es auf der Samples-Website die Seite [Workflow](workflow.md) mit elf Stationen fuer Montag und Dienstagvormittag. Jede Station hat ein Ziel und ein klares "Fertig, wenn", es wird immer nur eine Station bearbeitet.

| Nr | Station | Sample |
| --- | --- | --- |
| 1 | Editor und Kabel | setup |
| 2 | Knoepfe A und B | a-b-zaehler |
| 3 | Neigung messen | wasserwaage |
| 4 | Servo auf dem Tisch | zwei-stellungen |
| 5 | Box zusammenbauen | Anleitung der Lehrperson |
| 6 | Endlagen messen | endlagen-kalibrieren |
| 7 | Box oeffnen und schliessen | box-startprogramm |
| 8 | 4-Digit-Anzeige anschliessen | zahl-anzeigen |
| 9 | Anzeige als Zaehler | zaehler |
| 10 | Codeeingabe Stufe 1: Zahl einstellen, mit dem Logo bestaetigen | eigene Aufgabe |
| 11 | Codeeingabe Stufe 2: Zahl, dann Neigungsfolge | eigene Aufgabe |

Der Servo (P0) bleibt ab Station 4, die Anzeige (P1, P2) ab Station 8 angeschlossen, es wird nie umgesteckt. Die Reihenfolge von Station 4 und 5 (Servo erst frei testen, dann in die Mechanik setzen) ist ein Vorschlag und laesst sich anpassen.

## Montag, 21.09.: Box bauen und Komponenten kennenlernen

Alle arbeiten im eigenen Tempo dieselbe Kette ab: Box bauen, Servo mit Taste A und B, Sensoren des micro:bit. Am Abend steht die Box, der Servo oeffnet und schliesst per Code, und die Sensoren sind ausprobiert. Der Deckelausschnitt fuer den micro:bit ist schon gelasert, also beginnen alle mit dem Zusammenbau.

| Zeit | Programm |
| --- | --- |
| 09:00 bis 09:40 | Begruessung, Idee (vom Tresor zur Mysterybox), Wochenplan, Zweiergruppen; die Lehrperson zeigt die einfache Beispielbox, als Teaser eine Box, die sich nur nach einer bestimmten Neigungsfolge oeffnet |
| 09:40 bis 10:00 | Sicherheit: Batterien (Kurzschluss), Werkplatzregeln; die Loetregeln folgen kurz vor dem ersten Loeten |
| 10:00 bis 11:45 | Aufbauanleitung der Lehrperson: Box zusammenstecken, Schliessmechanismus und micro:bit-Halterung einbauen, der Servo laeuft zuerst ohne Zahnrad (Besprechung durch die Lehrperson); schnelle Gruppen sind nach etwa 45 Minuten fertig und gehen direkt weiter |
| sobald die Box steht | Servo (Signal an P0) am 3xAA-Fach anschliessen, Endlagen messen (endlagen-kalibrieren), dann mit dem box-startprogramm (laeuft so, mit Ideen zum Ausbauen) per Taste A und B oeffnen und schliessen |
| sobald das Basisprogramm laeuft | Sensoren des micro:bit, ohne etwas umzustecken: Neigung, Kompass, Lichtsensor, Logo-Touch; Aufgabe: eine Neigungsfolge oeffnet die Box |
| 13:15 bis 15:40 | weiter im eigenen Tempo: Basisprogramm und Sensoraufgabe abschliessen; wer fertig ist, loetet den LED-Strip (nach der Loeten-Seite), schliesst ihn an P1 an und probiert ihn aus |
| 15:40 bis 16:00 | Aufraeumen, Tageslog |

## Dienstag, 22.09.: Vorprojekt abschliessen, Raetsel planen

Bis Dienstagmittag ist das Vorprojekt fertig, danach beginnt das eigene Raetsel. Wer schnell ist, kann die Erweiterungen schon frueher nutzen, freigegeben werden sie ab 13:15.

| Zeit | Programm |
| --- | --- |
| 09:00 bis 09:15 | Startrunde |
| 09:15 bis 10:30 | LED-Strip loeten und anschliessen (wer es am Montag nicht geschafft hat), alternativ 4-Digit-Anzeige, Codebeispiele von GitHub ausprobieren |
| 10:30 bis 11:45 | Erweiterungsaufgabe aus den Codebeispielen: Neigungsfolge oder Tastencode oeffnet den Servo, der LED-Strip zeigt den Zustand |
| 13:15 bis 13:45 | Vorprojekt-Runde: jede Gruppe zeigt ihren ersten Schliessmechanismus 2 Minuten an ihrem Tisch (Was macht die Box? Was war schwierig? Welcher Sensor?), die anderen gehen herum; danach Kurzinput zu den Raetselmoeglichkeiten |
| 13:45 bis 15:40 | Eigene Raetselidee skizzieren (Ablauf, Eingaben, Anzeigen), passende Erweiterung waehlen: Display 1.8 Zoll, Drehregler mit Button oder Naeherungssensor, erste Tests |
| 15:40 bis 16:00 | Aufraeumen, Tageslog |

## Mittwoch, 23.09.: Eigenes Raetsel umsetzen

Der ganze Tag gehoert dem eigenen Raetsel, am Abend ist es komplett durchspielbar. Laser und 3D-Druck sind nur noch fuer Zusatzteile noetig, die Fristen stehen im Abschnitt dazu.

| Zeit | Programm |
| --- | --- |
| 09:00 bis 09:15 | Startrunde, Zwischenstand der Raetselideen |
| 09:15 bis 11:45 | Raetsel programmieren, Komponenten in die Box einbauen und befestigen |
| 13:15 bis 15:40 | Erweiterung integrieren, Raetsel und Verschluss zusammenbringen, erster Durchlauf von Anfang bis Ende |
| 15:40 bis 16:00 | Aufraeumen, Tageslog |

## Donnerstag, 24.09.: Testen und Praesentation vorbereiten

Ab Donnerstagmittag wird nichts Neues mehr angefangen, dann zaehlen nur noch Stabilitaet und die Praesentation.

| Zeit | Programm |
| --- | --- |
| 09:00 bis 09:15 | Startrunde |
| 09:15 bis 11:45 | Fehler beheben, Kabel ordnen, Dauertest mit 20 Oeffnungszyklen, Playtest: eine andere Gruppe spielt das Raetsel |
| 13:15 bis 14:30 | Lernjournal abschliessen, Kurzpraesentation vorbereiten (7 Minuten: Demo, eine Schwierigkeit, eine Erkenntnis) |
| 14:30 bis 15:30 | Generalprobe vor einer anderen Gruppe, Rueckmeldung, frische Batterien einlegen |
| 15:30 bis 16:00 | Werkplatz groesstenteils aufraeumen, Box sicher wegstellen |

Wer am Donnerstag nicht fertig wird, entscheidet um 14:30, was er am Freitag zeigt (Teilfunktion statt vollstaendiges Raetsel), damit der Freitag nicht in Hektik kippt.

## Freitag, 25.09.: Fertigstellen, Vorstellen, Abschluss

Die Praesentationen laufen von 10:00 bis 11:10, das Ende ist fuer 11:40 geplant und laesst 20 Minuten Puffer bis zum Abschluss um 12:00.

| Zeit | Programm |
| --- | --- |
| 08:45 bis 09:00 | Gleitzeit, ankommen |
| 09:00 bis 09:50 | Letzte Korrekturen, Funktionstest, frische Batterien, Box am Praesentationsplatz aufstellen |
| 09:50 bis 10:00 | Reihenfolge ziehen, Technik pruefen |
| 10:00 bis 11:10 | Praesentationen: 7 Gruppen zu je 10 Minuten (7 Minuten Demo, 3 Minuten Fragen und Wechsel) |
| 11:10 bis 11:25 | Rueckblick: was hat funktioniert, was wuerden wir anders machen (kurzes Feedback-Formular) |
| 11:25 bis 11:40 | Material einsammeln und Arbeitsplaetze aufraeumen |
| 11:40 bis 12:00 | Puffer, danach Abschluss |

## Fristen fuer Laser und 3D-Druck

Laserteile sind bis Mittwochnachmittag gelasert, spaetestens bis Donnerstagnachmittag. 3D-Druckteile muessen bis Donnerstag in Auftrag sein, damit sie ueber Nacht auf Freitag gedruckt werden koennen, das ist schon riskant.

| Was | Ziel | Spaeteste Frist | Bemerkung |
| --- | --- | --- | --- |
| Laserteile | Mittwochnachmittag | Donnerstagnachmittag | danach bleibt Zeit fuer Einbau und Generalprobe |
| 3D-Druck | so frueh wie moeglich | Donnerstag, Druck ueber Nacht | ein Fehldruck laesst keinen zweiten Versuch mehr zu, am Freitag bleibt nur Einbauen und Testen |

## Hinweise

- **Gleitzeit:** Verbindlich sind nur die Startrunden um 09:00 und 13:15 sowie das Aufraeumen ab 15:40. Was in den Startrunden gesagt wird, steht zusaetzlich als Tagesziel an der Tafel.
- **Erweiterungen:** Display, Drehregler und Naeherungssensor gibt es erst ab Dienstag 13:15 und nur fuer Interessierte.
- **Nicht geplant:** Fixe Pausen am Vormittag und Nachmittag, jede Gruppe legt sie selbst, solange der Arbeitsplatz aufgeraeumt bleibt.
