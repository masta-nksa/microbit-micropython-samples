# Fusion 360: 3D modellieren

Mit Fusion konstruierst du die Teile fuer deine Box: Platten mit Ausschnitten
fuer den **Lasercutter** und Halterungen fuer den **3D-Drucker**. Diese Seite
fuehrt dich in zwei kleinen Uebungen einmal durch den ganzen Weg: von der
Skizze bis zur fertigen Datei.

| Uebung | Ergebnis | Weiter mit |
|--------|----------|------------|
| [1: Frontplatte mit Taster-Ausschnitt](#uebung-1-frontplatte-mit-taster-ausschnitt-lasercutter) | `.dxf` | [LightBurn](lightburn.md) |
| [2: Halterung fuer den Taster](#uebung-2-halterung-fuer-den-taster-3d-druck) | `.stl` | PrusaSlicer oder Cura |

**Vorher anschauen (Video, ca. der erste Teil reicht):** [Fusion 360 Tutorial
fuer Anfaenger: Erste Schritte in der CAD-Software
(Deutsch)](https://www.youtube.com/watch?v=zZTSAMQc7jc) (YouTube, Kanal
mak3r). Falls dir das nicht liegt: [So geht Fusion - Einsteigertutorial fuer
Autodesk Fusion 360](https://www.youtube.com/watch?v=mI7RYHItzmM) (Kanal
Druckwerkstatt 3D).

> **Hinweis zu den Menuenamen:** Die Befehle stehen hier auf Englisch, wie sie
> in Fusion heissen, dahinter kurz das Tastenkuerzel. Je nach Sprache und
> Version koennen die Namen leicht abweichen. Im Zweifel: mit `S` das
> Suchfenster oeffnen und den Befehl eintippen.

## Die Oberflaeche in 5 Punkten

1. **Toolbar oben** (Reiter *Solid*): die Befehle *Create*, *Modify*,
   *Construct*, *Inspect*. Hier passiert fast alles.
2. **Browser links:** Liste aller Skizzen, Koerper (*Bodies*) und Parameter.
   Rechtsklick auf einen Eintrag oeffnet das Exportmenue.
3. **Timeline unten:** jeder Schritt, den du machst, als Kaestchen. Doppelklick
   auf ein Kaestchen aendert den Schritt nachtraeglich. Darum ist Fusion
   **parametrisch**: Aenderst du ein Mass, baut sich das Modell neu auf.
4. **ViewCube oben rechts:** Klick auf eine Seite dreht die Ansicht dorthin,
   das Haeuschen (Home) stellt die Standardansicht wieder her.
5. **Maus:** Mausrad = zoomen, Mausrad gedrueckt halten = verschieben,
   **Shift** + Mausrad gedrueckt halten = drehen.

Rueckgaengig: `Strg + Z`. Speichern: `Strg + S` (Fusion speichert in der Cloud
unter deinem Autodesk-Konto).

## Uebung 1: Frontplatte mit Taster-Ausschnitt (Lasercutter)

**Ziel:** Eine 60 x 40 mm grosse Platte aus Pappelsperrholz mit einem runden
Loch fuer den Stoessel des DS425-Tasters. Am Ende steht eine `.dxf`-Datei.

Die Masse stammen aus [Hardware-Masse](README.md): Stoessel-Durchmesser 3.5 mm,
empfohlener Ausschnitt **D 4.0 mm**
([ds425-pushbutton](input/ds425-pushbutton/)). Materialdicke: **5.5 mm**
(gemessen, siehe [Lasercutter Pappelsperrholz](lasercutter-pappelsperrholz.md)).

### 1. Neues Design und Parameter

1. **File > New Design**. Einheit ist **Millimeter** (mm). Pruefen unter
   *Browser > Document Settings > Units*.
2. **Modify > Change Parameters** (Parameter aendern). Bei *User Parameters*
   auf **+** klicken und drei Parameter anlegen:

   | Name | Wert | Bedeutung |
   |------|------|-----------|
   | `dicke` | 5.5 mm | Materialdicke |
   | `kerf` | 0.25 mm | Breite des Laserschnitts |
   | `loch_d` | 4 mm | gewuenschter Lochdurchmesser |

   Mit diesen Namen kannst du danach in jedes Massfeld rechnen, z. B.
   `loch_d - kerf`. Aendert sich das Material, stellst du **einmal** `dicke`
   um.

### 2. Skizze

1. **Create Sketch** (Skizze erstellen) und die Grundebene (*XY*) anklicken.
2. **Rectangle > 2-Point Rectangle** (`R`): zwei Ecken aufziehen. Mit dem
   Befehl **Sketch Dimension** (`D`) die Breite auf **60 mm** und die Hoehe auf
   **40 mm** setzen. Die untere linke Ecke mit der Maus auf den Ursprung
   ziehen, sie rastet ein und das Rechteck sitzt fest.
3. **Circle > Center Diameter Circle** (`C`): Kreis in die Mitte des
   Rechtecks setzen. Mit `D` den Durchmesser anklicken und
   `loch_d - kerf` eingeben. Den Mittelpunkt mit zwei Massen fest
   positionieren (30 mm von links, 20 mm von unten).
4. **Finish Sketch** (gruener Haken).

Skizzenlinien sind **blau**, solange etwas noch verschiebbar ist, und
**schwarz**, wenn alles fest bemasst ist. Ziel: alles schwarz.

> **Warum `loch_d - kerf`?** Der Laser schneidet etwa 0.25 mm breit. Er
> entfernt Material auf beiden Seiten der Linie, ein Loch wird dadurch um den
> Kerf **groesser** als gezeichnet. Zeichnest du es um den Kerf kleiner, hast
> du nach dem Schneiden das gewuenschte Mass. Fuer Aussenkanten gilt das
> Umgekehrte (Aussenmass **plus** Kerf). Die fertigen Dateien in diesem Repo
> haben den Kerf schon in der Zeichnung, deshalb bleibt der Schnittversatz in
> LightBurn auf 0.

### 3. Platte aufziehen (nur zur Kontrolle)

1. **Create > Extrude** (`E`). Die Flaeche zwischen Rechteck und Kreis
   anklicken (das Loch muss frei bleiben).
2. Bei *Distance* `dicke` eintippen, mit **OK** bestaetigen.

Jetzt siehst du die Platte in 3D. Fuer den Laser brauchst du nur die Skizze.
Trotzdem lohnt sich der Schritt: Du siehst sofort, ob das Loch am richtigen
Ort sitzt.

### 4. Als DXF exportieren

1. Im **Browser** unter *Sketches* Rechtsklick auf die Skizze.
2. **Save as DXF** (Als DXF speichern), einen Dateinamen und Speicherort
   waehlen.

Exportiert wird nur die Skizze, nicht der Koerper. Alle Linien der Skizze
kommen mit.

### 5. In LightBurn pruefen

1. In LightBurn: **Datei > Importieren**, die `.dxf` waehlen.
2. Ausgewaehltes Objekt: **Breite/Hoehe** kontrollieren (hier etwa 60 x 40 mm).
   Stimmt die Groesse nicht, war die Einheit in Fusion nicht mm.
3. Weiter mit Ebenen und Schnittwerten:
   [LightBurn](lightburn.md), [Werte fuer Pappelsperrholz](lasercutter-pappelsperrholz.md).

**Fertig, wenn:** Die Platte ist in LightBurn 60 x 40 mm gross und hat ein
rundes Loch.

## Uebung 2: Halterung fuer den Taster (3D-Druck)

**Ziel:** Ein kleiner Block mit quadratischer Aussparung, in den der 6 x 6 mm
grosse Taster passt. Am Ende steht eine `.stl`-Datei fuer den Slicer.

Weiter im selben Design (oder ein neues mit den gleichen Parametern).

### 1. Grundkoerper

1. **Create Sketch**, wieder die *XY*-Ebene.
2. **Rectangle > Center Rectangle**: vom Ursprung aus ein Rechteck aufziehen,
   mit `D` auf **20 x 20 mm** bemassen.
3. **Finish Sketch**, dann **Extrude** (`E`) mit *Distance* **8 mm**.

### 2. Aussparung fuer den Taster

1. **Create Sketch** und die **Oberseite** des Blocks anklicken.
2. **Center Rectangle** vom Ursprung aus, bemassen auf **6.4 x 6.4 mm**
   (Tastergehaeuse 6.0 mm plus 0.2 mm Spiel pro Seite).
3. **Finish Sketch**, dann **Extrude** (`E`). Das Quadrat anklicken. Bei
   *Operation* **Cut** waehlen und *Distance* **3.5 mm** eingeben (Hoehe des
   Tastergehaeuses).

### 3. Als STL exportieren

1. Im **Browser** unter *Bodies* Rechtsklick auf den Koerper.
2. **Save As Mesh**.
3. Format **STL (Binary)**, Einheit **Millimeter**, Verfeinerung **Medium**
   oder **High**. Speichern.
4. Die `.stl` im Slicer (PrusaSlicer oder Cura) oeffnen. Auf dem
   Druckbett soll die **flache Seite** unten liegen.

**Fertig, wenn:** Der Slicer zeigt den Block mit der quadratischen Aussparung,
das Mass stimmt (20 x 20 x 8 mm).

> **3D-Druck-Regel:** Passteile brauchen **Spiel**. Ein 3D-Drucker druckt nie
> exakt auf das Zehntel genau. Darum 0.2 mm pro Seite zugeben, bei einer
> Passung im Zweifel eher 0.3 mm. Das Mass ist danach am ausgedruckten Teil
> zu pruefen, nicht am Modell.

## Wenn etwas nicht klappt

| Problem | Ursache | Loesung |
|---------|---------|---------|
| Beim Extrudieren laesst sich keine Flaeche anklicken | Die Skizze ist nicht geschlossen, eine Linie hat eine Luecke | Skizze bearbeiten, Ecken pruefen. Endpunkte muessen exakt aufeinander liegen |
| Skizzenlinien bleiben blau | Es fehlt ein Mass oder eine Bedingung | Mit `D` die fehlenden Masse setzen, bis alles schwarz ist |
| Das Loch ist nach dem Extrudieren zugewachsen | Die Flaeche im Loch wurde mitgewaehlt | Nur die Flaeche **ausserhalb** des Kreises anklicken |
| Die DXF ist in LightBurn zu gross oder zu klein | Einheit in Fusion war nicht mm | Document Settings > Units auf mm stellen, neu exportieren |
| *Save as DXF* fehlt im Menue | Rechtsklick auf den Koerper statt auf die Skizze | Rechtsklick auf die Skizze im Browser |
| Kein *Save As Mesh* | Rechtsklick auf die Skizze statt auf den Koerper | Rechtsklick auf den Koerper unter *Bodies* |
| Aussparung passt nicht am gedruckten Teil | Kein Spiel eingerechnet | Aussparung um 0.1-0.2 mm groesser machen, neu drucken |

## Masse und fertige Modelle

- **Masse der Bauteile** (Taster, Encoder, Anzeigen, Servo ...): fuer jedes
  Bauteil eine `dimensions.json` und eine Tabelle in der `README.md`. Aufbau
  und Schema: [Hardware-Masse fuers CAD](README.md).
- **Fertige Modelle als Beispiel:** die Box mit Fingerzinken, die Halterung
  fuer den micro:bit und der Schliessmechanismus sind in Fusion entstanden:
  [Gehaeuse micro:bit](gehaeuse/microbit/). Die Box ist parametrisch gebaut:
  **t5** = 5 mm Materialstaerke, **45°** Fingerzinken-Winkel, **k0.35** =
  0.35 mm Kerf-Zugabe pro Schnitt. Den Kerf am eigenen Lasercutter mit
  Testmaterial ermitteln und in Fusion anpassen, statt die DXF von Hand
  nachzuschneiden.
