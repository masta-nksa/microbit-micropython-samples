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
│   ├── onboard/                     eingebaut, KEINE Verkabelung, kein hardware/
│   │   ├── buttons/                 a-b-zaehler
│   │   ├── touch-logo/              logo-schalter                 (V2)
│   │   ├── pin-touch/               beruehr-toene
│   │   ├── accelerometer/           wasserwaage · shake-wuerfel
│   │   ├── compass/                 kompass-pfeil
│   │   ├── microphone/              lautstaerke-balken            (V2)
│   │   ├── temperature/             temperatur-anzeigen
│   │   ├── light-level/             nachtlicht
│   │   ├── display/                 bilder-und-text · einzelne-pixel
│   │   ├── speaker/                 melodie-und-sound             (V2)
│   │   └── radio/                   senden-empfangen         (2 micro:bits)
│   ├── input/
│   │   ├── ds425-pushbutton/
│   │   │   ├── ton-bei-druck/       main.py · README.md · wiring/
│   │   │   └── ton-solange-gedrueckt/
│   │   └── ec11-encoder/
│   │       ├── drehen-zaehler/
│   │       ├── drehen-und-druck/
│   │       └── ton-hoehe-einstellen/
│   ├── servo/
│   │   └── miuzei-9g-servo/
│   │       ├── a-b-drehen/
│   │       ├── zwei-stellungen/
│   │       ├── sweep/
│   │       └── winkel-mit-encoder/
│   └── output/                      geplant (Display, Segmentanzeige, LED-Strip)
│
└── hardware/                        Masse fuers CAD, gleicher Pfad wie code-samples
                                     (nur fuer externe Bauteile, nicht fuer onboard/)
    ├── input/
    │   ├── ds425-pushbutton/        README.md · dimensions.json · bilder/
    │   └── ec11-encoder/
    └── servo/
        └── miuzei-9g-servo/
```

## Samples

### onboard (eingebaut, kein Aufbau)

| Bauteil | Sample | Beschreibung |
|---------|--------|--------------|
| [buttons](code-samples/onboard/buttons/) | [a-b-zaehler](code-samples/onboard/buttons/a-b-zaehler/) | A zaehlt hoch, B runter, A+B = Reset |
| [touch-logo](code-samples/onboard/touch-logo/) | [logo-schalter](code-samples/onboard/touch-logo/logo-schalter/) | Logo antippen schaltet ein Herz an/aus (V2) |
| [pin-touch](code-samples/onboard/pin-touch/) | [beruehr-toene](code-samples/onboard/pin-touch/beruehr-toene/) | P0/P1/P2 antippen spielt je einen Ton |
| [accelerometer](code-samples/onboard/accelerometer/) | [wasserwaage](code-samples/onboard/accelerometer/wasserwaage/) | Leuchtpunkt zeigt die Neigung |
| [accelerometer](code-samples/onboard/accelerometer/) | [shake-wuerfel](code-samples/onboard/accelerometer/shake-wuerfel/) | Schuetteln = Zufallszahl 1..6 |
| [compass](code-samples/onboard/compass/) | [kompass-pfeil](code-samples/onboard/compass/kompass-pfeil/) | Pfeil zeigt immer nach Norden |
| [microphone](code-samples/onboard/microphone/) | [lautstaerke-balken](code-samples/onboard/microphone/lautstaerke-balken/) | Lautstaerke als Balken (V2) |
| [temperature](code-samples/onboard/temperature/) | [temperatur-anzeigen](code-samples/onboard/temperature/temperatur-anzeigen/) | Knopf A -> Temperatur scrollt durch |
| [light-level](code-samples/onboard/light-level/) | [nachtlicht](code-samples/onboard/light-level/nachtlicht/) | wird es dunkel, leuchtet die Matrix |
| [display](code-samples/onboard/display/) | [bilder-und-text](code-samples/onboard/display/bilder-und-text/) | Bilderfolge und Lauftext |
| [display](code-samples/onboard/display/) | [einzelne-pixel](code-samples/onboard/display/einzelne-pixel/) | Leuchtpunkt mit den Knoepfen bewegen |
| [speaker](code-samples/onboard/speaker/) | [melodie-und-sound](code-samples/onboard/speaker/melodie-und-sound/) | Melodie, Soundeffekt, Ton per Logo (V2) |
| [radio](code-samples/onboard/radio/) | [senden-empfangen](code-samples/onboard/radio/senden-empfangen/) | zwei micro:bits funken sich Zahlen zu |

### input

| Bauteil | Sample | Beschreibung |
|---------|--------|--------------|
| [ds425-pushbutton](code-samples/input/ds425-pushbutton/) | [ton-bei-druck](code-samples/input/ds425-pushbutton/ton-bei-druck/) | Herz + kurzer Ton beim Druecken |
| [ds425-pushbutton](code-samples/input/ds425-pushbutton/) | [ton-solange-gedrueckt](code-samples/input/ds425-pushbutton/ton-solange-gedrueckt/) | Dauerton, solange gehalten wird |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [drehen-zaehler](code-samples/input/ec11-encoder/drehen-zaehler/) | Wert 0..9 per Drehknopf |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [drehen-und-druck](code-samples/input/ec11-encoder/drehen-und-druck/) | zusaetzlich: Druck = Reset auf 0 |
| [ec11-encoder](code-samples/input/ec11-encoder/) | [ton-hoehe-einstellen](code-samples/input/ec11-encoder/ton-hoehe-einstellen/) | Drehen = Tonhoehe, Druck = an/aus |

### servo

| Bauteil | Sample | Beschreibung |
|---------|--------|--------------|
| [miuzei-9g-servo](code-samples/servo/miuzei-9g-servo/) | [a-b-drehen](code-samples/servo/miuzei-9g-servo/a-b-drehen/) | Knopf A/B drehen den Servo, A+B zurueck auf 0 |
| [miuzei-9g-servo](code-samples/servo/miuzei-9g-servo/) | [zwei-stellungen](code-samples/servo/miuzei-9g-servo/zwei-stellungen/) | Knopf A = 0 Grad, Knopf B = 180 Grad |
| [miuzei-9g-servo](code-samples/servo/miuzei-9g-servo/) | [sweep](code-samples/servo/miuzei-9g-servo/sweep/) | faehrt langsam hin und her, Knopf A haelt an |
| [miuzei-9g-servo](code-samples/servo/miuzei-9g-servo/) | [winkel-mit-encoder](code-samples/servo/miuzei-9g-servo/winkel-mit-encoder/) | EC11-Drehknopf stellt den Winkel |

*Weitere Kategorien, Bauteile und Samples folgen.*

## Neues Sample hinzufuegen

1. Ordner `code-samples/<kategorie>/<bauteil>/<sample>/` anlegen mit `main.py`
   und `README.md`. Bei externen Bauteilen zusaetzlich `wiring/`.
2. Die `README.md` nach dem festen Abschnitts-Schema aufbauen (Details:
   [code-samples/README.md](code-samples/README.md#aufbau-einer-sample-readme)).
   Kurz: Beschreibung -> Material -> Verkabelung -> Foto -> Wie der Code
   funktioniert -> **`## Programm` mit dem Code direkt darunter** -> Uebertragen
   -> Erwartetes Verhalten -> Erweiterungen.
3. Im Abschnitt `## Programm` nur die zwei Marker setzen, den Code NICHT von
   Hand einfuegen:

   ```
   <!-- CODE:START -->
   <!-- CODE:END -->
   ```

4. `python tools/build_readme.py` ausfuehren - fuegt `main.py` zwischen die
   Marker ein. Nach jeder Aenderung an `main.py` erneut laufen lassen;
   `python tools/build_readme.py --check` meldet veraltete READMEs.

## Hinweise

- micro:bit **V2** hat einen eingebauten Lautsprecher und ein Mikrofon.
  Toene laufen mit `music.pitch(freq, dauer, pin=None)` ueber den Lautsprecher.
- Die Pins P0/P1/P2 haben abschaltbare interne Pull-up-/Pull-down-Widerstaende.
