# onboard

Alles, was **schon im micro:bit V2.2 eingebaut** ist: Knoepfe, LED-Matrix,
Lautsprecher, Mikrofon, Beschleunigungssensor, Kompass, Temperatursensor.

Der natuerliche Einstieg: laeuft ohne jeden Aufbau, nur der micro:bit am
USB-Kabel. Externe Bauteile kommen danach unter [`../input/`](../input/) und
[`../output/`](../output/) dazu.

## Unterschied zu `input/` und `output/`

| | extern (`input/`, `output/`) | eingebaut (`onboard/`) |
|---|---|---|
| `main.py` + `README.md` | ja | ja |
| Code im README-Abschnitt `## Programm` | ja (auto aus `main.py`) | ja (auto aus `main.py`) |
| Ordner `wiring/` | ja | nein (nichts zu verkabeln) |
| Masse unter `hardware/` | ja | nein (kein Panel-Ausschnitt) |
| Materialliste | micro:bit + Bauteile | nur `1x micro:bit V2.2` |
| README-Abschnitt Verkabelung | ASCII-Skizze | ersetzt durch *Hardware: eingebaut* |
| README-Abschnitt *Foto der Verkabelung* | ja | nein |

Der genaue Abschnittsaufbau steht in
[../README.md](../README.md#aufbau-einer-sample-readme).

## Bauteile

| Bauteil | Typ | API (Kurz) | Samples |
|---------|-----|------------|---------|
| [buttons/](buttons/) | Eingang | `button_a.was_pressed()` | a-b-zaehler |
| [touch-logo/](touch-logo/) | Eingang (V2) | `pin_logo.is_touched()` | logo-schalter |
| [pin-touch/](pin-touch/) | Eingang | `pin0.is_touched()` | beruehr-toene |
| [accelerometer/](accelerometer/) | Eingang | `accelerometer.get_x()`, `.was_gesture()` | wasserwaage, shake-wuerfel |
| [compass/](compass/) | Eingang | `compass.heading()` | kompass-pfeil |
| [microphone/](microphone/) | Eingang (V2) | `microphone.sound_level()` | lautstaerke-balken |
| [temperature/](temperature/) | Eingang | `temperature()` | temperatur-anzeigen |
| [light-level/](light-level/) | Eingang | `display.read_light_level()` | nachtlicht |
| [display/](display/) | Ausgang | `display.show()`, `.scroll()`, `.set_pixel()` | bilder-und-text, einzelne-pixel |
| [speaker/](speaker/) | Ausgang (V2) | `music.play()`, `audio.play()` | melodie-und-sound |
| [radio/](radio/) | Ein/Ausgang | `radio.send()`, `radio.receive()` | senden-empfangen |

⚡ **V2** = braucht micro:bit V2 (Lautsprecher / Mikrofon / Touch-Logo). Wir haben V2.2 - passt.

`radio/` braucht **zwei** micro:bits, sonst ist der Aufbau ueberall gleich:
nur der micro:bit am USB-Kabel.
