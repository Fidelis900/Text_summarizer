# 📝 Text Summarizer Web App

A simple and intelligent web application that summarizes English text using state-of-the-art NLP models from Hugging Face. Built with Flask and JavaScript.

---

## 🚀 Features

| Feature               | Description                                                                    |
| --------------------- | ------------------------------------------------------------------------------ |
| 🔁 Clear Button       | Easily clear the input text box with one click                                 |
| 📄 File Upload        | Upload `.txt` or `.pdf` files and extract text for summarization               |
| 🌍 Language Detection | Automatically detects the input language (only English is currently supported) |
| 🗂 Summary History     | Save previous summaries during a session (optional/future improvement)         |

---

## 📦 Technologies Used

- **Backend**: Python, Flask, Transformers (`facebook/bart-large-cnn`)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Language Detection**: `langdetect`
- **File Parsing**: `PyPDF2`, built-in Python file handling
- **API Integration**: Flask routes handle both raw text and file uploads

---

## 📁 Project Structure

summary_bot/
│
├── app.py # Flask server (backend)
├── summarizer.py # Text summarization + file extraction logic
├── templates/
│ └── index.html # HTML interface (frontend)
├── static/
│ └── script.js # JavaScript for UI interactions & API calls
│ └── style.css # (Optional) CSS file for styling
├── README.md # Project overview and documentation
└── requirements.txt # All dependencies

create and activate virtual Environment
python -m venv summary
summary\Scripts\activate # On Windows

install Dependencies
pip install -r requirements.txt

Run the app
python app.py

Visit
Open your browser and go to: http://localhost:5000

🧠 How It Works
Summarization: Sends input to Hugging Face's BART model and returns a concise summary.

File Upload: Accepts .txt or .pdf, extracts text, and sends it to the summarizer.

Language Detection: Uses langdetect to ensure the text is in English.

Frontend Interaction: Uses JavaScript fetch() to POST input to Flask endpoints and update the page without reloads.

💡 Example Usage
Paste a block of text or upload a file.

Click Summarize.

View the summary below.

Use Clear to reset and start over.

🧾 License
MIT License. Feel free to modify and use
