# output

Ausgabe-Bauteile. Geplant, Bauteile folgen mit der Zeit.

## Bauteile (geplant)

| Bauteil | Typ |
|---------|-----|
| lcd-display | LCD (z. B. 16x2 mit I2C-Backpack) |
| segmentanzeige | 7-Segment-Anzeige (z. B. TM1637) |
| led-strip | adressierbarer LED-Streifen (WS2812 / NeoPixel) |
| oled-display | OLED 128x64 (SSD1306, I2C) |

Aufbau je Bauteil wie bei `input/`: `output/<bauteil>/<sample>/` mit
`main.py`, `README.md`, `wiring/`. Masse unter `hardware/output/<bauteil>/`.
