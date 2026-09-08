# WS2812B LED-Strip - Masse

> **Status: nicht verifiziert.** Platzhalterwerte fuer einen 5050-WS2812B-Strip.
> Vor der Fertigung selbst messen (v. a. LED-Abstand!) und
> `dimensions.json` -> `"verified": true`.

Code-Samples: [../../../code-samples/output/ws2812b-led-strip/](../../../code-samples/output/ws2812b-led-strip/)

## Masstabelle (mm)

| Mass | Wert | Bemerkung |
|------|-----:|-----------|
| Streifenbreite | 10.0 | weisse Platine, einreihig |
| Dicke | 2.0 | ohne Silikon (IP30) |
| LED-Abstand | 33.3 | bei 30 LEDs/m - **am echten Strip pruefen** (30/60/144) |
| Klebeband hinten | ja | 3M |

## Ausschnitt / Nut

- Nut fuer Alu-Profil / Diffusor: **10.4 x 2.4 mm** (Breite + 0,2 pro Seite)
- Der Strip laesst sich nur an den markierten Schnittstellen kuerzen -
  Rastermass = LED-Abstand.

Maschinenlesbar: [`dimensions.json`](dimensions.json)

## Bilder

Datenblatt, Messfotos, CAD-Screenshots in [`bilder/`](bilder/).
