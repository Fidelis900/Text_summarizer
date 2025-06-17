from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from summarizer import summarize_text, extract_text_from_file
from langdetect import detect
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    if not text.strip():
        return jsonify({'error': 'Empty text provided'}), 400

    try:
        language = detect(text)
        if language != 'en':
            return jsonify({'summary': f"Detected language: {language}. Please use English text."})

        summary = summarize_text(text)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        text = extract_text_from_file(file)
        return jsonify({'content': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
