# Hardware-Masse fuer CAD

Masse ausgewaehlter Bauteile, damit daraus Panel-Ausschnitte, Halterungen und
Gehaeuse im CAD (z. B. Fusion) erzeugt werden koennen.

Schnitt-/Gravurparameter fuers Serienmaterial und eine LightBurn-Kurzanleitung:
[lasercutter-pappelsperrholz.md](lasercutter-pappelsperrholz.md).

## Aufbau

`hardware/<kategorie>/<bauteil>/` - **gleicher Pfad** wie unter
[`../code-samples/`](../code-samples/). Pro Bauteil:

| Datei | Zweck |
|-------|-------|
| `README.md` | Masstabelle, Skizze, empfohlener Ausschnitt (fuer Menschen) |
| `dimensions.json` | dieselben Masse maschinenlesbar (fuer CAD-/Fusion-Skripte) |
| `bilder/` | Fotos, Datenblatt-Ausschnitte, CAD-Screenshots |
| `cad/` | fertige Downloads: `ausschnitt.dxf` (Panel-Ausschnitt fuer den Lasercutter) und/oder `halterung.stl` (3D-druckbare Halterung) |

`.stl`-Dateien zeigt GitHub direkt als drehbares 3D-Modell an (Datei im Repo
anklicken) - kein Download noetig zum Anschauen. Zum **Drucken** trotzdem
herunterladen und z. B. in PrusaSlicer oder Cura oeffnen. Fuer `.dxf` gibt es
kein natives GitHub-Preview - zum Anschauen z. B. in LightBurn oder einem
DXF-Viewer oeffnen (kein PNG-Vorschaubild im Repo, das wurde zu
gross/unhandlich fuers README).

`hardware/gehaeuse/<name>/` ist eine Ausnahme vom Bauteil-Schema: hier liegt
kein einzelnes Bauteil, sondern ein ganzes Gehaeuse (z. B. die micro:bit-Box),
das mehrere der obigen Bauteile aufnimmt. Struktur innerhalb von `cad/` ist
dort frei (Unterordner je Baugruppe), Rest analog.

## Konventionen

- **Einheit:** Millimeter (mm), Winkel in Grad.
- **Feld `verified`:** `false` = aus Datenblatt / geschaetzt, `true` = selbst
  gemessen und geprueft. Erst bei `true` fuer echte Fertigung verwenden.
- **Toleranzen:** `panel_cutout` enthaelt ein Feld `tolerance` = wie viel der
  Ausschnitt pro Seite groesser sein soll als das Nennmass.
- **Nullpunkt:** Mittelpunkt des Bauteils (Stoessel- bzw. Wellenachse),
  Bauteil sitzt hinter dem Panel, Betaetiger schaut nach vorne (+Z).

## `dimensions.json` - Schema

```json
{
  "part": "Klartext-Name",
  "slug": "ordnername",
  "kind": "pushbutton | rotary-encoder | display | led-strip | ...",
  "units": "mm",
  "verified": false,
  "source": "Datenblatt-URL oder 'eigene Messung'",
  "body":     { "width": 0, "depth": 0, "height": 0 },
  "actuator": { "shape": "round|square", "diameter": 0, "protrusion": 0 },
  "mount":    { "type": "pcb|panel-thread|clip", "detail": "..." },
  "pins":     { "pattern": "2x2", "pitch_x": 0, "pitch_y": 0, "dia": 0 },
  "cad": {
    "panel_cutout": { "shape": "circle|rect", "diameter": 0, "tolerance": 0.2 },
    "note": "Freitext"
  }
}
```

Nicht zutreffende Felder weglassen. Ein CAD-Skript liest immer
`hardware/<kat>/<bauteil>/dimensions.json`. Optional: `cad_files` verweist auf
die Downloads in `cad/` (siehe oben), z. B.
`{ "ausschnitt": "cad/ausschnitt.dxf", "halterung": "cad/halterung.stl" }`.

## Bauteile

| Bauteil | Kategorie | verified | Downloads |
|---------|-----------|----------|-----------|
| [ds425-pushbutton](input/ds425-pushbutton/) | input | nein | Ausschnitt |
| [ec11-encoder](input/ec11-encoder/) | input | nein | Ausschnitt |
| [hc-sr04-abstandssensor](input/hc-sr04-abstandssensor/) | input | nein | - |
| [miuzei-9g-servo](servo/miuzei-9g-servo/) | servo | nein | - |
| [ws2812b-led-strip](output/ws2812b-led-strip/) | output | nein | - |
| [tm1637-4digit](output/tm1637-4digit/) | output | nein | Ausschnitt + Halterung |
| [st7735-tft-1-8-spi](output/st7735-tft-1-8-spi/) | output | nein | Ausschnitt + Halterung |

## Gehaeuse

| Gehaeuse | verified | Downloads |
|----------|----------|-----------|
| [microbit](gehaeuse/microbit/) | nein | Box (Lasercutter) + Deckel-Varianten + Halterung + Schliessmechanismus |
