# micro:bit V2.2 - MicroPython Sample Code

Sammlung einfacher, kommentierter Beispielprogramme fuer den **BBC micro:bit V2.2**,
programmiert in **MicroPython**. Entstanden fuer die Impulswoche an der
Neuen Kantonsschule Aarau.

Jede Aufgabe verbindet ein externes Bauteil ueber die Pins mit dem micro:bit
und enthaelt:

- den Sample-Code (`main.py`) mit ausfuehrlichen Kommentaren
- eine Beschreibung der Verkabelung (Text + ASCII-Skizze)
- einen Ordner `verkabelung/` fuer das reale Foto der Schaltung (nach dem Test)

## Editor

Alle Beispiele sind fuer den Online-Editor gedacht:
**<https://python.microbit.org/v/beta>**

Uebertragung Schritt fuer Schritt: [docs/setup.md](docs/setup.md)

## Aufgaben

| Nr. | Thema | Bauteil | Ordner |
|----:|-------|---------|--------|
| 1 | Einfacher Pushbutton am Pin | DS425 Momentary | [aufgaben/01-pushbutton](aufgaben/01-pushbutton) |

*Weitere Aufgaben folgen.*

## Repo-Struktur

```
micro_bit/
├── README.md
├── docs/
│   └── setup.md                 Editor + Uebertragung auf den micro:bit
└── aufgaben/
    └── 01-pushbutton/
        ├── README.md            Aufgabe, Material, Verkabelung
        ├── main.py              Sample-Code
        └── verkabelung/         Foto der realen Schaltung
```

## Hinweise

- micro:bit **V2** hat einen eingebauten Lautsprecher und ein Mikrofon.
  Toene laufen mit `music.pitch(freq, dauer, pin=None)` ueber den Lautsprecher.
- Die Pins P0/P1/P2 haben abschaltbare interne Pull-up-/Pull-down-Widerstaende.
