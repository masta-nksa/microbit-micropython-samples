# micro:bit V2.2 - MicroPython Sample Code

Sammlung einfacher, kommentierter Beispielprogramme fuer den **BBC micro:bit V2.2**,
programmiert in **MicroPython**. Entstanden fuer die Impulswoche an der
Neuen Kantonsschule Aarau.

Jedes Sample ist eine in sich abgeschlossene Seite (`README.md`) mit:

- Aufgabe, Materialliste und Verkabelung (Text + ASCII-Skizze)
- dem vollstaendigen Programm - direkt in der README, automatisch aus `main.py`
  eingefuegt (siehe [`tools/`](tools/))
- einem Ordner `wiring/` fuer das reale Foto der Schaltung (nach dem Test)

Dazu die **Masse der Bauteile fuers CAD** unter [`hardware/`](hardware/)
(Panel-Ausschnitte fuer Taster, Displays usw.).

## Editor

Alle Beispiele sind fuer den Online-Editor gedacht:
**<https://python.microbit.org/v/beta>**

Uebertragung Schritt fuer Schritt: [docs/setup.md](docs/setup.md)

## Repo-Struktur

```
micro_bit/
├── README.md
├── docs/
│   └── setup.md                     Editor + Uebertragung auf den micro:bit
├── tools/
│   └── build_readme.py              fuegt main.py in die Sample-READMEs ein
│
├── code-samples/                    kategorie / bauteil / sample
│   ├── input/
│   │   ├── ds425-pushbutton/
│   │   │   ├── ton-bei-druck/       main.py · README.md · wiring/
│   │   │   └── ton-solange-gedrueckt/
│   │   └── ec11-encoder/
│   │       ├── drehen-zaehler/
│   │       ├── drehen-und-druck/
│   │       └── ton-hoehe-einstellen/
│   └── output/                      geplant (Display, Segmentanzeige, LED-Strip)
│
└── hardware/                        Masse fuers CAD, gleicher Pfad wie code-samples
    └── input/
        ├── ds425-pushbutton/        README.md · dimensions.json · bilder/
        └── ec11-encoder/
```

## Samples

### input

| Bauteil | Sample | Beschreibung |
|---------|--------|--------------|
| [ds425-pushbutton](code-samples/input/ds425-pushbutton/) | [ton-bei-druck](code-samples/input/ds425-pushbutton/ton-bei-druck/) | Herz + kurzer Ton beim Druecken |
| [ds425-pushbutton](code-samples/input/ds425-pushbutton/) | [ton-solange-gedrueckt](code-samples/input/ds425-pushbutton/ton-solange-gedrueckt/) | Dauerton, solange gehalten wird |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [drehen-zaehler](code-samples/input/ec11-encoder/drehen-zaehler/) | Wert 0..9 per Drehknopf |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [drehen-und-druck](code-samples/input/ec11-encoder/drehen-und-druck/) | zusaetzlich: Druck = Reset auf 0 |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [ton-hoehe-einstellen](code-samples/input/ec11-encoder/ton-hoehe-einstellen/) | Drehen = Tonhoehe, Druck = an/aus |

*Weitere Kategorien, Bauteile und Samples folgen.*

## Neues Sample hinzufuegen

1. Ordner `code-samples/<kategorie>/<bauteil>/<sample>/` anlegen mit `main.py`
   und `README.md` (in der README die zwei Marker `<!-- CODE:START -->` /
   `<!-- CODE:END -->` an die Stelle setzen, wo der Code stehen soll).
2. `python tools/build_readme.py` ausfuehren - fuegt `main.py` dort ein.
3. Nach jeder Aenderung an `main.py` das Skript erneut laufen lassen.
   `python tools/build_readme.py --check` meldet veraltete READMEs.

## Hinweise

- micro:bit **V2** hat einen eingebauten Lautsprecher und ein Mikrofon.
  Toene laufen mit `music.pitch(freq, dauer, pin=None)` ueber den Lautsprecher.
- Die Pins P0/P1/P2 haben abschaltbare interne Pull-up-/Pull-down-Widerstaende.
