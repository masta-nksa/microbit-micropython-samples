# Setup: MicroPython auf den micro:bit V2.2 uebertragen

Fuer alle Aufgaben in diesem Repo wird der Online-Editor verwendet:

**<https://python.microbit.org/v/beta>**

## Ablauf

1. Editor im Browser oeffnen (Chrome oder Edge - WebUSB noetig).
2. Den Code der jeweiligen Aufgabe (`main.py`) in den Editor kopieren.
   Bei mehreren Dateien: links im Projektbaum weitere Dateien anlegen.
3. micro:bit mit dem USB-Kabel an den Computer anschliessen.
4. Unten auf **Connect** klicken und den micro:bit im Dialog auswaehlen.
5. **Send to micro:bit** klicken. Der Code laeuft danach sofort.
6. **Serielle Ausgabe / REPL:** unten auf **Open Serial** klicken, um
   `print(...)`-Ausgaben zu sehen.

## Alternative: .hex-Datei

Im Editor **Save** -> es wird eine `.hex`-Datei heruntergeladen.
Diese per Drag & Drop auf das Laufwerk `MICROBIT` kopieren.

## Haeufige Probleme

| Problem | Loesung |
|---------|---------|
| micro:bit erscheint nicht bei **Connect** | Anderes USB-Kabel (Datenkabel, nicht nur Ladekabel), anderer USB-Port |
| WebUSB nicht verfuegbar | Chrome oder Edge verwenden, kein Firefox/Safari |
| Code laeuft nicht neu | micro:bit kurz vom USB trennen oder Reset-Taste auf der Rueckseite |
| Kein Ton | micro:bit V2 hat einen eingebauten Lautsprecher; bei V1 externen Lautsprecher an P0 + GND |

## Pin-Uebersicht (Randstecker)

- **P0, P1, P2**: grosse Pads, analog + digital, ideal fuer Krokoklemmen
- **3V**: 3 Volt Ausgang
- **GND**: Masse
- P0 wird in Aufgabe 1 als digitaler Eingang mit internem Pull-up genutzt.
