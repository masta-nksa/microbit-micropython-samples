# LED-Matrix 5x5

25 einzeln ansteuerbare LEDs, Helligkeit je 0..9. Zeigt Zahlen, Text
(scrollend), fertige Bilder oder frei gesetzte Pixel.

- Eingebaut, kein Aufbau noetig
- `display`, `Image` - immer verfuegbar

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `display.show(Image.HEART)` | ein Bild / Zeichen anzeigen |
| `display.show("A")` | einzelnes Zeichen |
| `display.scroll("Hallo")` | Text von rechts nach links durchlaufen lassen |
| `display.set_pixel(x, y, h)` | Pixel `x,y` (0..4) auf Helligkeit `h` (0..9) |
| `display.get_pixel(x, y)` | Helligkeit eines Pixels lesen |
| `display.clear()` | alle LEDs aus |
| `Image("90000:...")` | eigenes Bild aus 5 Zeilen Helligkeitswerten |

Fertige Bilder: `Image.HAPPY`, `Image.HEART`, `Image.DUCK`, `Image.GHOST`,
`Image.ROCKET`, `Image.ALL_CLOCKS`, ... (Liste in der micro:bit-Doku).

## Samples (Lernreihenfolge)

1. [bilder-und-text/](bilder-und-text/) - A zeigt eine Bilderfolge, B scrollt Text
2. [einzelne-pixel/](einzelne-pixel/) - einen Leuchtpunkt mit den Knoepfen bewegen
