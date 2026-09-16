# Sample: farbflaechen  (1.8" TFT SPI Display, ST7735)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Grundfunktion pruefen - Display initialisieren, ganzen Bildschirm
#       nacheinander in ein paar Farben fuellen, dann drei Rechtecke.
#       Nutzt die Bibliothek st7735.py (2. Datei im Projekt) - siehe README.
#
#       fill() beschreibt hier bewusst den GANZEN Bildschirm (128x160 =
#       20480 Pixel) - fuer einen einmaligen Test ok, aber spuerbar
#       langsamer als ein kleines fill_rect(). Im naechsten Sample
#       (zahlen-zaehler) wird nur noch das veraenderte Rechteck neu
#       gezeichnet statt bei jedem Update der ganze Screen.
#
# --------------------------------------------------------------------------
# Verkabelung
#   Display SCK  -> P13 (Hardware-SPI, fix)   Display SDA/MOSI -> P15 (fix)
#   Display A0/DC -> P12                      Display RESET    -> P16
#   Display CS   -> P8                        Display LED      -> 3V
#   Display VCC  -> 3V (am eigenen Modul pruefen, manche wollen 5V)
#   Display GND  -> GND
# --------------------------------------------------------------------------

from microbit import pin8, pin12, pin16, sleep
from st7735 import ST7735, color565, BLACK, WHITE, RED, GREEN, BLUE

display = ST7735(cs=pin8, dc=pin12, rst=pin16)

# ----- Demo 1: ganzen Bildschirm der Reihe nach einfaerben -----
for farbe in (RED, GREEN, BLUE, WHITE, BLACK):
    display.fill(farbe)
    sleep(800)

# ----- Demo 2: ein paar Rechtecke, eigene Farbe per color565(r, g, b) -----
orange = color565(255, 140, 0)
display.fill_rect(10, 10, 40, 40, RED)
display.fill_rect(60, 10, 40, 40, GREEN)
display.fill_rect(10, 60, 90, 20, orange)

while True:
    sleep(1000)
