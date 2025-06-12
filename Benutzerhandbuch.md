# Benutzerhandbuch

Dieses Handbuch beschreibt die Nutzung der im Repository enthaltenen Skripte zur Demonstration von LLM-APIs. Die Anwendungen umfassen ein kleines Flask-Backend, verschiedene Streamlit-Oberflächen und ein Beispiel zur Dateisortierung mit KI.

## Voraussetzungen

- Python 3.10 oder neuer
- Abhängigkeiten aus `requirements.txt`
- Eine `.env`-Datei mit `OPENAI_API_KEY` und optional `GROQ_API_KEY`

Installieren Sie die Pakete mit:

```bash
pip install -r requirements.txt
```

Legen Sie anschließend im Projektverzeichnis eine `.env`-Datei an:

```bash
OPENAI_API_KEY=<Ihr OpenAI-Schlüssel>
# optional
GROQ_API_KEY=<Ihr Groq-Schlüssel>
```

## Backend starten

Das Backend stellt eine Route `/api/get_response` bereit. Starten Sie es mit:

```bash
python 1td_backend.py
```

Zum Testen existiert `1td_backend_demo_app.py`. Rufen Sie diese Anwendung mit Streamlit auf, um das Backend über eine einfache Eingabemaske anzusprechen:

```bash
streamlit run 1td_backend_demo_app.py
```

## Einfaches Frontend

Die Datei `1td_frontend.py` erzeugt ein minimales Streamlit-Frontend, das bei Knopfdruck einen kurzen Dankestext erstellt:

```bash
streamlit run 1td_frontend.py
```

## Dateisortierung und PDF-Konvertierung

`llm_filesorter.py` ermöglicht das Hochladen einer JSON-Datei mit E-Mails oder von PDF-Dateien. Aus PDFs werden Markdown-Dateien erzeugt, die anschließend anhand eines eingegebenen Prompts sortiert werden können. Beispielhafte Daten befinden sich unter `data/emails`.

Starten Sie die Anwendung mit:

```bash
streamlit run llm_filesorter.py
```

Wählen Sie die gewünschten Dateien aus, geben Sie Ihren Prompt ein und lassen Sie GPT‑4o und Groq den Inhalt sortieren.

## Lizenz

Dieses Projekt verwendet die MIT-Lizenz. Details siehe `LICENSE`.

