# tools/

Hilfsskripte fuer das Repo. Brauchen nur Python 3 (Standardbibliothek).

## build_readme.py

Fuegt den Inhalt jeder `main.py` in die daneben liegende `README.md` ein, damit
der Code in der README immer mit `main.py` uebereinstimmt.

In der README markieren die Zeilen

```
<!-- CODE:START -->
<!-- CODE:END -->
```

die Stelle, an der der Code stehen soll. Alles dazwischen wird beim Ausfuehren
durch einen ` ```python `-Block mit dem aktuellen `main.py`-Inhalt ersetzt.

Eine README kann **mehrere** Marker-Paare haben. Ein Paar mit Dateinamen nach
dem Doppelpunkt liest eine andere Datei aus demselben Ordner statt `main.py`
(z. B. eine mitgelieferte Bibliothek):

```
<!-- CODE:START:tm1637.py -->
<!-- CODE:END -->
```

```bash
python tools/build_readme.py            # READMEs aktualisieren
python tools/build_readme.py --check    # nur pruefen (Exit 1, wenn veraltet)
```

Einzige Quelle bleibt `main.py` - den Code nie direkt in der README aendern.
