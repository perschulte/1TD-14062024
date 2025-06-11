# 1TD-14062024

Dieses Repository enthaelt eine Sammlung einfacher Python-Skripte, die den Einsatz von LLM-APIs demonstrieren. Es gibt ein Flask-Backend, mehrere kleine Streamlit-Oberflaechen und ein Beispiel zum Sortieren von Dateien bzw. E-Mails.

## Voraussetzungen

- Python 3.10 oder neuer
- Abhaengigkeiten laut untenstehender Liste
- Eine `.env`-Datei mit `OPENAI_API_KEY` und optional `GROQ_API_KEY`

### Installation der Abhaengigkeiten

```bash
pip install flask streamlit openai groq python-dotenv PyPDF2 markdownify
```

## Nutzung

### Backend starten

```bash
python 1td_backend.py
```

Der Server stellt eine Route `/api/get_response` bereit. Ueber `1td_backend_demo_app.py` kann man darauf zugreifen:

```bash
streamlit run 1td_backend_demo_app.py
```

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

Beispieldaten befinden sich im Ordner `data/emails`.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details siehe `LICENSE`.
