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

### Sample mit externer Bibliothek (2. Datei)

Nutzt ein Sample eine mitgelieferte Bibliothek (z. B. `tm1637.py`, siehe
[output/tm1637-4digit/](output/tm1637-4digit/)), kommt vor `## Programm` ein
eigener Abschnitt `## Bibliothek: <dateiname>` mit einem zweiten Marker-Paar,
das den Dateinamen nach dem Doppelpunkt traegt:

```
<!-- CODE:START:tm1637.py -->
<!-- CODE:END -->
```

`build_readme.py` fuellt jedes Marker-Paar mit der jeweils genannten Datei -
ohne Namen `main.py`, mit Namen die Datei mit genau diesem Namen im selben
Ordner. Wie man eine zweite Datei im Online-Editor anlegt, steht in
[docs/setup.md](../docs/setup.md#zweite-datei-hinzufuegen-z-b-eine-mitgelieferte-bibliothek).

### Teststand festhalten

Sobald ein Sample (oder ein ganzes Bauteil) auf echter Hardware ausprobiert
wurde, kommt das als kurzer **"Stand"-Satz mit Datum** direkt unter die
Kurzbeschreibung am Anfang der README - Bauteil-README fuer "gilt fuer alle
Samples", einzelne Sample-README wenn nur eines geprueft ist:

```
**Stand (12.09.2026):** auf echter Hardware getestet - funktioniert.
```

bzw. bei offenen Punkten kurz benennen, was noch fehlt (z. B. "noch nicht
getestet", "ein Wert noch nicht kalibriert"). Kein eigener Abschnitt, keine
Tabelle - nur ehrlich festhalten, was tatsaechlich schon lief. Beispiele:
[tm1637-4digit](output/tm1637-4digit/README.md), [hc-sr04-abstandssensor](input/hc-sr04-abstandssensor/README.md).

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
