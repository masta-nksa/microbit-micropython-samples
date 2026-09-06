# DS425 Pushbutton (Momentary)

Einfacher taktiler Taster (Schliesser). Solange gedrueckt: Kontakt geschlossen,
sonst offen. 4 Beine, je zwei gegenueberliegende fest verbunden.

- Anschluss: ein Bein an `P0`, ein diagonales Bein an `GND`
- Kein externer Widerstand noetig - interner Pull-up per `pin0.set_pull(pin0.PULL_UP)`
- Masse fuers CAD: [../../../hardware/input/ds425-pushbutton/](../../../hardware/input/ds425-pushbutton/)

## Samples (Lernreihenfolge)

1. [ton-bei-druck/](ton-bei-druck/) - kurzer Ton + Herz beim Druecken
2. [ton-solange-gedrueckt/](ton-solange-gedrueckt/) - Dauerton, solange gehalten wird
