# naeherungsalarm

Bauteil: [HC-SR04 Ultraschall-Abstandssensor](../README.md) · Kategorie: input

Piept schneller, je naeher ein Hindernis ist - wie eine Einparkhilfe im
Auto. Weit weg: Stille. Ganz nah: schnelles Dauerpiepsen.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | HC-SR04 Ultraschall-Abstandssensor |
| 4 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/input/hc-sr04-abstandssensor/](../../../../hardware/input/hc-sr04-abstandssensor/)

## Verkabelung

Identisch zu [abstand-messen](../abstand-messen/README.md#verkabelung):

```
   P1 -> Trig      P2 -> Echo      3V -> Vcc      GND -> Gnd
```

Details: [Bauteil-README](../README.md#anschluss-an-den-microbit---standard-einfach-und-sicher-3-v).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- Gleiche `abstand_cm()`-Funktion wie in [abstand-messen](../abstand-messen/).
- Das Piep-**Intervall** wird linear zwischen 50 ms (bei `NAH_CM`) und
  500 ms (bei `FERN_CM`) berechnet - naeher heisst kuerzeres Intervall.
- `letzter_beep` (aus `running_time()`) sorgt dafuer, dass nur alle
  `intervall` Millisekunden ein Ton gespielt wird, nicht bei jedem
  Schleifendurchlauf.
- `music.pitch(1500, 40, pin=None)` spielt einen kurzen Ton ueber den
  eingebauten Lautsprecher, `P0` bleibt fuer andere Bauteile frei.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: naeherungsalarm  (HC-SR04 Ultraschall-Abstandssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Piept schneller, je naeher ein Hindernis ist - wie eine Einparkhilfe.
#       Weit weg: Stille. Ganz nah: schnelles Dauerpiepsen.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie "abstand-messen")
#   Sensor Trig -> P1     Sensor Echo -> P2
#   Sensor Vcc  -> 3V     Sensor Gnd  -> GND
# --------------------------------------------------------------------------

import machine
import music
from microbit import *

TRIG = pin1
ECHO = pin2

NAH_CM = 5      # ab hier: schnellstes Piepsen
FERN_CM = 60    # ab hier: Stille


def abstand_cm():
    TRIG.write_digital(0)
    sleep(2)
    TRIG.write_digital(1)
    sleep(1)
    TRIG.write_digital(0)
    dauer_us = machine.time_pulse_us(ECHO, 1, 30000)
    if dauer_us < 0:
        return None
    return dauer_us / 58.0


letzter_beep = 0

while True:
    cm = abstand_cm()
    jetzt = running_time()

    if cm is not None and cm < FERN_CM:
        cm = max(NAH_CM, cm)
        # naeher -> kuerzeres Intervall (50 ms ganz nah .. 500 ms an der Grenze)
        intervall = int(50 + (cm - NAH_CM) / (FERN_CM - NAH_CM) * 450)
        if jetzt - letzter_beep >= intervall:
            music.pitch(1500, 40, pin=None)   # ueber den eingebauten Lautsprecher
            letzter_beep = jetzt
        display.show(Image.TARGET)
    else:
        display.clear()

    sleep(20)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Hand langsam an den Sensor heranfuehren -> die Pieptoene werden schneller
- Ab `FERN_CM` (60 cm) ist es still, die Matrix ist leer
- Naeher als `FERN_CM` -> Zielsymbol auf der Matrix

## Moegliche Erweiterungen

- Tonhoehe statt Intervall aendern (je naeher, desto hoeher)
- ab einer Schwelle einen Dauerton statt Piepsen
- Servo eine Schranke schliessen lassen, wenn zu nah

## Hinweis

`NAH_CM`/`FERN_CM` und die Intervall-Grenzen (50-500 ms) nach Bedarf anpassen.
