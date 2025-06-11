# 1TD-14062024

Dieses Repository enthaelt eine Sammlung einfacher Python-Skripte, die den Einsatz von LLM-APIs demonstrieren. Enthalten sind ein kleines Flask-Backend, einige Streamlit-Oberflaechen sowie ein Beispiel zur Sortierung von Dateien bzw. E-Mails mittels KI.

## Voraussetzungen

- Python 3.10 oder neuer
- Abhaengigkeiten laut untenstehender Liste
- Eine `.env`-Datei mit `OPENAI_API_KEY` und optional `GROQ_API_KEY`

### Installation der Abhaengigkeiten

```bash
pip install flask streamlit openai groq python-dotenv PyPDF2 markdownify
```

### Einrichten der `.env`-Datei

Legen Sie im Projektverzeichnis eine Datei namens `.env` mit folgendem Inhalt an:

```bash
OPENAI_API_KEY=<Ihr OpenAI-Schluessel>
# Optionaler Schluessel fuer Groq
GROQ_API_KEY=<Ihr Groq-Schluessel>
```

## Nutzung

### Backend starten

```bash
python 1td_backend.py
```

Der Server stellt eine Route `/api/get_response` bereit. Ueber die folgende Demo-Anwendung laesst sich die API direkt ausprobieren:

```bash
streamlit run 1td_backend_demo_app.py
```

Die Anwendung sendet den eingegebenen Prompt an das lokale Backend und zeigt die erhaltene Antwort an.

### Einfaches Frontend

Die Datei `1td_frontend.py` zeigt ein minimales Streamlit-Beispiel, das einen kurzen Dankestext generieren laesst.

```bash
streamlit run 1td_frontend.py
```

### Dateisortierung mit KI

`llm_filesorter.py` erlaubt das Hochladen von PDFs oder einer Beispiel-JSON mit E-Mails, die anschließend sortiert oder in Markdown umgewandelt werden koennen.

```bash
streamlit run llm_filesorter.py
```

Beispieldaten befinden sich im Ordner `data/emails`. Die Anwendung konvertiert zunaechst ausgewaehlte PDF-Dateien in Markdown und sortiert diese anschliessend anhand Ihres Prompts.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details siehe `LICENSE`.
