# abstand-messen

Bauteil: [HC-SR04 Ultraschall-Abstandssensor](../README.md) · Kategorie: input

Den Abstand zu einem Hindernis messen und als **Balken auf der LED-Matrix**
zeigen (naeher = mehr LEDs). Der genaue Wert in cm geht zusaetzlich ueber
die serielle Konsole raus. Erstes Sample - die Verkabelung gilt fuer alle
HC-SR04-Samples.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | HC-SR04 Ultraschall-Abstandssensor |
| 4 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/input/hc-sr04-abstandssensor/](../../../../hardware/input/hc-sr04-abstandssensor/)

## Verkabelung

```
   micro:bit          HC-SR04
  +---------+        +---------+
  |      P1 |--------| Trig    |
  |      P2 |--------| Echo    |
  |      3V |--------| Vcc     |
  |     GND |--------| Gnd     |
  +---------+        +---------+
```

Betrieb an **3V** (statt 5V) - reduziert die Reichweite auf ca. 20-150 cm,
macht `Echo` dafuer ungefaehrlich fuer den micro:bit-Pin. Fuer mehr Reichweite
(5V + Spannungsteiler): [Bauteil-README](../README.md#mehr-reichweite-5-v--spannungsteiler-optional).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- `abstand_cm()` schickt einen 1-ms-Trigger-Impuls und misst dann mit
  `machine.time_pulse_us(ECHO, 1, 30000)` die Dauer des Echo-Pulses in
  Mikrosekunden. `dauer_us / 58.0` ergibt den Abstand in cm.
  Details: [Bauteil-README](../README.md#messung-in-micropython).
- Ein negativer Wert (Timeout) heisst "kein Echo" -> `None`.
- `balken(n)` zuendet `n` von 25 LEDs zeilenweise. `n` wird linear zwischen
  `NAH_CM` (Balken voll) und `FERN_CM` (Balken leer) berechnet.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: abstand-messen  (HC-SR04 Ultraschall-Abstandssensor)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Den Abstand zu einem Hindernis messen und als Balken auf der
#       LED-Matrix zeigen (naeher = mehr LEDs). Der Wert in cm geht
#       zusaetzlich ueber die serielle Konsole raus (Open Serial).
#
# --------------------------------------------------------------------------
# Verkabelung  (Betrieb an 3V - einfach und sicher, siehe Bauteil-README)
# --------------------------------------------------------------------------
#   Sensor Trig  ->  P1
#   Sensor Echo  ->  P2
#   Sensor Vcc   ->  3V   (statt der spezifizierten 5 V - reduziert die
#                          Reichweite, macht Echo aber ungefaehrlich fuer den Pin)
#   Sensor Gnd   ->  GND
#
#   Fuer mehr Reichweite (5V + Spannungsteiler an Echo): siehe Bauteil-README.
# --------------------------------------------------------------------------

import machine
from microbit import *

TRIG = pin1
ECHO = pin2

NAH_CM = 5     # ab hier: Balken komplett voll
FERN_CM = 40   # ab hier: Balken leer


def abstand_cm():
    TRIG.write_digital(0)
    sleep(2)
    TRIG.write_digital(1)
    sleep(1)                 # 1 ms Triggerimpuls (mehr als die geforderten 10 us)
    TRIG.write_digital(0)

    dauer_us = machine.time_pulse_us(ECHO, 1, 30000)   # auf HIGH-Puls warten, Timeout 30 ms
    if dauer_us < 0:
        return None           # kein Echo: zu nah, zu weit, oder nichts im Weg
    return dauer_us / 58.0     # Schallgeschwindigkeit -> cm


def balken(n):
    # n LEDs anzeigen (0..25), zeilenweise von oben
    n = max(0, min(25, n))
    display.clear()
    for i in range(n):
        display.set_pixel(i % 5, i // 5, 9)


while True:
    cm = abstand_cm()

    if cm is None:
        display.show(Image.NO)
        print("kein Echo")
    else:
        n = int(25 * (FERN_CM - cm) / (FERN_CM - NAH_CM))
        balken(n)
        print("Abstand:", round(cm, 1), "cm")

    sleep(100)   # >= 60 ms Pause zwischen Messungen (Datenblatt-Empfehlung)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Hand naeher an den Sensor halten (senkrecht, flache Flaeche) -> mehr LEDs leuchten
- Hand weiter weg -> weniger LEDs, ab `FERN_CM` nichts mehr
- Kein Hindernis im Bereich -> X-Symbol, "kein Echo" auf der seriellen Konsole
- **Open Serial** zeigt den genauen cm-Wert

## Moegliche Erweiterungen

- `NAH_CM`/`FERN_CM` an das eigene Projekt anpassen
- Balken durch eine Zahl ersetzen (`display.scroll(int(cm))`)
- mehrere Messungen mitteln, um Ausreisser zu glaetten
