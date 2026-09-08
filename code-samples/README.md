# Code-Samples

Aufbau: `kategorie / bauteil / sample`

- **kategorie** - z. B. `onboard`, `input`, `output`, `servo`, `sound`
- **bauteil** - konkretes Bauteil, z. B. `ds425-pushbutton`, `ec11-encoder`
- **sample** - ein lauffaehiges Beispiel: `main.py`, `README.md` (extern zusaetzlich `wiring/`)

Die Masse jedes Bauteils fuers CAD liegen unter demselben Pfad in
[`../hardware/`](../hardware/), z. B. `hardware/input/ds425-pushbutton/`.

## Aufbau einer Sample-README

Jede Sample-`README.md` ist eine abgeschlossene Seite und hat immer dieselben
Abschnitte in dieser Reihenfolge:

| Abschnitt | Inhalt |
|-----------|--------|
| Titel + 1-2 Saetze | was das Sample macht |
| `## Material` | Bauteilliste (`onboard`: nur `1x micro:bit V2.2`) |
| `## Verkabelung` | ASCII-Skizze — bei `onboard/` stattdessen `## Hardware` "eingebaut, kein Aufbau" |
| `## Foto der Verkabelung` | Platzhalter fuer das Foto — nur extern, nicht bei `onboard/` |
| `## Wie der Code funktioniert` | kurze Erklaerung (Stichpunkte / kleine Tabelle) |
| `## Programm` | **der vollstaendige Code, direkt unter der Erklaerung** |
| `## Auf den micro:bit uebertragen` | immer gleicher Text (Editor-Link) |
| `## Erwartetes Verhalten` | was man beim Testen sieht/hoert |
| `## Moegliche Erweiterungen` | Ideen zum Weitermachen |

Der Code im Abschnitt `## Programm` wird **nicht von Hand** eingefuegt: zwischen
den Zeilen

```
<!-- CODE:START -->
<!-- CODE:END -->
```

traegt [`tools/build_readme.py`](../tools/build_readme.py) den aktuellen Inhalt
von `main.py` ein. Einzige Quelle bleibt `main.py`; nach jeder Aenderung daran
`python tools/build_readme.py` ausfuehren (`--check` meldet veraltete READMEs).

## Kategorien

| Kategorie | Inhalt | Status |
|-----------|--------|--------|
| [onboard/](onboard/) | eingebaut: Knoepfe, Matrix, Lautsprecher, Mikrofon, Sensoren | in Arbeit |
| [input/](input/) | externe Eingabe: Taster, Rotary-Encoder, Poti, Joystick | in Arbeit |
| [servo/](servo/) | Servomotoren | in Arbeit |
| [output/](output/) | externe Ausgabe: LED-Strips, LCD-/OLED-Display, Segmentanzeige | in Arbeit |

Bei `onboard/` gibt es **keine Verkabelung** und keinen `hardware/`-Ordner -
alles ist schon im micro:bit V2.2 drin.

*Kategorien und Bauteile werden mit der Zeit erweitert.*
