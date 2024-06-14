import os
import streamlit as st
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Abrufen des API-Schlüssels aus den Umgebungsvariablen
gpt_4o = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_thank_you_message():
    results = gpt_4o.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a cheerful button AI. Make the ones the click you smile. You answer only with emojis",
                            },
                            {
                                "role": "user",
                                "content": "Some one pressed you. You know what to do!",
                            }
                        ],
                        model="gpt-4o",
                        max_tokens=20,
                        temperature=0.5,
                    )
            
    message = results.choices[0].message.content
    return message

# Streamlit App
st.title("KI-Enhanced Frontend Control")

st.write("Drücke den Button, um einen KI-generierten Dankesspruch zu erhalten.")

if st.button('Klick mich!'):
    thank_you_message = get_thank_you_message()
    st.success(thank_you_message)