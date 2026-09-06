# DS425 Momentary Pushbutton - Masse

> **Status: nicht verifiziert.** Alle Werte sind Platzhalter (typischer
> 6x6-mm-Taktschalter). Vor der Fertigung selbst messen und
> `dimensions.json` -> `"verified": true` setzen.

Code-Samples zu diesem Bauteil:
[../../../code-samples/input/ds425-pushbutton/](../../../code-samples/input/ds425-pushbutton/)

## Masstabelle (mm)

| Mass | Wert | Bemerkung |
|------|-----:|-----------|
| Gehaeuse Breite x Tiefe | 6.0 x 6.0 | quadratisch |
| Gehaeuse Hoehe (ohne Stoessel) | 3.5 | ab Platine |
| Stoessel-Durchmesser | 3.5 | rund |
| Stoessel-Ueberstand | 1.5 | ab Gehaeuseoberkante; variiert je Bauform |
| Pin-Raster X (zwischen den Reihen) | 6.5 | |
| Pin-Raster Y (in der Reihe) | 4.5 | |

## Skizze (Draufsicht)

```
        6.0
   +-----------+        o = Pin
   | o       o |   ---
   |    ( )    |   4.5   ( ) = Stoessel, D 3.5
   | o       o |   ---
   +-----------+
         6.5
```

## Empfohlener Panel-Ausschnitt

- Kreis, Durchmesser **4.0 mm** (Stoessel 3.5 + 0.2 pro Seite Spiel)
- Der Taster wird von hinten gegen das Panel gesetzt (Gehaeuse 6x6 liegt an,
  Stoessel schaut durch den Ausschnitt nach vorne).
- Fuer eine Platine dahinter: Lochbild 2x2, Raster 6.5 x 4.5 mm.

Maschinenlesbar: [`dimensions.json`](dimensions.json)

## Bilder

Datenblatt-Ausschnitte, Messfotos und CAD-Screenshots in [`bilder/`](bilder/).
