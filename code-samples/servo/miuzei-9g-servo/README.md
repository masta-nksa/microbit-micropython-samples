# Miuzei Micro Servo 9g (Metallgetriebe)

Kleiner Hobby-Servo, SG90-kompatibel, aber mit Metallzahnraedern (robuster).
Stellbereich ca. 0..180 Grad. 3-poliges Kabel:

| Ader | Bedeutung | an den micro:bit |
|------|-----------|------------------|
| orange oder gelb | Signal (PWM) | `P0` |
| rot | Plus (+) | `3V` bzw. externes Batteriefach |
| braun oder schwarz | Minus (-) / GND | `GND` |

## Ansteuerung

Ein Servo wird ueber ein **PWM-Signal** gestellt: alle 20 ms ein Impuls,
dessen **Laenge** den Winkel bestimmt.

| Impulslaenge | Winkel |
|-------------|--------|
| ca. 0.5 ms | 0 Grad |
| ca. 1.5 ms | 90 Grad |
| ca. 2.4 ms | 180 Grad |

In MicroPython:

```python
pin0.set_analog_period(20)                 # 20 ms Periode = 50 Hz
pin0.write_analog(duty)                     # duty 0..1023 = 0..20 ms
```

`write_analog(26)` ergibt ca. 0.5 ms, `write_analog(123)` ca. 2.4 ms - dazwischen
linear. Zittert der Servo an den Endlagen, den Bereich etwas verkleinern
(z. B. 34..115).

## Stromversorgung - wichtig

- Ein **einzelner unbelasteter** 9g-Servo laeuft meist direkt am `3V`-Pin.
- Unter Last, bei mehreren Servos oder wenn der micro:bit **neu startet /
  der Servo zittert**: **externes Batteriefach** verwenden
  (3x 1.5 V = 4.5 V reicht; 4x 1.5 V = 6 V ist das Maximum laut Servo).

### Anschluss mit externer Batteriebox (3x 1.5 V = 4.5 V)

Die Batteriebox hat zwei Kabel: **rot = Plus (+)**, **schwarz = Minus (-)**.
Der Servo bekommt seinen Strom NUR aus der Box, mit dem micro:bit wird nur
das Signal und die gemeinsame Masse geteilt.

```
  Batteriebox 4.5V         Servo                micro:bit
  ----------------         -----                ---------
  rot  (+)  --------------> rot   (+)
  schwarz (-) --+--------->  braun (-)
                |
                +---------------------------->  GND      (gemeinsame Masse!)
                           orange -----------> P0        (Signal)

  3V am micro:bit bleibt frei.
```

Schritt fuer Schritt:

1. **rot** der Box  ->  **rot** des Servos
2. **schwarz** der Box  ->  **braun/schwarz** des Servos
3. **schwarz** der Box (oder braun des Servos)  ->  **GND** am micro:bit
   (diese Masse-Bruecke ist zwingend, sonst "sieht" der Servo das Signal nicht)
4. **orange/gelb** des Servos  ->  **P0** am micro:bit
5. Der `3V`-Pin des micro:bit bleibt frei - **niemals** `+` der Box an `3V`
   oder an einen Pin legen.

Auf dem Steckbrett: `+` der Box auf die rote Schiene, `-` auf die blaue
Schiene, micro:bit-`GND` ebenfalls an die blaue Schiene, Servo `+/-` an die
Schienen, Servo-Signal an `P0`.

> Box erst einschalten, wenn alles gesteckt ist. Zum Programmieren muss der
> micro:bit weiterhin per USB am Rechner haengen - das ist kein Problem,
> solange `+` der Box nirgends mit dem micro:bit verbunden ist.

## Servo an einer Mechanik mit Endanschlag

Treibt der Servo etwas an, das **nicht** volle 180 Grad Weg hat (Bolzen,
Klappe, Schieber), darf er nur in einem begrenzten Fenster fahren. Faehrt er
gegen den Anschlag, geht er in den **Stall**: hohe Stromaufnahme, Brummen,
heisse Zahnraeder, Brownout/Reset am micro:bit.

Regeln:

- **Zwei kalibrierte Endpunkte** (`PULS_A`, `PULS_B` in Mikrosekunden), der
  Servo faehrt nur dazwischen. `set_puls()` klemmt jeden Wert hart auf dieses
  Fenster.
- Jeweils **~30 µs Sicherheitsmarge** vom echten Anschlag weg (Servo-Toleranz,
  Getriebespiel, Temperaturdrift).
- Endpunkte **messen, nicht rechnen**: mit
  [endlagen-kalibrieren](endlagen-kalibrieren/) in feinen Schritten anfahren
  und den µs-Wert ablesen. Rechnerisch nur zur Kontrolle: ca. **11 µs pro
  Grad** Servowinkel, mal Getriebe-Uebersetzung `Z_servo / Z_rad`.
- Beim Einschalten in die **Mitte des Fensters** fahren, nicht auf 1500 µs -
  das koennte schon am Anschlag liegen.
- Sanft fahren: in kleinen µs-Stufen mit kurzer Pause, nicht springen.
- Optional nach dem Fahren `pin0.write_analog(0)` -> Servo stromlos, kein
  Brummen. Nur, wenn die Mechanik die Lage von selbst haelt.

Ablauf: erst [endlagen-kalibrieren](endlagen-kalibrieren/), dann die zwei Werte
in [bolzen-schalten](bolzen-schalten/) eintragen.

## Samples (Lernreihenfolge)

1. [a-b-drehen/](a-b-drehen/) - Knopf A/B drehen den Servo, A+B zurueck auf 0
2. [zwei-stellungen/](zwei-stellungen/) - Knopf A = 0 Grad, Knopf B = 180 Grad
3. [sweep/](sweep/) - faehrt langsam hin und her, Knopf A haelt an
4. [winkel-mit-encoder/](winkel-mit-encoder/) - Drehknopf (EC11) stellt den Winkel
5. [endlagen-kalibrieren/](endlagen-kalibrieren/) - sichere Endpunkte einer eigenen Mechanik finden
6. [bolzen-schalten/](bolzen-schalten/) - zwischen zwei kalibrierten Endpunkten fahren (Endanschlag)

Masse fuers CAD (spaeter): [../../../hardware/servo/miuzei-9g-servo/](../../../hardware/servo/miuzei-9g-servo/)
