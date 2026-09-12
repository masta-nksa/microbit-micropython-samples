# zaehler

Bauteil: [TM1637 4-Digit-Anzeige](../README.md) · Kategorie: output

Knopf **A** zaehlt hoch, Knopf **B** runter, **A+B** setzt auf 0 zurueck.
Wie das onboard-Sample [a-b-zaehler](../../../onboard/buttons/a-b-zaehler/),
nur mit der externen Anzeige (Bereich 0..9999) statt der LED-Matrix (0..9).

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | TM1637 4-Digit-Anzeige |
| 4 | Jumperkabel |

Masse fuers CAD: [../../../../hardware/output/tm1637-4digit/](../../../../hardware/output/tm1637-4digit/)

## Verkabelung

Identisch zu [zahl-anzeigen](../zahl-anzeigen/README.md#verkabelung):

```
   P1 -> CLK      P2 -> DIO      3V -> VCC      GND -> GND
```

Details: [Bauteil-README](../README.md#anschluss-an-den-micro-bit).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Wie der Code funktioniert

- **A+B zuerst pruefen** (`is_pressed()` fuer beide), sonst wuerde ein Druck
  auf beide Knoepfe nur hoch- oder runterzaehlen.
- `button_x.was_pressed()`: reagiert einmal pro Druck (Flanke), kein Prellen.
- `max(0, min(9999, zaehler))` haelt den Wert im darstellbaren Bereich.
- Treiber (`_start`/`_stop`/`_write_byte`/`anzeige`) wie in
  [zahl-anzeigen](../zahl-anzeigen/).

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: zaehler  (TM1637 4-Digit-Anzeige)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt hoch, Knopf B runter, A+B setzt auf 0 zurueck.
#       Wie das onboard-Sample "a-b-zaehler", nur mit der externen
#       4-stelligen Anzeige statt der LED-Matrix (Bereich 0..9999 statt 0..9).
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle TM1637-Samples)
#   Anzeige CLK -> P1     Anzeige DIO -> P2
#   Anzeige VCC -> 3V     Anzeige GND -> GND
# --------------------------------------------------------------------------

from microbit import *

CLK = pin1
DIO = pin2
HELLIGKEIT = 3

SEGMENTE = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]


def _start():
    CLK.write_digital(1)
    DIO.write_digital(1)
    DIO.write_digital(0)
    CLK.write_digital(0)


def _stop():
    DIO.write_digital(0)
    CLK.write_digital(1)
    DIO.write_digital(1)


def _write_byte(b):
    for i in range(8):
        CLK.write_digital(0)
        DIO.write_digital((b >> i) & 1)
        CLK.write_digital(1)
    CLK.write_digital(0)
    DIO.read_digital()
    CLK.write_digital(1)
    CLK.write_digital(0)


def anzeige(d0, d1, d2, d3, doppelpunkt=False):
    _start()
    _write_byte(0x40)
    _stop()

    _start()
    _write_byte(0xC0)
    for i, d in enumerate([d0, d1, d2, d3]):
        wert = SEGMENTE[d] if d is not None else 0x00
        if i == 1 and doppelpunkt:
            wert |= 0x80
        _write_byte(wert)
    _stop()

    _start()
    _write_byte(0x88 | HELLIGKEIT)
    _stop()


def zahl_in_ziffern(n):
    n = max(0, min(9999, n))
    text = str(n).rjust(4)
    return [int(z) if z != " " else None for z in text]


# ----- Zaehler -----
zaehler = 0
anzeige(*zahl_in_ziffern(zaehler))

while True:
    # A + B zuerst pruefen, sonst wuerde es nur hoch- oder runterzaehlen
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0
    elif button_a.was_pressed():
        zaehler = zaehler + 1
    elif button_b.was_pressed():
        zaehler = zaehler - 1

    zaehler = max(0, min(9999, zaehler))
    anzeige(*zahl_in_ziffern(zaehler))
    sleep(50)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Start: `0`
- A druecken -> `1`, `2`, ... bis `9999`
- B druecken -> wieder runter bis `0`
- A und B zusammen -> `0`

## Moegliche Erweiterungen

- Schrittweite per EC11-Encoder statt Knopf einstellen
- bei Erreichen von `9999` kurz blinken
- Wert beim Ausschalten merken (Datei auf dem micro:bit speichern)
