# senden-empfangen

Bauteil: [Funk (radio)](../README.md) · Kategorie: onboard

Dasselbe Programm auf **zwei** micro:bits. Knopf **A** zaehlt hoch und funkt
die Zahl zum anderen Board, das sie anzeigt und kurz piept.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 2 | micro:bit V2.2 (beide mit diesem Programm) |

## Hardware

Eingebaut, kein Aufbau noetig. Beide Boards brauchen dieselbe `GRUPPE` im
Code. Arbeiten mehrere Teams im selben Raum, bekommt jedes Team eine eigene
Gruppennummer.

## Wie der Code funktioniert

- `radio.on()` schaltet den Funk ein, `radio.config(group=GRUPPE)` legt die
  Gruppe fest - nur Boards mit derselben Gruppe hoeren sich.
- `radio.send(str(zaehler))` sendet - immer **Text**, darum `str(...)`.
- `radio.receive()` gibt die naechste Nachricht zurueck oder `None`, wenn
  gerade nichts angekommen ist. Darum die Pruefung `if nachricht is not None`.
- `nachricht[-1]` ist das letzte Zeichen - reicht, um eine Ziffer auf der
  Matrix zu zeigen.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: senden-empfangen  (Funk zwischen zwei micro:bits)
# Board:   BBC micro:bit V2.2  (zwei Stueck)
# Sprache: MicroPython
#
# Ziel: Dasselbe Programm laeuft auf BEIDEN micro:bits. Knopf A zaehlt einen
#       Wert hoch und funkt ihn zum anderen Board. Wer eine Nachricht
#       empfaengt, zeigt die Zahl an und piept kurz.
#
# --------------------------------------------------------------------------
# Hardware
# --------------------------------------------------------------------------
#   Nichts anschliessen - der Funk ist eingebaut. Nur brauchst du zwei
#   micro:bits, beide mit diesem Programm. Beide muessen dieselbe GRUPPE
#   benutzen (unten). Reichweite offen ca. 10..20 m.
# --------------------------------------------------------------------------

from microbit import *
import radio
import music

GRUPPE = 23   # auf beiden Boards gleich! Andere Teams: andere Zahl waehlen.

radio.on()
radio.config(group=GRUPPE)

zaehler = 0
display.show(Image.ARROW_N)

while True:
    # --- Senden ---
    if button_a.was_pressed():
        zaehler = zaehler + 1
        radio.send(str(zaehler))      # radio.send braucht Text
        display.show(str(zaehler % 10))

    # --- Empfangen ---
    nachricht = radio.receive()       # None, wenn nichts da ist
    if nachricht is not None:
        display.show(nachricht[-1])   # letzte Ziffer der empfangenen Zahl
        music.pitch(880, 80, pin=None)
        print("empfangen:", nachricht)

    sleep(20)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

Auf **beide** micro:bits denselben Code laden.
<https://python.microbit.org/v/beta> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- beide Boards zeigen zuerst einen Pfeil nach oben
- auf Board 1 A druecken -> Board 2 zeigt die Zahl + piept
- auf Board 2 A druecken -> Board 1 zeigt dessen Zahl + piept
- jedes Board hat seinen eigenen Zaehler

## Moegliche Erweiterungen

- statt einer Zahl `radio.send("ping")` und beim Empfang ein Herz zeigen
- Schuetteln sendet eine Wuerfelzahl an alle
- Chat: A und B waehlen aus mehreren festen Nachrichten
- `radio.config(power=7)` (0..7) - Sendeleistung / Reichweite
