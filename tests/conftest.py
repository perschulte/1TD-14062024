import sys
import types
import importlib
import contextlib


def load_module():
    import os
    root = os.path.dirname(os.path.dirname(__file__))
    if root not in sys.path:
        sys.path.insert(0, root)
    st = types.SimpleNamespace(
        title=lambda *a, **k: None,
        write=lambda *a, **k: None,
        file_uploader=lambda *a, **k: None,
        text_input=lambda *a, **k: "",
        button=lambda *a, **k: False,
        columns=lambda n: (None,) * n,
        success=lambda *a, **k: None,
    )
    @contextlib.contextmanager
    def spinner(msg):
        yield
    st.spinner = spinner

    openai_mod = types.SimpleNamespace(OpenAI=lambda *a, **k: types.SimpleNamespace(chat=types.SimpleNamespace(completions=types.SimpleNamespace(create=lambda *a, **k: types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=""))])))))
    groq_mod = types.SimpleNamespace(Groq=lambda *a, **k: types.SimpleNamespace(chat=types.SimpleNamespace(completions=types.SimpleNamespace(create=lambda *a, **k: types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=""))])))))
    markdownify_mod = types.SimpleNamespace(markdownify=lambda text: text)
    dotenv_mod = types.SimpleNamespace(load_dotenv=lambda: None)

    class DummyPage:
        def __init__(self, text):
            self._text = text
        def extract_text(self):
            return self._text

    class DummyPdfReader:
        def __init__(self, file_obj):
            content = file_obj.read().decode("utf-8")
            self.pages = [DummyPage(content)]

    PyPDF2_mod = types.SimpleNamespace(PdfReader=DummyPdfReader)

    for name, module in {
        "streamlit": st,
        "openai": openai_mod,
        "groq": groq_mod,
        "markdownify": markdownify_mod,
        "PyPDF2": PyPDF2_mod,
        "dotenv": dotenv_mod,
    }.items():
        sys.modules[name] = module

    if "llm_filesorter" in sys.modules:
        del sys.modules["llm_filesorter"]
    module = importlib.import_module("llm_filesorter")
    return module


import pytest


@pytest.fixture
def llm(monkeypatch):
    return load_module()
