# Hardware-Masse fuer CAD

Masse ausgewaehlter Bauteile, damit daraus Panel-Ausschnitte, Halterungen und
Gehaeuse im CAD (z. B. Fusion) erzeugt werden koennen.

## Aufbau

`hardware/<kategorie>/<bauteil>/` - **gleicher Pfad** wie unter
[`../code-samples/`](../code-samples/). Pro Bauteil:

| Datei | Zweck |
|-------|-------|
| `README.md` | Masstabelle, Skizze, empfohlener Ausschnitt (fuer Menschen) |
| `dimensions.json` | dieselben Masse maschinenlesbar (fuer CAD-/Fusion-Skripte) |
| `bilder/` | Fotos, Datenblatt-Ausschnitte, CAD-Screenshots |

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
`hardware/<kat>/<bauteil>/dimensions.json`.

## Bauteile

| Bauteil | Kategorie | verified |
|---------|-----------|----------|
| [ds425-pushbutton](input/ds425-pushbutton/) | input | nein |
| [ec11-encoder](input/ec11-encoder/) | input | nein |
| [miuzei-9g-servo](servo/miuzei-9g-servo/) | servo | nein |
