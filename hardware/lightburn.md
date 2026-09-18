# LightBurn: Bedienung & alle Ausschnitt-Dateien

Allgemeine LightBurn-Bedienung (Software zum Vorbereiten und Senden von
Dateien an den Lasercutter) sowie eine Uebersicht **aller** in diesem Repo
vorhandenen Ausschnitt- und Halterungs-Dateien. Material-spezifische
Schnitt-/Gravurwerte (Speed/Power/Fokus) stehen separat:
[lasercutter-pappelsperrholz.md](lasercutter-pappelsperrholz.md).

## Alle Ausschnitt- und Halterungs-Dateien

| Bauteil | Kategorie | Datei | Zweck |
|---|---|---|---|
| [ds425-pushbutton](input/ds425-pushbutton/) | input | [ausschnitt.dxf](input/ds425-pushbutton/cad/ausschnitt.dxf) | Panel-Ausschnitt (Lasercutter) |
| [ec11-encoder](input/ec11-encoder/) | input | [ausschnitt.dxf](input/ec11-encoder/cad/ausschnitt.dxf) | Panel-Ausschnitt (Lasercutter) |
| [tm1637-4digit](output/tm1637-4digit/) | output | [ausschnitt.dxf](output/tm1637-4digit/cad/ausschnitt.dxf) | Panel-Ausschnitt (Lasercutter) |
| [tm1637-4digit](output/tm1637-4digit/) | output | [halterung.stl](output/tm1637-4digit/cad/halterung.stl) | Halterung (3D-Druck) |
| [st7735-tft-1-8-spi](output/st7735-tft-1-8-spi/) | output | [ausschnitt.dxf](output/st7735-tft-1-8-spi/cad/ausschnitt.dxf) | Panel-Ausschnitt (Lasercutter) |
| [st7735-tft-1-8-spi](output/st7735-tft-1-8-spi/) | output | [halterung.stl](output/st7735-tft-1-8-spi/cad/halterung.stl) | Halterung (3D-Druck) |
| [gehaeuse/microbit](gehaeuse/microbit/) | Gehaeuse | [BOX_KOMPLETT.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/BOX_KOMPLETT.dxf) | Box, alle Teile auf einem Blatt (Lasercutter) |
| [gehaeuse/microbit](gehaeuse/microbit/) | Gehaeuse | [Boden.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/Boden.dxf) · [Deckelplatte.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/Deckelplatte.dxf) · [Eckklotz.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/Eckklotz.dxf) · [Laengswand.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/Laengswand.dxf) · [Querwand.dxf](gehaeuse/microbit/cad/box-pappelsperrholz/Querwand.dxf) | Box, einzelne Teile (Lasercutter) |
| [gehaeuse/microbit](gehaeuse/microbit/) | Gehaeuse | [mit Sichtfenster](gehaeuse/microbit/cad/deckel-varianten/microbit_mit_Sichtfenster.dxf) · [mit Sichtfenster + A/B](gehaeuse/microbit/cad/deckel-varianten/microbit_mit_Sichtfenster_A_B.dxf) · [ohne Sichtfenster](gehaeuse/microbit/cad/deckel-varianten/microbit_ohne_Sichtfenster.dxf) | Deckel-Varianten (Lasercutter) |
| [gehaeuse/microbit](gehaeuse/microbit/) | Gehaeuse | [Microbit_V2_Case.stl](gehaeuse/microbit/cad/microbit-halterung/Microbit_V2_Case.stl) | micro:bit-Halterung (3D-Druck) |
| [gehaeuse/microbit](gehaeuse/microbit/) | Gehaeuse | [Bolzen_Zahnstange.stl](gehaeuse/microbit/cad/schliessmechanismus/Bolzen_Zahnstange.stl) · [Ritzel.stl](gehaeuse/microbit/cad/schliessmechanismus/Ritzel.stl) · [Schale_oben.stl](gehaeuse/microbit/cad/schliessmechanismus/Schale_oben.stl) · [Schale_unten.stl](gehaeuse/microbit/cad/schliessmechanismus/Schale_unten.stl) | Schliessmechanismus (3D-Druck) |

**Noch keine Ausschnitt-Datei:** [hc-sr04-abstandssensor](input/hc-sr04-abstandssensor/),
[ws2812b-led-strip](output/ws2812b-led-strip/), [miuzei-9g-servo](servo/miuzei-9g-servo/)
(folgen spaeter).

`.dxf` hat auf GitHub kein Vorschaubild - zum Anschauen in LightBurn oder
einem DXF-Viewer oeffnen. `.stl` zeigt GitHub direkt als drehbares 3D-Modell
(Datei anklicken), zum Drucken trotzdem herunterladen.

## Was ist LightBurn?

LightBurn ist die Software zum Vorbereiten und Senden von Dateien an den
Lasercutter - Formen, Text, Bilder und importierte Vektorgrafiken (z. B. die
`.dxf`-Dateien oben).

### Die wichtigsten Bereiche

- **Arbeitsbereich:** alle Objekte werden hier erstellt/angeordnet (max. 1000 x 600 mm).
- **Werkzeugleiste links:** Formen, Linien, Text, Auswahl.
- **Farbpalette unten:** weist Objekten eine Bearbeitungsebene (Layer) zu.
- **Cuts/Layers rechts:** hier werden Geschwindigkeit, Leistung usw. je Ebene festgelegt - die Werte dafuer stehen material-spezifisch bei [lasercutter-pappelsperrholz.md](lasercutter-pappelsperrholz.md).
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
4. **Speed**, **Max Power**, **Min Power**, **Passes** aus
   [lasercutter-pappelsperrholz.md](lasercutter-pappelsperrholz.md) eintragen -
   fuer den jeweiligen Zweck (Schneiden vs. Gravieren).
5. **Fokus/Z-Offset:** nur sichtbar, wenn die Z-Achse im Geraeteprofil
   aktiviert ist. Erst **Autofokus** einmal ausfuehren, danach **nicht mehr
   manuell nachfokussieren** - stattdessen den Z-Offset-Wert am Layer
   eintragen (Z-Offset ist eine **Layer-Eigenschaft**, keine
   Objekteigenschaft). Zusaetzlich **"Relative Z moves only"** in den
   Geraeteeinstellungen aktivieren, sonst faehrt die Maschine auf absolute
   statt relative Koordinaten.

**Grundregel:** Gravieren = hoehere Geschwindigkeit, niedrigere Leistung.
Schneiden = niedrigere Geschwindigkeit, hoehere Leistung. Die exakten Werte
haengen von Material, Dicke, Fokus und Linse ab - deshalb nur freigegebene
Werte verwenden, nicht raten.

**Min Power** ist die Leistung bei Geschwindigkeit Null. Der Controller
interpoliert linear bis Max Power bei Sollgeschwindigkeit - das wirkt sich in
Ecken, an Linienanfaengen und auf kurzen Segmenten aus (der Kopf beschleunigt
dort noch). Zu niedriges Min: kleine Loecher/Zinken kommen nicht durch, obwohl
lange Kanten sauber schneiden. Faustregel: Min = Max minus 5-15 Prozentpunkte.

### Datei anlegen/importieren

- Neues Projekt: **Datei -> Neu**
- DXF/SVG importieren: **Datei -> Importieren** (z. B. eine `ausschnitt.dxf`
  aus der Tabelle oben)
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
2. Modus **Image**, Werte aus [lasercutter-pappelsperrholz.md](lasercutter-pappelsperrholz.md#gravur-ebenen)
   (300 mm/s, Max 12.5 % / Min 10 %, Line Interval 0.1200 mm).
3. Im **Bild anpassen**-Dialog: Kontrast **+10 %**, Dither-Modus **Stucki**
   oder **Jarvis**, Vorschau pruefen.
4. Scharfe, kontrastreiche Bilder ohne unruhigen Hintergrund funktionieren am
   besten.
5. **Line Interval** (Zeilenabstand): zu klein = zu dunkel/unscharf, zu gross
   = sichtbare Luecken. Testbereich ca. 0.08-0.20 mm (120-300 DPI).

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
