from transformers import pipeline
from langdetect import detect
import PyPDF2

# Load summarization pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    lang = detect(text)
    if lang != 'en':
        return "Only English text is supported currently."
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_text_from_file(file):
    if file.filename.endswith('.txt'):
        return file.read().decode('utf-8')
    elif file.filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    else:
        raise ValueError("Unsupported file format. Please upload a .txt or .pdf file.")
