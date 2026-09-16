# Loeten: Pinheader & Kabel an Module

Kurzanleitung fuers Anloeten von Pinheadern und Kabeln an die Module in
diesem Projekt (TM1637, ST7735-Display, HC-SR04, EC11-Encoder,
DS425-Taster, WS2812B-Strip). Gilt fuer eine **stufenlos regelbare
Loetstation bis 400 °C**.

> **Sicherheit:** Loetkolben nur nach Einweisung und unter Aufsicht
> benutzen. Immer auf der Ablage/im Staender abstellen, nie ablegen. Spitze
> wird >200 °C heiss - nicht beruehren, auch kurz nach dem Ausschalten
> nicht (kuehlt langsam ab). In einem beluefteten Raum arbeiten - Loetrauch
> (Kolophonium aus dem Flussmittel) nicht einatmen, Kopf zur Seite halten
> statt direkt ueber die Loetstelle zu beugen. Nach dem Loeten Haende
> waschen, vor allem bei bleihaltigem Lot. Kein Lot/Flussmittel essen oder
> in die Naehe von Lebensmitteln bringen. Loetkolben nach Gebrauch immer
> ausschalten/ausstecken.

## Temperatur-Richtwerte

Am eigenen Lot ablesen, welcher Typ es ist (Aufdruck auf der Rolle) - die
beiden Typen brauchen unterschiedliche Temperaturen:

| Lot-Typ | Schmelzpunkt | Spitzentemperatur |
|---|---|---|
| **Bleihaltig** (z. B. Sn63Pb37) | ca. 183 °C | **300-320 °C** |
| **Bleifrei** (z. B. SAC305, Sn99Cu1) | ca. 217-227 °C | **330-360 °C** |

Je nach Loetstelle zusaetzlich anpassen:

| Loetstelle | Temperatur | Bemerkung |
|---|---|---|
| Pinheader auf duennem Modul-PCB (TM1637, ST7735-Display) | unterer Bereich der Tabelle oben | duenne Platinen/Pads loesen sich leichter ab - nicht laenger als 2-3 s pro Pin |
| Kabel direkt an ein Pad/Loetauge | Mitte der Tabelle | Kabel vor dem Anloeten selbst verzinnen (siehe unten) |
| Dicke Leiterbahn, Massefolie, dicker Draht (z. B. Servo-/Strip-Anschluss) | oberer Bereich der Tabelle, im Zweifel +10-15 °C | dicke Kupferflaechen leiten die Waerme weg, brauchen kurzzeitig mehr Energie |

**Grundregel: so kalt wie moeglich, so heiss wie noetig.** Nicht einfach auf
400 °C stellen "damit es schneller geht" - hoehere Temperatur heisst mehr
Oxidation an der Spitze, schnellerer Spitzenverschleiss und ein hoeheres
Risiko, Bauteile oder Leiterbahnen zu beschaedigen. Wenn eine Loetstelle bei
korrekter Temperatur laenger als ca. 3-4 Sekunden braucht, ist meist die
Spitze verschmutzt/oxidiert oder zu klein fuer die Waermemenge - nicht die
Temperatur weiter hochdrehen, sondern Spitze reinigen (siehe unten).

## Technik in Kuerze

1. **Spitze verzinnen**, bevor es losgeht: kurz auf den feuchten Schwamm
   oder ins Messing-Reinigungswolle-Pad tippen, dann einen kleinen
   Lottropfen auf die Spitze geben - sie soll glaenzend-silbern sein, nicht
   grau/oxidiert.
2. Loetkolben **an Pad UND Kabel/Pin gleichzeitig** halten (nicht nur am
   Draht), ca. 1-2 Sekunden vorwaermen.
3. **Lot an die Verbindungsstelle** fuehren (nicht an die Kolbenspitze) -
   das Lot soll durch die Waerme von Pad und Pin schmelzen, nicht durch die
   Spitze direkt.
4. Genug Lot fuer eine kleine, glatte Wulst, dann zuerst das **Lot**, dann
   den **Kolben** wegziehen.
5. **Nicht bewegen**, bis die Stelle abgekuehlt ist (ca. 2-3 Sekunden) -
   sonst entsteht eine "kalte" Loetstelle.

### Kabel vorverzinnen

Bei freien Kabelenden (nicht direkt an einem Pad): Ader abisolieren, kurz
verdrillen, Loetkolben an die Ader halten und einen duennen Lotfilm
aufziehen ("verzinnen"), **bevor** sie an das Pad geloetet wird. Das macht
die eigentliche Verbindung schneller und zuverlaessiger.

## Gute vs. schlechte Loetstelle

| Merkmal | Gut | Schlecht |
|---|---|---|
| Oberflaeche | glatt, glaenzend | matt, koernig ("kalte Loetstelle") |
| Form | kleiner, konkaver Huegel (wie ein Vulkan) | Kugel/Klumpen oder zu wenig Lot |
| Pin sichtbar | Kontur des Pins/Drahts noch leicht erkennbar | Pin komplett im Lot versteckt |
| Nachbarpins | sauber getrennt | Lotbruecke zum Nachbarpin |

Bei engen Pinreihen (4-polige Module wie TM1637/LCD, Pitch oft 2.54 mm oder
enger) **immer auf Bruecken zum Nachbarpin pruefen** - im Zweifel mit einer
Lupe oder dem Handy-Foto vergroessert nachschauen. Eine Bruecke laesst sich
mit Entloetlitze oder durch nochmaliges, vorsichtiges Erhitzen und
Abstreifen entfernen.

## Spitzenpflege

- Vor und nach dem Loeten auf dem **feuchten Schwamm oder Messingwolle**
  abstreifen - Messingwolle ist schonender fuer die Spitze als ein nasser
  Schwamm (kein Temperaturschock).
- Spitze **nie trocken** oder laenger unbenutzt ohne Lotschicht liegen
  lassen - vor dem Ausschalten/Ablegen einen kleinen Lottropfen auf der
  Spitze belassen, das schuetzt vor Oxidation.
- Grau-schwarze, "verbrannte" Spitze loetet schlecht (Waerme kommt nicht
  mehr an) - erst reinigen/neu verzinnen, bevor die Temperatur erhoeht wird.
