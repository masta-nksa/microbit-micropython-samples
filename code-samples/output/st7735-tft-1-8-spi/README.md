# 1.8" TFT SPI Display (ST7735)

Farbiges 128x160-Pixel-TFT-Display mit **ST7735**-Treiberchip, angesteuert
per SPI (5 Signalleitungen: SCK, SDA/MOSI, A0/DC, RESET, CS).

**Stand (16.09.2026):** Treiber `st7735.py` ist eine eigene Portierung
(siehe unten) - **noch nicht auf echter Hardware getestet.** Vor dem Einsatz
mit [farbflaechen](farbflaechen/) pruefen, ob Bild/Farben stimmen.

## Anschluesse am Modul

| Pin (Beschriftung auf dem Modul) | Bedeutung |
|---|---|
| `SCK` (auch `SCL`) | SPI-Takt |
| `SDA` (auch `MOSI`, `DIN`) | Daten zum Display |
| `A0` (auch `DC`, `RS`) | Data/Command-Umschaltung |
| `RESET` (auch `RST`) | Reset, aktiv Low |
| `CS` | Chip-Select, aktiv Low |
| `LED` (auch `BL`, `BLK`) | Backlight - bei den meisten Modulen reicht dauerhaft an 3V |
| `VCC` | Plus - **am eigenen Modul pruefen**, manche billigen Module wollen 5V |
| `GND` | Masse |

Wie beim TM1637: **Beschriftung auf dem Modul massgeblich**, nicht die
Position der Pins.

## Anschluss an den micro:bit

```
   micro:bit          ST7735-Modul
  +---------+        +------------+
  |     13  |--------| SCK        |   Hardware-SPI-Takt (fix)
  |     15  |--------| SDA / MOSI |   Hardware-SPI-Daten (fix)
  |     12  |--------| A0 / DC    |
  |     16  |--------| RESET      |
  |      8  |--------| CS         |
  |      3V |--------| LED        |
  |      3V |--------| VCC        |
  |     GND |--------| GND        |
  +---------+        +------------+
```

- `P13`/`P15` sind die festen Hardware-SPI-Pins des micro:bit (`microbit.spi`) -
  hier nicht frei waehlbar wie bei den bit-gebangten Protokollen (TM1637,
  WS2812B). `MISO` (P14) bleibt unbenutzt, die meisten Module liefern
  sowieso keine Daten zurueck.
- `A0/DC`, `RESET`, `CS` sind frei waehlbar; P8/P12/P16 sind nur ein
  Vorschlag, in `main.py` anpassbar.
- Faellt das Bild aus/bleibt weiss: zuerst `RESET` und `CS` pruefen, danach
  `A0/DC` (vertauschtes Data/Command fuehrt zu Datenmuell auf dem Screen).

## Bibliothek: eigene Portierung `st7735.py`

Fuer den ST7735 gibt es keine fertige micro:bit-native Bibliothek wie
`mcauser/microbit-tm1637` fuers TM1637 - alle verbreiteten MicroPython-Treiber
sind auf `machine.SPI`/`machine.Pin` zugeschnitten, die es auf dem micro:bit
nicht gibt. `st7735.py` ist deshalb eine eigene, schlanke Portierung der
Init-Sequenz und Pixel-Logik aus
[adafruit/micropython-adafruit-rgb-display](https://github.com/adafruit/micropython-adafruit-rgb-display)
(MIT-Lizenz, Radomir Dopieralski) auf `microbit.spi` + `write_digital()`.

**Bewusst kein Framebuffer:** ein volles 128x160-Bild waere 40 KB (2 Byte je
Pixel) - zu viel RAM fuer den micro:bit. Stattdessen schreibt `fill_rect()`
die Pixel blockweise direkt per SPI, ohne den Bildschirminhalt im RAM zu
halten.

```python
from microbit import pin8, pin12, pin16
from st7735 import ST7735, color565, BLACK, WHITE, RED, GREEN, BLUE

display = ST7735(cs=pin8, dc=pin12, rst=pin16)   # Standard: 128x160, 4 MHz SPI

display.fill(RED)                    # ganzer Bildschirm - fuer haeufige Updates zu langsam
display.fill_rect(10, 10, 40, 40, GREEN)   # nur ein Rechteck - das eigentliche Werkzeug
display.pixel(5, 5, WHITE)
farbe = color565(255, 140, 0)        # eigene Farbe aus R/G/B (0-255) bauen
```

## Performance: nicht bei jedem Update alles neu zeichnen

`display.fill()` beschreibt alle 20480 Pixel - fuer einen einmaligen
Bildschirmwechsel ok, aber spuerbar traege, wenn es in einer Schleife bei
jedem Update passiert (z. B. ein Zaehler, eine Uhr, ein Messwert). Die
Faustregel:

- **Nur das Rechteck neu zeichnen, das sich tatsaechlich veraendert hat**
  (`fill_rect()` auf die genaue Stelle, nicht `fill()` auf alles).
- Bei mehreren unabhaengigen Elementen (z. B. 4 Ziffern) **pruefen, welche
  sich seit dem letzten Mal veraendert haben**, und nur die neu zeichnen -
  siehe [zahlen-zaehler](zahlen-zaehler/).
- Hardware-SPI ist bereits deutlich schneller als das bit-gebangte
  TM1637-Protokoll - der Flaschenhals ist fast immer die **Pixel-Menge**,
  nicht die Uebertragungsgeschwindigkeit selbst.

## Samples (Lernreihenfolge)

1. [farbflaechen/](farbflaechen/) - Grundfunktion: Bildschirm einfaerben, Rechtecke zeichnen
2. [zahlen-zaehler/](zahlen-zaehler/) - Knopf A/B zaehlen 0..9999 mit eigener Blockschrift,
   nur die veraenderten Ziffern werden neu gezeichnet

Masse fuers CAD: [../../../hardware/output/st7735-tft-1-8-spi/](../../../hardware/output/st7735-tft-1-8-spi/)
