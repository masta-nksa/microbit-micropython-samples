# Code-Samples

Aufbau: `kategorie / bauteil / sample`

- **kategorie** - z. B. `onboard`, `input`, `output`, `servo`, `sound`
- **bauteil** - konkretes Bauteil, z. B. `ds425-pushbutton`, `ec11-encoder`
- **sample** - ein lauffaehiges Beispiel mit `main.py`, `README.md`, `wiring/`

Die Masse jedes Bauteils fuers CAD liegen unter demselben Pfad in
[`../hardware/`](../hardware/), z. B. `hardware/input/ds425-pushbutton/`.

## Kategorien

| Kategorie | Inhalt | Status |
|-----------|--------|--------|
| [onboard/](onboard/) | eingebaut: Knoepfe, Matrix, Lautsprecher, Mikrofon, Sensoren | in Arbeit |
| [input/](input/) | externe Eingabe: Taster, Rotary-Encoder, Poti, Joystick | in Arbeit |
| [output/](output/) | externe Ausgabe: LCD-Display, Segmentanzeige, LED-Strips | geplant |

Bei `onboard/` gibt es **keine Verkabelung** und keinen `hardware/`-Ordner -
alles ist schon im micro:bit V2.2 drin.

*Kategorien und Bauteile werden mit der Zeit erweitert.*
