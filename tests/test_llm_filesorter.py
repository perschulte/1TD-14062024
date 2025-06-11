import io
import json

def test_read_json_file(llm):
    data = [{"a": 1, "b": 2}]
    file_obj = io.BytesIO(json.dumps(data).encode("utf-8"))
    assert llm.read_json_file(file_obj) == data

def test_pdf_to_markdown(llm):
    text = "Hello PDF"
    pdf_bytes = io.BytesIO(text.encode("utf-8"))
    result = llm.pdf_to_markdown(pdf_bytes)
    assert text in result
