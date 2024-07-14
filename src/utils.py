import os
import json
import PyPDF2
from .config import UPLOAD_DIR, ALLOWED_EXTENSIONS


def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_uploaded_file(uploaded_file):
    """Save the uploaded file to the upload directory and extract its text"""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract and save the text content
    text_content = extract_text_from_pdf(file_path)
    save_pdf_text(uploaded_file.name, text_content)

    return file_path


def extract_text_from_pdf(file_path):
    """Extract text content from a PDF file"""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def get_existing_pdfs():
    """Get a list of existing PDFs in the upload directory"""
    if not os.path.exists(UPLOAD_DIR):
        return []
    return [f for f in os.listdir(UPLOAD_DIR) if f.endswith('.pdf')]


def save_pdf_text(pdf_name, text_content):
    """Save extracted text content to a JSON file"""
    text_file_path = os.path.join(UPLOAD_DIR, f"{pdf_name}.json")
    with open(text_file_path, 'w') as f:
        json.dump({"text": text_content}, f)


def load_pdf_text(pdf_name):
    """Load extracted text content from a JSON file"""
    text_file_path = os.path.join(UPLOAD_DIR, f"{pdf_name}.json")
    if os.path.exists(text_file_path):
        with open(text_file_path, 'r') as f:
            return json.load(f)["text"]
    return None


def read_pdf_content(pdf_files):
    """Read and combine text from selected PDFs"""
    pdf_texts = []
    for pdf_file in pdf_files:
        text_content = load_pdf_text(pdf_file)
        if text_content is None:
            # If text content is not found, extract it and save
            file_path = os.path.join(UPLOAD_DIR, pdf_file)
            text_content = extract_text_from_pdf(file_path)
            save_pdf_text(pdf_file, text_content)
        pdf_texts.append(text_content)
    return "\n".join(pdf_texts)


def delete_pdf(pdf_file):
    """Delete a PDF file and its associated text content from the upload directory"""
    file_path = os.path.join(UPLOAD_DIR, pdf_file)
    text_file_path = os.path.join(UPLOAD_DIR, f"{pdf_file}.json")
    deleted = False
    if os.path.exists(file_path):
        os.remove(file_path)
        deleted = True
    if os.path.exists(text_file_path):
        os.remove(text_file_path)
        deleted = True
    return deleted
