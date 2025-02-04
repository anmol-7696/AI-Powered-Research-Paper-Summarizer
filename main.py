import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)  # Open the PDF file
    for page in doc:
        text += page.get_text("text") + "\n"  # Extract text from each page
    return text

# Example usage
pdf_file = "sample_research_paper.pdf"  # Replace with your PDF file
extracted_text = extract_text_from_pdf(pdf_file)
print(extracted_text[:1000])  # Print first 1000 characters for preview
