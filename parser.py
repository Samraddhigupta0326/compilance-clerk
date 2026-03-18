import pdfplumber
import pytesseract

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text
            else:
                # OCR fallback
                img = page.to_image().original
                text += pytesseract.image_to_string(img)

    return text