---
title: Theorie
---

# Theorie: wie die Bauteile "sprechen"

Kurze, einfach gehaltene Erklaerungen, **wie** die externen Bauteile mit dem
micro:bit kommunizieren - fuer alle, die mehr wissen wollen als "so wird's
angeschlossen, dann laeuft's". Zum Nachschlagen gedacht, **keine
Voraussetzung** zum Loslegen: jedes Sample funktioniert auch ohne diese Seite.
Jeder Abschnitt unten laesst sich einzeln aufklappen.

## Warum ueberhaupt verschiedene Protokolle? {#warum-protokolle}

Ein Bauteil mit vielen Funktionen (z. B. 4 Ziffern, 100 LEDs) muesste
eigentlich sehr viele Kabel haben - fuer jede Ziffer/LED eine eigene Leitung.
Das waere unpraktisch. Darum schicken die meisten externen Bauteile ihre
Daten stattdessen **seriell**: alle Infos nacheinander ueber ein oder zwei
Kabel, Bit fuer Bit. Dabei gibt es zwei Grundvarianten:

- **Mit eigener Taktleitung (`CLK`):** Ein zweites Kabel tickt im Rhythmus
  und sagt dem Empfaenger "genau **jetzt** ist ein neues Bit auf der
  Datenleitung gueltig, lies es ab". Sender und Empfaenger muessen sich nicht
  auf eine Zeit einigen - der Takt gibt sie vor. Beispiel: **TM1637**, **SPI**
  (beim ST7735-Display).
- **Ohne Taktleitung, nur ueber Timing:** Es gibt nur die Datenleitung. Ob ein
  Bit eine 0 oder eine 1 ist, erkennt der Empfaenger daran, **wie lange** die
  Leitung high bzw. low bleibt - beide Seiten muessen exakt dasselbe Timing
  kennen. Ein Kabel weniger, dafuer aber empfindlicher gegen Verzoegerungen
  (z. B. durch die Leitungsqualitaet). Beispiel: **WS2812B**.

Die folgenden Abschnitte zeigen, wie das konkret bei den einzelnen Bauteilen
aussieht.

<details markdown="1">
<summary><strong>WS2812B LED-Strip</strong> - ein Draht fuer beliebig viele LEDs</summary>

## WS2812B LED-Strip: ein Draht fuer beliebig viele LEDs {#ws2812b}

Bauteil-README: [code-samples/output/ws2812b-led-strip/](../code-samples/output/ws2812b-led-strip/)

Jede LED auf dem Strip hat ihren eigenen kleinen Chip eingebaut und ist wie
eine Perle an einer Kette mit der naechsten verbunden (`DO` der einen an
`DIN` der naechsten). Alle LEDs haengen an **derselben einen** Datenleitung -
trotzdem kann jede LED eine andere Farbe zeigen. Das funktioniert wie eine
Art Flüsterpost mit Paketen:

1. Der micro:bit schickt **alle Farbwerte fuer den ganzen Strip hintereinander**
   auf die eine Datenleitung - 24 Bit (3 Byte: Gruen, Rot, Blau) pro LED, in
   der Reihenfolge der LEDs.
2. Die **erste** LED der Kette "hoert mit", nimmt sich **ihre eigenen** ersten
   24 Bit heraus (= ihre Farbe) und reicht **den Rest des Datenstroms**
   unveraendert an `DO` weiter zur naechsten LED.
3. Die **zweite** LED macht dasselbe: sich die naechsten 24 Bit nehmen, den
   Rest weiterreichen. Und so weiter bis zur letzten LED.

Es gibt dabei **keine** Taktleitung. Ob ein Bit 0 oder 1 ist, erkennt der Chip
allein daran, wie lange die Datenleitung fuer dieses Bit high bleibt (eine 0
ist ein kurzer High-Puls, eine 1 ein langer - beides im Bereich von
Nanosekunden bis wenigen Mikrosekunden). Das Modul `neopixel` im micro:bit
erzeugt dieses Timing exakt - im eigenen Code muss man sich darum nicht
kuemmern, nur `np.show()` aufrufen.

</details>

<details markdown="1">
<summary><strong>TM1637</strong> - CLK + DATA, ein getaktetes 2-Draht-Protokoll</summary>

## TM1637: CLK + DATA - ein getaktetes 2-Draht-Protokoll {#tm1637}

Bauteil-README: [code-samples/output/tm1637-4digit/](../code-samples/output/tm1637-4digit/) (dort auch die genaue Start/Stop-Bedingung und Byte-Adressierung)

Anders als der WS2812B-Strip hat das TM1637-Modul eine **eigene Taktleitung**
(`CLK`). Der micro:bit gibt auf `CLK` den Rhythmus vor; auf jeden Taktschlag
hin liest der Chip das aktuelle Bit von `DIO` ab. Weil der Takt sagt, wann
gelesen werden soll, muss das Timing der Datenleitung selbst nicht exakt
sein - das macht dieses Protokoll toleranter und einfacher zu "von Hand"
programmieren (bit-gebanged) als das timing-kritische WS2812B-Protokoll.
`DIO` wird dabei in **beide Richtungen** genutzt: der micro:bit sendet damit
Befehle und Ziffern, der Chip meldet darauf (bei diesem Modul ungenutzt) auch
eine Bestaetigung zurueck.

</details>

<details markdown="1">
<summary><strong>EC11-Drehgeber</strong> - zwei versetzte Signale zeigen die Richtung</summary>

## EC11-Drehgeber: zwei versetzte Signale zeigen die Richtung {#ec11}

Bauteil-README: [code-samples/input/ec11-encoder/](../code-samples/input/ec11-encoder/) (dort auch der genaue Code zum Auslesen)

Der Drehgeber hat **keine** Datenleitung im obigen Sinn, sondern zwei
einfache Ein/Aus-Signale (`CLK` und `DT`), die beim Drehen **beide** zwischen
0 und 1 wechseln - aber leicht **zeitversetzt** zueinander (um 90 Grad
"phasenverschoben", daher der Fachbegriff **Quadratur-Encoder**). Diese
Verzoegerung zwischen den beiden Signalen verraet die Drehrichtung:

- Dreht man **im Uhrzeigersinn**, kippt `CLK` **vor** `DT`.
- Dreht man **gegen den Uhrzeigersinn**, kippt `DT` **vor** `CLK`.

Der Code muss darum nur pruefen, *welches der beiden Signale zuerst kippt*,
wenn eine Raste erreicht wird - daraus ergibt sich hoch- oder runterzaehlen.

</details>

<details markdown="1">
<summary><strong>HC-SR04</strong> - Abstand per Echo-Laufzeit</summary>

## HC-SR04: Abstand per Echo-Laufzeit {#hc-sr04}

Bauteil-README: [code-samples/input/hc-sr04-abstandssensor/](../code-samples/input/hc-sr04-abstandssensor/) (dort auch die genaue Formel und Spannungsteiler-Variante)

Kein Bit-Protokoll, sondern eine **Zeitmessung**: der micro:bit schickt einen
kurzen Impuls auf `Trig`, der Sensor sendet daraufhin einen fuer Menschen
unhoerbaren Ultraschall-Ton aus und setzt `Echo` auf High. Trifft der
Schall auf ein Hindernis, kommt ein Echo zurueck und der Sensor setzt `Echo`
wieder auf Low. Die **Dauer**, die `Echo` high war, ist also die Zeit, die
der Schall fuer **hin und zurueck** gebraucht hat. Da die
Schallgeschwindigkeit bekannt ist (~343 m/s bei Zimmertemperatur), laesst
sich daraus direkt der Abstand berechnen - genau das macht `dauer_us / 58.0`
in der README.

</details>

<details markdown="1">
<summary><strong>Servo</strong> - PWM, die Pulslaenge bestimmt den Winkel</summary>

## Servo: PWM - die Pulslaenge bestimmt den Winkel {#servo}

Bauteil-README: [code-samples/servo/miuzei-9g-servo/](../code-samples/servo/miuzei-9g-servo/) (dort auch Kalibrierung und sichere Stromversorgung)

Auch hier keine Bits, sondern ein **PWM-Signal** (Pulsweitenmodulation): alle
20 Millisekunden schickt der micro:bit einen kurzen High-Impuls auf die
Signalleitung. Nicht der Pegel zaehlt, sondern **wie lange** dieser einzelne
Impuls dauert - ca. 0.5 ms bedeutet fuer den Servo "fahre auf 0 Grad", ca.
2.4 ms "fahre auf 180 Grad", dazwischen linear. Der Servo hat intern eine
eigene kleine Elektronik, die diese Pulslaenge staendig misst und den Motor
so lange nachregelt, bis die Achse den passenden Winkel erreicht hat.

</details>

<details markdown="1">
<summary><strong>SPI</strong> (ST7735-Display) - getaktet wie TM1637, aber schneller und mit Adressierung</summary>

## SPI (ST7735-Display): getaktet wie TM1637, aber schneller und mit Adressierung {#spi}

Bauteil-README: [code-samples/output/st7735-tft-1-8-spi/](../code-samples/output/st7735-tft-1-8-spi/)

SPI ist wie CLK+DATA (siehe TM1637 oben) ein **getaktetes** Protokoll - auch
hier gibt eine Taktleitung (`SCK`) den Rhythmus vor, zu dem die Datenleitung
(`SDA`/`MOSI`) gelesen wird. Zwei Unterschiede machen SPI fuer ein Display
mit vielen Pixeln praktikabler:

- SPI ist als **Hardware-Funktion** im micro:bit eingebaut (feste Pins `13`/`15`)
  und dadurch deutlich schneller als das von Hand getaktete (bit-gebangte)
  TM1637-Protokoll.
- Eine eigene Leitung `CS` (Chip-Select) sagt dem Display "die naechsten Bits
  sind fuer **dich**" - so koennten grundsaetzlich mehrere SPI-Bauteile
  dieselben `SCK`/`SDA`-Leitungen teilen und trotzdem einzeln angesprochen
  werden (in diesem Repo aber nur mit einem Display genutzt).

Die zusaetzliche Leitung `A0`/`DC` sagt dem Display, ob die naechsten Bytes
ein **Befehl** (z. B. "Bildschirm loeschen") oder **Bilddaten** (Pixelfarben)
sind.

</details>
