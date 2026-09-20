# Fusion 360: 3D modellieren

> **Status: Anleitung in Arbeit.** Diese Seite ist der Platz fuer die
> Schritt-fuer-Schritt-Anleitung zum Modellieren in Autodesk Fusion. Bis sie
> fertig ist, steht hier, wie Fusion in diesem Projekt eingesetzt wird und wo
> die fertigen Dateien liegen.

## Einstieg als Video

[Fusion 360 Tutorial fuer Anfaenger: Erste Schritte in der CAD-Software
(Deutsch)](https://www.youtube.com/watch?v=zZTSAMQc7jc) (YouTube, Kanal
mak3r). Weiteres Einsteiger-Video, falls dir das erste nicht liegt: [So geht
Fusion - Einsteigertutorial fuer Autodesk Fusion
360](https://www.youtube.com/watch?v=mI7RYHItzmM) (Kanal Druckwerkstatt 3D).

## Wofuer wir Fusion brauchen

Die Teile fuer Box, Halterungen und Mechanik werden als 3D-Modell in Fusion
konstruiert und von dort in zwei Richtungen exportiert:

| Ziel | Format | Weiterverarbeitung |
|------|--------|--------------------|
| Lasercutter (Holzplatten, Ausschnitte) | `.dxf` | in LightBurn oeffnen: [LightBurn](lightburn.md) |
| 3D-Drucker (Halterungen, Mechanik) | `.stl` | in PrusaSlicer oder Cura oeffnen |

## Masse der Bauteile

Die Masse der verwendeten Bauteile (Taster, Encoder, Anzeigen, Servo ...)
stehen fuer jedes Bauteil in einer `dimensions.json` und als Tabelle in der
`README.md`. Aufbau und Schema: [Hardware-Masse fuers CAD](README.md).

## Fertige Modelle als Beispiel

Die Box mit Fingerzinken, die Halterung fuer den micro:bit und der
Schliessmechanismus sind in Fusion entstanden:
[Gehaeuse micro:bit](gehaeuse/microbit/).

Parameter der Box, die in Fusion als Variablen eingestellt werden: **t5** =
5 mm Materialstaerke, **45°** Fingerzinken-Winkel, **k0.35** = 0.35 mm
Kerf-Zugabe pro Schnitt. Den Kerf am eigenen Lasercutter mit Testmaterial
ermitteln und in Fusion anpassen, statt die DXF von Hand nachzuschneiden.

## Noch offen

- Schritt-fuer-Schritt-Anleitung: neues Modell anlegen, Skizze, Extrusion,
  Parameter
- Export als DXF (Lasercutter) und STL (3D-Druck)
