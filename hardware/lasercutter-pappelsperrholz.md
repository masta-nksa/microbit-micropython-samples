# Lasercutter: Pappelsperrholz 6 mm - Parameter & LightBurn-Kurzanleitung

Schnitt- und Gravurwerte fuer das Serienmaterial (Box + alle `cad/ausschnitt.dxf`
in diesem Repo), plus eine kurze LightBurn-Einfuehrung fuers Einstellen dieser
Werte. Gilt fuer die Maschine **Max-1060R, 100 W CO2** (Ruida-Controller,
LightBurn-Geraeteprofil `omtgech 1060r`, Arbeitsflaeche 1000 x 600 mm).

> **Sicherheit:** Lasercutter nur nach Einweisung und unter Aufsicht benutzen.
> Nur freigegebene Materialien verwenden, Laser waehrend des Betriebs nie
> unbeaufsichtigt lassen. **Nie ueber 80 % Max Power** (Roehrenlebensdauer),
> Kuehlwasser 18-22 °C, Maschine **nie ohne Kuehlung** betreiben. Keine
> Leistungswerte aus dem Internet uebernehmen - nur die hier freigegebenen
> Werte, Aenderungen nur nach Ruecksprache mit der Betreuungsperson.

## Material

**6 mm Pappelsperrholz** (Nennmass). Reales Blatt an 5 Stellen mit dem
Messschieber pruefen - der **groesste** gemessene Wert zaehlt fuer die
Konstruktion, nicht der Nennwert. Aktuell gemessen: **5.5 mm**. Weicht ein
neu gekauftes Blatt (andere Charge/Sorte) merklich ab, vor der Serie einen
kurzen Testschnitt mit den Werten unten machen, nicht blind uebernehmen.

## Bestaetigte Schnitt-Ebene (Cut)

| Parameter | Wert |
|---|---|
| Fokus | **+2 mm ins Material** (Z-Offset am Layer, nach Autofokus) |
| Geschwindigkeit | **16 mm/s** |
| Leistung | **Max 55 % / Min 45 %** |
| Durchgaenge | **1** |
| Kerf | **0.25 mm**, bereits **in der Geometrie** kompensiert (alle `ausschnitt.dxf` und die Box-Teile in diesem Repo) |
| LightBurn-Schnittversatz | **0 - nichts einstellen** (Kerf steckt schon in der Zeichnung, sonst wird doppelt kompensiert) |

**Status: verifiziert.** Cross-bestaetigt in mehreren realen LightBurn-Projekten
fuer diese Box (u. a. Zinken-Testteil: Teile liessen sich sauber herausdruecken).

## Gravur-Ebenen

| Modus | Einsatz | Geschwindigkeit | Leistung | Sonstiges | Status |
|---|---|---:|---|---|---|
| **Image** | Fotos, Graustufenbilder | 300 mm/s | Max 12.5 % / Min 10 % | Line Interval 0.12 mm | aus echtem Projekttest, vor Serie auf Reststueck pruefen |
| **Fill** | Text, Logos, Flaechen | 250 mm/s | Max 15 % / Min 10 % | Line Interval 0.1 mm | **nur Startwert, unbestaetigt** - erst testen |
| **Line** | Markierungen, Testbeschriftung | 150 mm/s | 12 % | - | **nur Startwert, unbestaetigt** |

Der 100-W-Laser braucht fuer Gravuren **deutlich** weniger Leistung als fuers
Schneiden - die hohe Maximalleistung der Maschine ist kein Grund, mit hoher
Leistung zu gravieren. Ist das Ergebnis zu hell: Geschwindigkeit und Leistung
vorsichtig in kleinen Schritten anpassen, immer erst am Reststueck testen.

---

## LightBurn-Kurzanleitung

### Was ist LightBurn?

LightBurn ist die Software zum Vorbereiten und Senden von Dateien an den
Lasercutter - Formen, Text, Bilder und importierte Vektorgrafiken (z. B. die
`.dxf`-Dateien aus diesem Repo).

### Die wichtigsten Bereiche

- **Arbeitsbereich:** alle Objekte werden hier erstellt/angeordnet (max. 1000 x 600 mm).
- **Werkzeugleiste links:** Formen, Linien, Text, Auswahl.
- **Farbpalette unten:** weist Objekten eine Bearbeitungsebene (Layer) zu.
- **Cuts/Layers rechts:** hier werden Geschwindigkeit, Leistung usw. je Ebene festgelegt - **hier kommen die Werte von oben rein.**
- **Laser-Fenster rechts:** Laser steuern, Rahmen-Test, Start.

Die Farben zeigen **nicht** die Farbe des fertigen Werkstuecks - jede Farbe
ist nur eine Ebene mit eigenen Einstellungen (Schneiden, Konturgravur,
Flaechengravur, Bildgravur ...).

Hilfetipp: Maus ueber eine Funktion halten und **F1** druecken oeffnet die
passende LightBurn-Hilfeseite.

### Eine Ebene einstellen (Leistung, Geschwindigkeit, Fokus)

1. Objekt auswaehlen, unten eine Farbe anklicken (neue Ebene) oder eine
   bestehende Farbe waehlen.
2. Im Fenster **Cuts/Layers** auf die Ebene **doppelklicken**.
3. **Mode** waehlen: `Line` (Schneiden/Kontur), `Fill` (Flaeche/Text), `Image`
   (Fotos/Pixelbilder).
4. **Speed**, **Max Power**, **Min Power**, **Passes** aus der Tabelle oben
   eintragen - fuer den jeweiligen Zweck (Schneiden vs. Gravieren).
5. **Fokus/Z-Offset:** nur sichtbar, wenn die Z-Achse im Geraeteprofil
   aktiviert ist. Erst **Autofokus** einmal ausfuehren, danach **nicht mehr
   manuell nachfokussieren** - stattdessen den Z-Offset-Wert aus der Tabelle
   oben am Layer eintragen (Z-Offset ist eine **Layer-Eigenschaft**, keine
   Objekteigenschaft). Zusaetzlich **"Relative Z moves only"** in den
   Geraeteeinstellungen aktivieren, sonst faehrt die Maschine auf absolute
   statt relative Koordinaten.

**Grundregel:** Gravieren = hoehere Geschwindigkeit, niedrigere Leistung.
Schneiden = niedrigere Geschwindigkeit, hoehere Leistung. Die exakten Werte
haengen von Material, Dicke, Fokus und Linse ab - deshalb nur die oben
freigegebenen Werte verwenden, nicht raten.

**Min Power** ist die Leistung bei Geschwindigkeit Null. Der Controller
interpoliert linear bis Max Power bei Sollgeschwindigkeit - das wirkt sich in
Ecken, an Linienanfaengen und auf kurzen Segmenten aus (der Kopf beschleunigt
dort noch). Zu niedriges Min: kleine Loecher/Zinken kommen nicht durch, obwohl
lange Kanten sauber schneiden. Faustregel: Min = Max minus 5-15 Prozentpunkte.

### Datei anlegen/importieren

- Neues Projekt: **Datei -> Neu**
- DXF/SVG importieren: **Datei -> Importieren** (z. B. eine `cad/ausschnitt.dxf`
  aus diesem Repo)
- Speichern: **Datei -> Speichern unter**

Nach **jedem** Import zuerst die Layerliste durchgehen und pruefen, ob jede
Ebene die richtigen Werte hat - siehe naechster Abschnitt.

### Groesse/Position pruefen

Ausgewaehltes Objekt oben: **X/Y** (Position), **Breite/Hoehe** (Abmessung),
Schloss-Symbol haelt das Seitenverhaeltnis. Immer kontrollieren, dass in **mm**
gearbeitet wird und das Motiv innerhalb 1000 x 600 mm liegt.

### Wichtige Tastenkombinationen

| Aktion | Taste |
|---|---|
| Mehrere Objekte auswaehlen | Shift halten |
| Loeschen | Entf |
| Rueckgaengig | Strg + Z |
| Duplizieren | Strg + D |
| Gruppieren | Strg + G |
| Verschweissen (eine zusammenhaengende Form) | Strg + W |

Gruppieren behaelt einzelne Objekte, Verschweissen macht daraus eine Form.

### Bilder gravieren

1. Bild importieren, auf Zielgroesse bringen - **nicht** zu stark vergroessern
   (sonst pixelig/unscharf).
2. Modus **Image**, Werte aus der Tabelle oben.
3. Bei Bedarf Helligkeit/Kontrast/Schaerfe anpassen, Vorschau pruefen.
4. Scharfe, kontrastreiche Bilder ohne unruhigen Hintergrund funktionieren am
   besten. Fuer Logos/SW-Grafiken meist ein Dither-Modus sinnvoll.
5. **Line Interval** (Zeilenabstand): zu klein = zu dunkel/unscharf, zu gross
   = sichtbare Luecken. Testbereich ca. 0.08-0.20 mm (120-300 DPI) - fuer
   unser Material siehe Tabelle oben (0.12 mm).

## Die teuersten Fallstricke

- **Gravur-Layer vergessen umzustellen.** Passiert leicht nach einem Import:
  Text/Bild laeuft dann mit voller Schnittleistung und wird verkohlt durch
  das Holz gefraest. Nach **jedem** Import die Layerliste durchgehen.
- **Spiegelung im Geraeteprofil** (`MirrorX`/`MirrorY`): auf dem Werkstueck
  kann eine Gravur seitenverkehrt/spiegelverkehrt herauskommen, obwohl sie in
  LightBurn richtig aussieht. Vor der ersten Gravur mit einem asymmetrischen
  Testobjekt pruefen (betrifft v. a. Text/Beschriftungen, bei symmetrischen
  Schnittteilen egal).
- **DXF-Text ist unzuverlaessig beim Import** - Beschriftungen lieber direkt
  in LightBurn setzen statt im DXF mitzuliefern.
- **Mehrfachdurchgaenge** sind bei 100 W ein Notnagel, kein Standardwerkzeug -
  nur wenn man sonst ueber 80 % Leistung muesste. Bei duennem Material
  ungeeignet (Teil kann nach dem 1. Durchgang verrutschen).
- **Verrussung:** Platte 10-20 mm ueber die Wabe stellen (Naegel/Winkel unter
  die Ecken) ist die wirksamste Massnahme. Leistung senken hilft **nicht** -
  das erzwingt langsameres Fahren und damit mehr Verkohlung.
