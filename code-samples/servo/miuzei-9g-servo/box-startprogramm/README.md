# box-startprogramm

Bauteil: [Miuzei Micro Servo 9g](../README.md) · Kategorie: servo

Startprogramm fuer die **eigene Mysterybox**: Knopf **A** oeffnet die Box,
Knopf **B** schliesst sie, **A + B** ist der Notfall (faehrt in die Mitte).
Das Programm laeuft so, sobald zwei Werte eingetragen sind. Danach machst du
es mit den **Ideen** weiter unten Schritt fuer Schritt zu deinem eigenen
Schliessmechanismus - und lernst dabei die Sensoren des micro:bit kennen.

**Stand:** aus [bolzen-schalten](../bolzen-schalten/) abgeleitet, Ablauf am
Rechner geprueft, noch nicht auf echter Hardware getestet.

## Material

| Anzahl | Bauteil |
|-------:|---------|
| 1 | micro:bit V2.2 |
| 1 | Miuzei Micro Servo 9g (Metallgetriebe), in der Mechanik der Box |
| 1 | Batteriefach 3x 1.5 V (4.5 V) |
| 3 | Jumperkabel / Krokoklemmen |

## Verkabelung

Wie bei [bolzen-schalten](../bolzen-schalten/README.md#verkabelung), mit
externem Batteriefach:

```
  Batteriefach 3xAA          Servo                 micro:bit
  ----------------           -----                 ---------
  rot  (+)  ---------------> rot   (+)
  schwarz (-) --+----------> braun (-)
                |
                +--------------------------------> GND     (gemeinsame Masse!)
                       orange/gelb ---------------> P0      (Signal)

  3V am micro:bit bleibt frei.
```

Details: [Bauteil-README](../README.md#stromversorgung---wichtig).

## Foto der Verkabelung

Nach dem Test ein Foto in [`wiring/`](wiring/) ablegen und hier einbinden:

<!-- ![Verkabelung](wiring/foto.jpg) -->

## Einstellen (Pflicht vor dem ersten Lauf)

Oben im Code stehen zwei Werte, beide sind am Anfang leer (`None`). Solange
sie fehlen, faehrt der Servo **nie** - die Matrix zeigt nur ein `?`.

1. Mit [endlagen-kalibrieren](../endlagen-kalibrieren/) beide Endlagen deiner
   Box messen (Box ganz offen, Box ganz zu).
2. Beide Werte um etwa 15 bis 30 us **Richtung Mitte** zuruecknehmen.
3. Eintragen:

```python
PULS_AUF = 950     # Box offen   (dein Wert)
PULS_ZU = 1500     # Box zu      (dein Wert)
```

4. `START_ZUSTAND` auf `"auf"`, `"zu"` oder `"unbekannt"` setzen - je nachdem,
   wie die Box beim Einschalten steht.

Wirken A und B verkehrt herum: die beiden Werte tauschen (und
`START_ZUSTAND` anpassen).

## Wie der Code funktioniert

- `box_auf()` und `box_zu()` fahren den Servo sanft in kleinen Schritten von
  einer Endlage in die andere und schalten ihn danach stromlos (die Reibung
  haelt die Lage). Sie geben `True` zurueck, wenn sie gefahren sind, sonst
  `False`.
- Ein zweiter Befehl in **dieselbe** Richtung tut nichts. Sonst wuerde der
  Servo gegen den Anschlag druecken.
- `box_zustand()` sagt dir, ob die Box gerade `"auf"`, `"zu"` oder
  `"unbekannt"` ist.
- `rueckmeldung(ok)` zeigt einen Haken (gefahren) oder ein Kreuz (nichts
  passiert). Fehlen die Endlagen, zeigt sie ein `?`.
- Der erste Befehl nach dem Einschalten fuehrt den Servo kurz in die Mitte
  des Fensters. Das ist Absicht (sichere Ausgangslage).
- In der Hauptschleife steht die Zeile `>>> IDEEN HIER EINFUEGEN <<<`. Dort
  kommen die Ideen unten hinein.

## Programm

Ganzer Code, Quelle [`main.py`](main.py) (hier automatisch eingefuegt):

<!-- CODE:START -->
```python
# Sample: box-startprogramm  (Miuzei Micro Servo 9g, Metallgetriebe)
# Board:   BBC micro:bit V2.2
# Sprache: MicroPython
#
# Ziel: Startprogramm fuer die eigene Mysterybox. Knopf A oeffnet die Box,
#       Knopf B schliesst sie, A + B zusammen ist der Notfall (faehrt in die
#       Mitte). Danach kann man mit kleinen Ideen (siehe README) die Sensoren
#       des micro:bit einbauen.
#
#       Das Programm faehrt den Servo erst, wenn unter "1) Endlagen" beide
#       Werte eingetragen sind. Vorher zeigt die Matrix nur ein "?".
#
# --------------------------------------------------------------------------
# Verkabelung (wie alle Servo-Samples)
#   Servo orange/gelb (Signal)  ->  P0
#   Servo rot         (+)        ->  Batteriefach 3xAA (+)
#   Servo braun/schwarz (-)      ->  Batteriefach (-)  UND  micro:bit GND
# --------------------------------------------------------------------------

from microbit import *
import music        # nur fuer Ideen mit Ton - immer mit pin=None benutzen!

# ===== 1) Endlagen (Mikrosekunden) - mit "endlagen-kalibrieren" messen ====
PULS_AUF = None      # Box offen   (Beispiel: 950)
PULS_ZU = None       # Box zu      (Beispiel: 1500)
# Brummt der Servo an einer Endlage: den Wert 15-30 us Richtung Mitte ruecken.

# ===== 2) Startzustand: wie steht die Box beim Einschalten? ===============
#   "auf", "zu" oder "unbekannt" (dann darf der erste Befehl in beide
#   Richtungen fahren)
START_ZUSTAND = "unbekannt"

# ===== 3) Fahr-Verhalten ==================================================
SCHRITT = 8          # us pro Rampenschritt (kleiner = sanfter)
PAUSE = 15           # ms zwischen den Rampenschritten
# ========================================================================

pin0.set_analog_period(20)          # 20 ms = 50 Hz

_zustand = START_ZUSTAND
_puls = None                        # unbekannt, bis der Servo das erste Mal faehrt


def bereit():
    """True, sobald beide Endlagen eingetragen sind."""
    return PULS_AUF is not None and PULS_ZU is not None


def _schreibe(u):
    pin0.write_analog(int(u / 20000 * 1023))


def _fahre(ziel):
    global _puls
    lo = min(PULS_AUF, PULS_ZU)
    hi = max(PULS_AUF, PULS_ZU)
    ziel = max(lo, min(hi, ziel))           # nie ausserhalb des Fensters
    if _puls is None:
        _puls = (PULS_AUF + PULS_ZU) // 2   # erste Fahrt: sichere Mitte annehmen
    d = SCHRITT if ziel > _puls else -SCHRITT
    while abs(_puls - ziel) > SCHRITT:
        _puls += d
        _schreibe(_puls)
        sleep(PAUSE)
    _puls = ziel
    _schreibe(_puls)
    sleep(250)                              # ankommen lassen
    pin0.write_analog(0)                    # Servo stromlos -> Reibung haelt die Lage


def box_auf():
    """Box oeffnen. Gibt True zurueck, wenn sie gefahren ist."""
    global _zustand
    if not bereit() or _zustand == "auf":
        return False                        # schuetzt den Servo vor dem Anschlag
    _fahre(PULS_AUF)
    _zustand = "auf"
    return True


def box_zu():
    """Box schliessen. Gibt True zurueck, wenn sie gefahren ist."""
    global _zustand
    if not bereit() or _zustand == "zu":
        return False
    _fahre(PULS_ZU)
    _zustand = "zu"
    return True


def box_zustand():
    """Gibt 'auf', 'zu' oder 'unbekannt' zurueck."""
    return _zustand


def rueckmeldung(ok):
    """Haken (gefahren) oder Kreuz (nichts passiert) auf der Matrix."""
    if not bereit():
        display.show("?")                   # Endlagen fehlen -> erst messen
    else:
        display.show(Image.YES if ok else Image.NO)
    sleep(400)
    display.clear()


# ===== Hauptschleife ======================================================
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # Notfall: langsam in die Mitte, Zustand zuruecksetzen
        if bereit():
            _fahre((PULS_AUF + PULS_ZU) // 2)
            _zustand = "unbekannt"
        display.show("?")
        sleep(500)
        display.clear()

    elif button_a.was_pressed():
        rueckmeldung(box_auf())

    elif button_b.was_pressed():
        rueckmeldung(box_zu())

    # >>> IDEEN HIER EINFUEGEN (siehe README) <<<

    sleep(20)
```
<!-- CODE:END -->

## Auf den micro:bit uebertragen

<https://python.microbit.org/v/3> -> Code einfuegen -> **Connect** -> **Send to micro:bit**.
Details: [../../../../docs/setup.md](../../../../docs/setup.md).

## Erwartetes Verhalten

- Ohne eingetragene Werte: A oder B zeigen ein `?`, der Servo bleibt still
- Mit Werten: A oeffnet die Box (Haken), B schliesst sie (Haken)
- A zweimal hintereinander: beim zweiten Mal ein Kreuz, nichts bewegt sich
- A + B gleichzeitig: Servo faehrt langsam in die Mitte, Matrix zeigt `?`

## Ideen zum Ausbauen

**Immer nur eine Idee auf einmal einbauen und testen.** Die Codestuecke kommen
an die Stelle `>>> IDEEN HIER EINFUEGEN <<<` in der Hauptschleife (mit
**4 Leerzeichen** eingerueckt, wie die Zeilen darueber), ausser es steht
etwas anderes dabei.

| Nr | Idee | Sensor | Schwierigkeit |
|---:|------|--------|---------------|
| 1 | Ton beim Oeffnen | Lautsprecher | sehr leicht |
| 2 | Schuetteln schliesst die Box | Beschleunigungssensor | leicht |
| 3 | Kippen oeffnet und schliesst | Beschleunigungssensor | leicht |
| 4 | Logo als zweite Sicherung | Touch-Logo | leicht |
| 5 | Klatschen oeffnet | Mikrofon | mittel |
| 6 | Dunkel schliesst die Box | Lichtsensor | mittel |

### Idee 1: Ton beim Oeffnen

Aendere in der Funktion `rueckmeldung(ok)` die Zeile mit dem Haken so, dass
bei `ok` auch ein Ton kommt:

```python
    else:
        display.show(Image.YES if ok else Image.NO)
        if ok:
            music.pitch(880, 150, pin=None)
```

> **Wichtig: immer `pin=None`.** Ohne diesen Zusatz gibt der micro:bit den Ton
> auch an **P0** aus - dort haengt der Servo, er wuerde zucken.

### Idee 2: Schuetteln schliesst die Box

```python
    if accelerometer.was_gesture("shake"):
        rueckmeldung(box_zu())
```

### Idee 3: Kippen oeffnet und schliesst

```python
    if accelerometer.was_gesture("left"):
        rueckmeldung(box_auf())
    if accelerometer.was_gesture("right"):
        rueckmeldung(box_zu())
```

Kippt es in die falsche Richtung, `"left"` und `"right"` tauschen. Andere
Gesten: `"up"`, `"down"`, `"face up"`, `"face down"`.
Die Neigung als Zahl: [wasserwaage](../../../onboard/accelerometer/wasserwaage/).

### Idee 4: Logo als zweite Sicherung

Die Box oeffnet nur, wenn du **A drueckst und gleichzeitig das Logo beruehrst**.
Ersetze in der Hauptschleife die Zeile `elif button_a.was_pressed():` durch:

```python
    elif button_a.was_pressed() and pin_logo.is_touched():
```

Mehr zum Logo: [logo-schalter](../../../onboard/touch-logo/logo-schalter/).

### Idee 5: Klatschen oeffnet

```python
    if microphone.sound_level() > 150 and box_zustand() == "zu":
        rueckmeldung(box_auf())
        sleep(1000)
```

Die Schwelle `150` musst du an deinen Raum anpassen: mit
[lautstaerke-balken](../../../onboard/microphone/lautstaerke-balken/) siehst du,
wie laut ein Klatschen ist. Die Pause `sleep(1000)` verhindert, dass das
Servo-Geraeusch selbst wieder als Klatschen zaehlt.

### Idee 6: Dunkel schliesst die Box

```python
    if display.read_light_level() < 20 and box_zustand() == "auf":
        rueckmeldung(box_zu())
```

Die Schwelle `20` anpassen. Mehr zum Lichtsensor:
[nachtlicht](../../../onboard/light-level/nachtlicht/).

### Und dann?

- Zwei Ideen kombinieren, z. B. **Logo halten und schuetteln**.
- Eine **Folge** von Neigungen als Code merken. Der Weg dorthin steht im
  [Workflow](../../../../docs/workflow.md), Station 11.
- Eine Zahl auf der [4-Digit-Anzeige](../../output/tm1637-4digit/) als Code
  eingeben (Workflow, Station 10).
