from openai import OpenAI
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from groq import Groq

# Laden der Umgebungsvariablen aus der .env-Datei
# Dies stellt sicher, dass sensible Informationen wie API-Schlüssel nicht im Code hartkodiert werden
load_dotenv()

# Abrufen des OpenAI API-Schlüssels aus den Umgebungsvariablen
# OpenAI-Instanz mit dem API-Schlüssel initialisieren
openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Funktion zum Abschicken der OpenAI-Prompt
# Diese Funktion sendet eine Anfrage an die OpenAI API und erhält eine Antwort
def get_openai_response(prompt):
    # Verwenden des GPT-4o-Modells, um eine Antwort auf die gegebene Eingabe (Prompt) zu generieren
    results = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o", #OpenAI
        #model="llama3-8b-8192", # Groq
        max_tokens=200, # Begrenzung der Antwort auf maximal 200 Tokens
        temperature=0.5, # Steuerung der Kreativität der Antwort (0.5 ist ein moderater Wert)
    )
    
    # Extrahieren der generierten Nachricht aus der API-Antwort
    message = results.choices[0].message.content
    return message

# Flask-Anwendung
# Flask ist ein leichtgewichtiges Web-Framework für Python, das für den Aufbau von Webservern verwendet wird
app = Flask(__name__)

# Definition einer API-Route, die POST-Anfragen an '/api/get_response' entgegennimmt
@app.route('/api/get_response', methods=['POST'])
def api_get_response():
    # Extrahieren der JSON-Daten aus der Anfrage
    data = request.get_json()
    prompt = data.get('prompt')
    
    # Überprüfen, ob die 'prompt'-Daten im JSON vorhanden sind
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400 # 400 Bad Request, wenn kein Prompt vorhanden ist

    try:
        # Aufrufen der Funktion zum Abrufen der OpenAI-Antwort und Rückgabe der Antwort als JSON
        response = get_openai_response(prompt)
        return jsonify({"response": response})
    except Exception as e:
        # Fehlerbehandlung und Rückgabe einer Fehlernachricht im Fehlerfall
        return jsonify({"error": str(e)}), 500 # 500 Internal Server Error bei Ausnahmen

# Starten des Flask-Webservers, wenn dieses Skript direkt ausgeführt wird
if __name__ == '__main__':
    app.run(debug=True) # Der Debug-Modus ist aktiviert, um detaillierte Fehlerprotokolle während der Entwicklung anzuzeigen
