# Touch-Logo (nur V2)

Das goldene micro:bit-Logo oben auf der Platine ist beim **V2** ein
kapazitiver Beruehrungssensor - ein "dritter Knopf", den man nicht druecken
muss, sondern nur antippt.

- Eingebaut, kein Aufbau noetig
- Nur micro:bit **V2** (beim V1 ist das Logo nur bedruckt)
- `pin_logo` - verfuegbar ueber `from microbit import *`

## Wichtige Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `pin_logo.is_touched()` | `True`, solange das Logo **jetzt** beruehrt wird |
| `pin_logo.set_touch_mode(pin_logo.CAPACITIVE)` | Beruehrungsmodus (V2-Standard, meist nicht noetig) |

Anders als `button_a` gibt es hier **kein** `was_pressed()` - die Flanke
(Wechsel "nicht beruehrt -> beruehrt") merkt man sich selbst.

## Samples (Lernreihenfolge)

1. [logo-schalter/](logo-schalter/) - Logo antippen schaltet ein Herz an und aus
