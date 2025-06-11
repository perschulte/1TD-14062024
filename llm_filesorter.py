import os
import json
import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv
import PyPDF2
from markdownify import markdownify as md

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Abrufen des API-Schlüssels aus den Umgebungsvariablen
gpt_4o = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def read_json_file(json_file):
    """Reads a JSON file and returns its content."""
    content = json_file.read().decode('utf-8')
    return json.loads(content)

def pdf_to_markdown(pdf_file):
    """Converts a PDF file to Markdown format.

    Args:
        pdf_file (io.BytesIO): A file-like object containing the PDF data.

    Returns:
        str: The content of the PDF file converted to Markdown format.
    """
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        if page_text:
            text += page_text
    markdown_text = md(text)
    return markdown_text

def convert_pdfs_to_markdown(pdf_files, md_folder):
    """Converts multiple PDF files to Markdown format and saves them to a specified folder.

    Args:
        pdf_files (list of io.BytesIO): A list of file-like objects containing the PDF data.
        md_folder (str): The path to the folder where the converted Markdown files should be saved.

    Returns:
        None
    """
    if not os.path.exists(md_folder):
        os.makedirs(md_folder)
    for pdf_file in pdf_files:
        md_content = pdf_to_markdown(pdf_file)
        md_file = os.path.join(md_folder, os.path.splitext(pdf_file.name)[0] + '.md')
        with open(md_file, 'w') as f:
            f.write(md_content)
    st.success("Selected PDFs have been converted to Markdown and saved.")

def read_markdown_files(md_folder):
    """Reads all Markdown files in a folder and returns their content as a dictionary.

    Args:
        md_folder (str): The path to the folder containing the Markdown files.

    Returns:
        dict: A dictionary where keys are filenames and values are file contents.
    """
    file_contents = {}
    for filename in os.listdir(md_folder):
        if filename.endswith(".md"):
            with open(os.path.join(md_folder, filename), 'r') as file:
                file_contents[filename] = file.read()
    return file_contents

def sort_emails_by_importance_gpt4o(emails, prompt):
    email_contents = "\n".join([f"Subject: {email['subject']}\nBody: {email['body']}" for email in emails])
    results = gpt_4o.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a sorting assistant AI. Sort the emails based on the given prompt.",
            },
            {
                "role": "user",
                "content": f"Prompt: {prompt}\n\nEmails:\n{email_contents}",
            }
        ],
        model="gpt-4o",
        max_tokens=300,
        temperature=0.5,
    )
    sorted_emails = results.choices[0].message.content
    return sorted_emails

def sort_emails_by_importance_groq(emails, prompt):
    email_contents = "\n".join([f"Subject: {email['subject']}\nBody: {email['body']}" for email in emails])
    results = groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a sorting assistant AI. Sort the emails based on the given prompt.",
            },
            {
                "role": "user",
                "content": f"Prompt: {prompt}\n\nEmails:\n{email_contents}",
            }
        ],
        model="llama3-8b-8192",
        max_tokens=300,
        temperature=0.5,
    )
    sorted_emails = results.choices[0].message.content
    return sorted_emails


def sort_files_by_prompt_gpt4(md_folder, prompt):
    file_contents = read_markdown_files(md_folder)
    content_str = "\n".join([f"Filename: {name}\nContent: {content}" for name, content in file_contents.items()])
    results = gpt_4o.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a sorting assistant AI. Sort the files based on the given prompt. Only return the file names.",
                            },
                            {
                                "role": "user",
                                "content": f"Prompt: {prompt}\n\nFiles:\n{content_str}",
                            }
                        ],
                        model="gpt-4o",
                        max_tokens=200,
                        temperature=0.5,
                    )
    sorted_files = results.choices[0].message.content
    return sorted_files

def sort_files_by_prompt_groq(md_folder, prompt):
    file_contents = read_markdown_files(md_folder)
    content_str = "\n".join([f"Filename: {name}\nContent: {content}" for name, content in file_contents.items()])
    results = groq.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a sorting assistant AI. Sort the files based on the given prompt. Only return the file names.",
                            },
                            {
                                "role": "user",
                                "content": f"Prompt: {prompt}\n\nFiles:\n{content_str}",
                            }
                        ],
                        model="Mixtral-8x7b-32768",
                        max_tokens=200,
                        temperature=0.5,
                    )
    sorted_files = results.choices[0].message.content
    return sorted_files


markdown_folder = ".markdown"

# Streamlit App
st.title("KI-Enhanced Frontend Control")

st.write("### Emailsortierung mit KI")
uploaded_file = st.file_uploader("Wähle eine JSON-Datei aus", type=["json"])

if uploaded_file:
    emails = read_json_file(uploaded_file)
    st.write("### Unsortierte Emails")
    st.write(emails)
    
    user_prompt = st.text_input("Gib einen Prompt ein, um die Emails zu sortieren")

    if st.button('Sortiere Emails'):
        if user_prompt:
            with st.spinner("Sorting emails..."):
                with ThreadPoolExecutor() as executor:
                    future_gpt4 = executor.submit(sort_emails_by_importance_gpt4o, emails, user_prompt)
                    future_groq = executor.submit(sort_emails_by_importance_groq, emails, user_prompt)
                    
                    sorted_emails_gpt4 = future_gpt4.result()
                    sorted_emails_groq = future_groq.result()

            col1, col2 = st.columns(2)
            
            with col1:
                st.write("### GPT-4 Sortierte Emails")
                st.write(sorted_emails_gpt4)
            
            with col2:
                st.write("### Groq Sortierte Emails")
                st.write(sorted_emails_groq)
        else:
            st.error("Bitte gib einen Prompt ein.")
