
# Bildqualitätsbewertung mit BRISQUE

Dieses Projekt bewertet die Bildqualität mithilfe der BRISQUE-Metrik (Blind/Referenceless Image Spatial Quality Evaluator). Das Projekt enthält zwei Versionen: ein Kommandozeilen-Tool und eine Anwendung mit grafischer Benutzeroberfläche (GUI).

## Voraussetzungen

Bevor du beginnst, stelle sicher, dass du folgende Abhängigkeiten installiert hast:

- **Python 3.x**
- **pip** (zum Installieren von Python-Paketen)

### Erforderliche Python-Pakete:

- `opencv-python` für Bildverarbeitung
- `torch` für Deep-Learning-Unterstützung
- `piq` für Bildqualitätsmetriken (BRISQUE)
- `halo` für die Ladeanimation (Spinner UI)
- `tkinter` für die GUI
- `Pillow` für Bildbearbeitung

Zum Installieren der benötigten Abhängigkeiten führe folgenden Befehl aus:

```bash
pip install opencv-python torch piq halo tkinter pillow
```

---

## 1. Kommandozeilen-Version

Die Kommandozeilen-Version ermöglicht es dir, die Qualität eines Bildes zu bewerten, indem der BRISQUE-Score berechnet wird.

### Anwendung:

1. Klone oder lade dieses Repository herunter.
2. Öffne dein Terminal oder die Eingabeaufforderung.
3. Navigiere in den Ordner, in dem sich das Skript befindet.
4. Führe den folgenden Befehl aus, um die Bildqualität zu bewerten:

```bash
python image_quality.py <image_path>
```

Ersetze `<image_path>` durch den Pfad zum Bild, das du analysieren möchtest. Zum Beispiel:

```bash
python image_quality.py bild.jpg
```

Das Skript gibt den BRISQUE-Score sowie eine Interpretation der Bildqualität aus:

```bash
Ergebnisse der Bildqualitätsbewertung: BRISQUE-Score: 45.25 (Niedriger ist besser)

Interpretationshilfe:
0  - 20 : Hervorragende Qualität
20 - 40 : Gute Qualität
40 - 60 : Mittelmäßige Qualität
60 - 80 : Schlechte Qualität
80 - 100: Sehr schlechte Qualität
```

---

## 2. GUI-Version

Die GUI-Version bietet eine Benutzeroberfläche, in der du ein Bild auswählen kannst. Das Programm berechnet dann den BRISQUE-Score und zeigt ihn zusammen mit einer Interpretation an.

### Anwendung:

1. Klone oder lade dieses Repository herunter.
2. Stelle sicher, dass alle oben genannten Abhängigkeiten installiert sind.
3. Starte die GUI-Anwendung mit folgendem Befehl:

```bash
python image_quality_gui.py
```

4. Es öffnet sich ein Fenster, in dem du auf „📂 Bild auswählen“ klicken kannst, um ein Bild hochzuladen. Das Bild wird angezeigt und der BRISQUE-Score zusammen mit einer Bewertungsskala ausgegeben.

---
