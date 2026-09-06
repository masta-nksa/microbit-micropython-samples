# EC11 Rotary Encoder (mit Push) - Masse

> **Status: nicht verifiziert.** Platzhalterwerte fuer die EC11-Standardbauform.
> Vor der Fertigung selbst messen und `dimensions.json` -> `"verified": true`.

Code-Samples folgen unter
`../../../code-samples/input/ec11-encoder/` (noch nicht angelegt).

## Masstabelle (mm)

| Mass | Wert | Bemerkung |
|------|-----:|-----------|
| Gehaeuse Breite x Tiefe | 12.0 x 12.0 | |
| Gehaeuse Hoehe | 6.5 | ohne Welle/Gewinde |
| Gewindebund | M7 x 0.75, Laenge 5.0 | fuer Panelmontage |
| Welle Durchmesser | 6.0 | D-Form (abgeflacht) |
| Welle Laenge | 15.0 | ab Gewindeoberkante |
| Rastungen / Impulse pro Umdrehung | 20 / 20 | |
| Taster (Push) | ja | Welle druecken |

## Ausschnitt fuers Panel

- Rundloch Durchmesser **7.2 mm** fuer den Gewindebund
- Zusaetzlich kleines Loch D 2.0 mm fuer den Verdrehschutz-Stift,
  ca. 7 mm von der Mitte (Lage am realen Teil pruefen)

Maschinenlesbar: [`dimensions.json`](dimensions.json)

## Anschluss am micro:bit (Vorschau)

- Encoder-Pins A/B an zwei GPIOs (z. B. `P0`, `P1`), Mittelpin an `GND`
- Taster-Pins an einen weiteren GPIO (z. B. `P2`) + `GND`
- interne Pull-ups im Code aktivieren

## Bilder

Datenblatt und Messfotos in [`bilder/`](bilder/).
