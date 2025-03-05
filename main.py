import fitz  # PyMuPDF
import requests
import os
import json
from nltk.tokenize import sent_tokenize, word_tokenize

# Load configuration from JSON file
def load_config(config_path: str = "config.json") -> dict:
    """Load configuration from a JSON file."""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config file: {e}")
        return {}

def download_pdf(url: str, pdf_path: str, timeout: int) -> bool:
    """Download PDF from a URL and save it locally."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded successfully: {pdf_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return False

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a given PDF file."""
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found.")
        return ""

    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        print(f"Extracted text from PDF: {pdf_path}")
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def save_text_to_file(text: str, output_file: str) -> None:
    """Save extracted text to a file."""
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted text saved to: {output_file}")
    except Exception as e:
        print(f"Error saving text to file: {e}")

# Main script execution
if __name__ == "__main__":
    config = load_config()  # Load config values

    pdf_url = config.get("pdf_url", "")
    pdf_file = config.get("pdf_file", "downloaded_paper.pdf")
    text_file = config.get("text_file", "extracted_text.txt")
    timeout = config.get("timeout", 60)

    if pdf_url and download_pdf(pdf_url, pdf_file, timeout):
        extracted_text = extract_text_from_pdf(pdf_file)
        if extracted_text:
            save_text_to_file(extracted_text, text_file)
            if config.get("debug", False):
                print(extracted_text[:1000])  # Print first 1000 characters for preview
