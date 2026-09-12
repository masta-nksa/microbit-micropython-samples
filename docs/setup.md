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

## Zweite Datei hinzufuegen (z. B. eine mitgelieferte Bibliothek)

Manche Samples liefern neben `main.py` eine zweite Datei mit, z. B. eine
kleine Bibliothek wie `tm1637.py`. Beide muessen im selben Projekt landen:

1. Im Editor links im Dateibereich auf **das Plus-Symbol** bzw. **"Neue
   Datei"** klicken (Beschriftung kann je nach Editor-Version leicht
   abweichen).
2. Die Datei **exakt** so benennen, wie im Sample angegeben (z. B.
   `tm1637.py`) - der Dateiname wird zum Modulnamen fuer `import`.
3. Den Bibliothekscode aus der README hineinkopieren, speichern.
4. In `main.py` ganz normal importieren, z. B. `from tm1637 import TM1637`.
5. **Send to micro:bit** uebertraegt danach beide Dateien zusammen.

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
