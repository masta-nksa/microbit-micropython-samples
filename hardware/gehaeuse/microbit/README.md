# micro:bit-Gehaeuse - Grundstruktur

Das Gesamt-Gehaeuse (Pappelsperrholz, lasergeschnitten), in das der micro:bit
und die einzelnen Hardware-Elemente eingebaut werden. Anders als die
Bauteil-Ordner unter [`../../input/`](../../input/), [`../../output/`](../../output/)
und [`../../servo/`](../../servo/) beschreibt dieser Ordner nicht ein
einzelnes Bauteil, sondern die Box drumherum.

> **Status: nicht verifiziert / in Arbeit.** Aus einem laufenden
> Fusion-Projekt exportiert. Vor der Fertigung pruefen, insbesondere
> Materialstaerke (aktuell fuer 5 mm Pappelsperrholz ausgelegt) und Kerf am
> eigenen Lasercutter.

## Aufbau

```
cad/
├── box-pappelsperrholz/   Aussenbox mit Fingerzinken (Boden, Deckelplatte,
│                          Eckklotz, Laengswand, Querwand + Gesamtzeichnung)
├── deckel-varianten/      Alternative Deckel-Ausschnitte fuer den micro:bit
├── microbit-halterung/    3D-druckbare Halterung, in die die micro:bit-
│                          Platine eingeklipst wird
├── schliessmechanismus/   3D-druckbare Teile fuer den Verschluss der Box
│                          (Zahnstange, Ritzel, zwei Schalenhaelften)
├── taster-v1/             Taster A/B durch den Holzdeckel, Version 1: Gewindebolzen
│                          im Holzloch mit Kontermutter
└── taster-v2/             Taster A/B durch den Holzdeckel, Version 2: fest verschraubte
                           Fuehrungshuelse mit Stoessel und Knopf
```

## Box (Lasercutter, Pappelsperrholz)

Parameter aus dem Dateinamen der Fusion-Konstruktion: **t5** = 5 mm
Materialstaerke, **45°** Fingerzinken-Winkel, **k0.35** = 0.35 mm Kerf-Zugabe
pro Schnitt. Beim eigenen Lasercutter den Kerf am Testmaterial ermitteln und
bei Abweichung in Fusion neu exportieren statt die DXF von Hand
nachzuschneiden.

Schnitt-/Gravur-Layer-Werte fuer 6 mm Pappelsperrholz (Speed, Power, Fokus):
[../../lasercutter-pappelsperrholz.md](../../lasercutter-pappelsperrholz.md).
LightBurn-Bedienung und alle Ausschnitt-Dateien: [../../lightburn.md](../../lightburn.md).
GitHub kann `.dxf` nicht anzeigen - zum Anschauen z. B. in LightBurn oder
einem DXF-Viewer oeffnen.

- [`cad/box-pappelsperrholz/BOX_KOMPLETT.dxf`](cad/box-pappelsperrholz/BOX_KOMPLETT.dxf) - alle Teile auf einem Blatt
- [`cad/box-pappelsperrholz/Boden.dxf`](cad/box-pappelsperrholz/Boden.dxf)
- [`cad/box-pappelsperrholz/Deckelplatte.dxf`](cad/box-pappelsperrholz/Deckelplatte.dxf)
- [`cad/box-pappelsperrholz/Eckklotz.dxf`](cad/box-pappelsperrholz/Eckklotz.dxf)
- [`cad/box-pappelsperrholz/Laengswand.dxf`](cad/box-pappelsperrholz/Laengswand.dxf)
- [`cad/box-pappelsperrholz/Querwand.dxf`](cad/box-pappelsperrholz/Querwand.dxf)

## Deckel-Varianten (Download)

Drei Varianten fuer den Deckelausschnitt ueber dem micro:bit - je nach
gewuenschter Sichtbarkeit von LED-Matrix/Tastern auswaehlen (GitHub kann
`.dxf` nicht anzeigen - z. B. in LightBurn oeffnen):

- [`cad/deckel-varianten/microbit_mit_Sichtfenster.dxf`](cad/deckel-varianten/microbit_mit_Sichtfenster.dxf)
- [`cad/deckel-varianten/microbit_mit_Sichtfenster_A_B.dxf`](cad/deckel-varianten/microbit_mit_Sichtfenster_A_B.dxf) - mit zusaetzlichem Ausschnitt fuer Taster A/B
- [`cad/deckel-varianten/microbit_ohne_Sichtfenster.dxf`](cad/deckel-varianten/microbit_ohne_Sichtfenster.dxf)

## micro:bit-Halterung (3D-Druck, Download)

- [`cad/microbit-halterung/Microbit_V2_Case.stl`](cad/microbit-halterung/Microbit_V2_Case.stl) -
  Halterung fuer die micro:bit-V2-Platine, wird in die Box eingesetzt
  (auf GitHub direkt als 3D-Modell anschaubar, kein Download noetig).
  Zum Drucken z. B. in PrusaSlicer oder Cura oeffnen.

## Schliessmechanismus (3D-Druck, Download)

Zahnstangen-Verschluss zum Auf-/Zuschieben der Box (alle als 3D-Modell direkt
auf GitHub anschaubar, zum Drucken z. B. in PrusaSlicer oder Cura oeffnen):

- [`cad/schliessmechanismus/Bolzen_Zahnstange.stl`](cad/schliessmechanismus/Bolzen_Zahnstange.stl)
- [`cad/schliessmechanismus/Ritzel.stl`](cad/schliessmechanismus/Ritzel.stl)
- [`cad/schliessmechanismus/Schale_oben.stl`](cad/schliessmechanismus/Schale_oben.stl)
- [`cad/schliessmechanismus/Schale_unten.stl`](cad/schliessmechanismus/Schale_unten.stl)

## Taster A/B durch den Holzdeckel (3D-Druck, Download)

Damit man die micro:bit-Taster durch den Holzdeckel mit dem Finger druecken kann
(statt mit einer Schraube). Holz 4 - 9 mm dick, rundes Loch im Holz. Zwei Versionen:

| | Version 1 | Version 2 (empfohlen) |
|---|---|---|
| Prinzip | Gewindebolzen im Holzloch, Kontermutter, Kappe | Fuehrungshuelse mit Klemmmutter im Holz, Stoessel gleitet darin, Knopf |
| Holzloch | Ø 10,4 mm | Ø 12,4 mm |
| Teile je Taster | 3 (Stoessel, Mutter, Kappe) | 4 (Huelse, Stoessel, Knopf, Klemmmutter) |
| Fuehrung | nur die Holzdicke, wackelt etwas | ca. 12 mm lange Bohrung, fest im Holz |
| Anleitung | [`cad/taster-v1/README.md`](cad/taster-v1/README.md) | [`cad/taster-v2/README.md`](cad/taster-v2/README.md) |

Beide sind nur in Fusion numerisch geprueft, noch nicht gedruckt; die Anleitungen nennen
die Annahmen (Tasterflaeche, Tasterhoehe), die vor dem Serien-Druck nachgemessen werden sollten.

**Version 1:**
[`stoessel_links.stl`](cad/taster-v1/stoessel_links.stl) /
[`stoessel_rechts.stl`](cad/taster-v1/stoessel_rechts.stl) (je 1x),
[`kontermutter.stl`](cad/taster-v1/kontermutter.stl) /
[`kappe.stl`](cad/taster-v1/kappe.stl) (je 2x),
[`deck_mit_microbit_taster_rund.dxf`](cad/taster-v1/deck_mit_microbit_taster_rund.dxf),
[`taster_bauen.py`](cad/taster-v1/taster_bauen.py)

**Version 2:**
[`huelse_links.stl`](cad/taster-v2/huelse_links.stl) /
[`huelse_rechts.stl`](cad/taster-v2/huelse_rechts.stl) (je 1x),
[`stoessel.stl`](cad/taster-v2/stoessel.stl),
[`knopf.stl`](cad/taster-v2/knopf.stl),
[`klemmmutter.stl`](cad/taster-v2/klemmmutter.stl) (je 2x),
[`deck_mit_microbit_taster_v2.dxf`](cad/taster-v2/deck_mit_microbit_taster_v2.dxf),
[`taster_bauen.py`](cad/taster-v2/taster_bauen.py)

## Bilder

Fotos, Datenblatt-Ausschnitte, CAD-Screenshots in [`bilder/`](bilder/).
