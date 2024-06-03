import streamlit as st
import requests

st.title("KI-Backend Demo")

prompt = st.text_input("Gib deine Prompt ein:")

if st.button("Absenden"):
    response = requests.post(
        "http://localhost:5000/api/get_response",
        json={"prompt": prompt}
    )
    if response.status_code == 200:
        st.success(response.json().get("response"))
    else:
        st.error("Fehler: " + response.json().get("error"))
