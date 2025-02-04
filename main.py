import fitz  # PyMuPDF
import requests

def download_pdf(url, pdf_path):
    """Download PDF from a URL."""
    response = requests.get(url)
    with open(pdf_path, 'wb') as f:
        f.write(response.content)

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)  # Open the PDF file
    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page
    return text

# Example usage
pdf_url = "https://ir.vignan.ac.in/id/eprint/586/1/28.pdf"  # Replace with your PDF URL
pdf_file = "downloaded_paper.pdf"  # Local file path

# Download the PDF
download_pdf(pdf_url, pdf_file)

# Extract text from the downloaded PDF
extracted_text = extract_text_from_pdf(pdf_file)
print(extracted_text[:1000])  # Print first 1000 characters for preview

