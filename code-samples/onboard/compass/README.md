# Kompass / Magnetometer

Misst das Erdmagnetfeld und daraus die **Himmelsrichtung**, in die die
Oberkante des micro:bit zeigt (0 = Norden, 90 = Osten, ...).

- Eingebaut, kein Aufbau noetig
- `compass` - Objekt, immer verfuegbar

## Kalibrieren ist Pflicht

Vor der ersten Messung **muss** `compass.calibrate()` laufen. Dabei
erscheint ein Punkt auf der Matrix - den micro:bit langsam in alle Richtungen
kippen, bis der ganze Rand voll ist. Danach zeigt ein Smiley kurz an: fertig.

Ohne Kalibrierung liefert `heading()` Unsinn. In der Naehe von Metall,
Magneten, Lautsprechern oder Netzteilen ist die Messung ebenfalls gestoert.

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `compass.calibrate()` | Kalibrier-Spiel starten (blockiert, bis fertig) |
| `compass.is_calibrated()` | `True`, wenn schon kalibriert |
| `compass.heading()` | Richtung 0..359 Grad (0 = Norden) |
| `compass.get_field_strength()` | Staerke des Magnetfelds in Nanotesla |

## Samples (Lernreihenfolge)

1. [kompass-pfeil/](kompass-pfeil/) - ein Pfeil auf der Matrix zeigt immer nach Norden
