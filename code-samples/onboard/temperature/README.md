# Temperatursensor

Der micro:bit misst die Temperatur **des Prozessorchips**, nicht direkt die
Raumluft. Der Wert liegt darum meist ein paar Grad zu hoch und reagiert
traege. Fuer Trends ("waermer/kaelter") und einfache Experimente reicht es.

- Eingebaut, kein Aufbau noetig
- `temperature()` - Funktion, verfuegbar ueber `from microbit import *`

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `temperature()` | aktuelle Temperatur in Grad Celsius (ganze Zahl) |

## Samples (Lernreihenfolge)

1. [temperatur-anzeigen/](temperatur-anzeigen/) - Knopf A druecken -> Temperatur laeuft durch
