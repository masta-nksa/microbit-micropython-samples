# Sample: zahlen-zaehler  (1.8" TFT SPI Display, ST7735)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Knopf A zaehlt hoch, Knopf B runter, A+B setzt auf 0 zurueck -
#       wie "zaehler" beim TM1637, aber auf dem Farbdisplay mit einer
#       selbstgebauten 4-stelligen Blockschrift.
#
#       Performance-Punkt: NICHT bei jedem Update display.fill() auf dem
#       ganzen Bildschirm aufrufen (128x160 Pixel dauern spuerbar). Stattdessen
#       wird jede der 4 Ziffern mit dem vorherigen Wert verglichen und nur
#       die tatsaechlich veraenderten Ziffern-Rechtecke neu gezeichnet.
#       Bei einem einfachen Hoch-/Runterzaehler aendert sich meistens nur
#       die letzte Ziffer - der Rest bleibt unangetastet.
#
# --------------------------------------------------------------------------
# Verkabelung  (wie alle st7735-Samples)
#   Display SCK -> P13   Display SDA/MOSI -> P15   Display A0/DC -> P12
#   Display RESET -> P16   Display CS -> P8   Display LED/VCC -> 3V   GND -> GND
# --------------------------------------------------------------------------

from microbit import pin8, pin12, pin16, button_a, button_b, sleep
from st7735 import ST7735, BLACK, WHITE

display = ST7735(cs=pin8, dc=pin12, rst=pin16)

# 3x5-Punkte-Blockschrift, '1' = Pixel an
_FONT = {
    "0": ("111", "101", "101", "101", "111"),
    "1": ("010", "110", "010", "010", "111"),
    "2": ("111", "001", "111", "100", "111"),
    "3": ("111", "001", "111", "001", "111"),
    "4": ("101", "101", "111", "001", "001"),
    "5": ("111", "100", "111", "001", "111"),
    "6": ("111", "100", "111", "101", "111"),
    "7": ("111", "001", "010", "010", "010"),
    "8": ("111", "101", "111", "101", "111"),
    "9": ("111", "101", "111", "001", "111"),
    " ": ("000", "000", "000", "000", "000"),
}

SCALE = 8                       # ein Blockschrift-Pixel = 8x8 Bildschirm-Pixel
DIGIT_W = 3 * SCALE + 6         # Ziffernbreite + kleiner Abstand
DIGIT_H = 5 * SCALE
X0, Y0 = 4, 60                  # Startposition der 4-stelligen Anzeige


def draw_digit(index, char):
    x = X0 + index * DIGIT_W
    display.fill_rect(x, Y0, DIGIT_W, DIGIT_H, BLACK)  # nur DIESE Zelle loeschen
    rows = _FONT[char]
    for row in range(5):
        for col in range(3):
            if rows[row][col] == "1":
                display.fill_rect(x + col * SCALE, Y0 + row * SCALE, SCALE, SCALE, WHITE)


zaehler = 0
letzter_text = "    "  # erzwingt beim ersten Durchlauf, dass alle 4 Ziffern gezeichnet werden

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        zaehler = 0
    elif button_a.was_pressed():
        zaehler = zaehler + 1
    elif button_b.was_pressed():
        zaehler = zaehler - 1
    zaehler = max(0, min(9999, zaehler))

    text = "{:>4d}".format(zaehler)
    for i in range(4):
        if text[i] != letzter_text[i]:
            draw_digit(i, text[i])
    letzter_text = text

    sleep(50)
