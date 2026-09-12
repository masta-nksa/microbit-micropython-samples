# HC-SR04 Ultraschall-Abstandssensor

Misst den Abstand zu einem Hindernis per Ultraschall-Laufzeit: ein kurzer
Trigger-Impuls loest einen Schallstoss aus, der Sensor haelt `Echo` so lange
auf High, wie das Echo unterwegs war.

## Anschluesse am Modul

| Pin (Beschriftung, bei diesem konkreten Modul von oben nach unten) | Bedeutung |
|---|---|
| `Gnd` | Masse |
| `Echo` | Ausgang: High-Puls, Dauer = Laufzeit |
| `Trig` | Eingang: Trigger-Impuls ausloesen |
| `Vcc` | Plus |

Laut Datenblatt **5 V**. Die Reihenfolge kann bei anderen Modulen abweichen -
nach der Beschriftung anschliessen.

## Anschluss an den micro:bit - Standard (einfach und sicher, 3 V)

```
   micro:bit          HC-SR04
  +---------+        +---------+
  |      P1 |--------| Trig    |
  |      P2 |--------| Echo    |
  |      3V |--------| Vcc     |
  |     GND |--------| Gnd     |
  +---------+        +---------+
```

Der Sensor wird hier mit **3 V statt der spezifizierten 5 V** betrieben. Das
reduziert die zuverlaessige Reichweite auf ca. **20-150 cm** (fuer die
meisten Uebungen genug), macht die Verkabelung dafuer aber **sicher und
einfach**: Bei 3 V bleibt auch der `Echo`-Rueckgabepuls bei ca. 3 V - direkt
vertraeglich mit einem micro:bit-Pin (der max. ca. 3,6 V vertraegt). Kein
Spannungsteiler noetig.

## Mehr Reichweite: 5 V + Spannungsteiler (optional)

Voll spezifiziert braucht der HC-SR04 5 V (Reichweite laut Datenblatt bis
400 cm). Bei 5 V liefert `Echo` aber auch ~5-V-Pulse zurueck - das
**ueberschreitet die maximale Eingangsspannung eines micro:bit-Pins und kann
ihn beschaedigen**. Abhilfe: ein Spannungsteiler zwischen `Echo` und dem
micro:bit-Pin.

```
  Sensor Echo ---[ 1 kOhm ]---+---[ 2 kOhm ]--- GND
                              |
                          micro:bit Pin   (~3,3 V statt 5 V)
```

`Vcc` kommt dann von einer externen 5-V-Quelle (GND gemeinsam mit dem
micro:bit), `Trig` bleibt direkt am micro:bit - der Sensor erkennt den
3,3-V-Trigger auch im 5-V-Betrieb zuverlaessig.

## Messung in MicroPython

```python
import machine

dauer_us = machine.time_pulse_us(ECHO, 1, 30000)   # wartet auf den HIGH-Puls
abstand_cm = dauer_us / 58.0                        # Schallgeschwindigkeit
```

- `machine.time_pulse_us(pin, pegel, timeout_us)` misst die Dauer eines
  Pulses in Mikrosekunden - genau, was hier gebraucht wird (der micro:bit
  selbst kann per `sleep()` nur auf 1 ms genau warten).
- Ein **negativer Rueckgabewert** heisst Timeout: kein Echo (Hindernis zu
  nah - unter ~2 cm -, zu weit weg, oder schraeg/weich, sodass nichts
  reflektiert wird).
- Zwischen zwei Messungen mindestens **~60 ms** warten (Datenblatt), sonst
  kann ein spaetes Echo die naechste Messung stoeren.
- Der Trigger-Impuls muss laut Datenblatt mindestens 10 µs lang sein. Da
  `sleep()` nur Millisekunden kann, wird hier 1 ms (= 1000 µs) benutzt - das
  ist laenger als noetig, funktioniert aber zuverlaessig.

## Samples (Lernreihenfolge)

1. [abstand-messen/](abstand-messen/) - Abstand messen, als LED-Balken zeigen
2. [naeherungsalarm/](naeherungsalarm/) - piept schneller, je naeher ein Hindernis ist
3. [entfernungsanzeige-tm1637/](entfernungsanzeige-tm1637/) - Abstand in cm auf der [TM1637-Anzeige](../../output/tm1637-4digit/) darstellen

Masse fuers CAD (spaeter): [../../../hardware/input/hc-sr04-abstandssensor/](../../../hardware/input/hc-sr04-abstandssensor/)
