"""
PDF Reader with OCR fallback
"""

def extract_text_from_pdf(path, use_ocr=False):
    text_parts = []

    # Try pdfplumber
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                txt = page.extract_text()
                if txt:
                    text_parts.append(txt)
    except:
        pass

    # Try PyPDF2 if still empty
    if not text_parts:
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(path)
            for p in reader.pages:
                try:
                    txt = p.extract_text()
                    if txt:
                        text_parts.append(txt)
                except:
                    pass
        except:
            pass

    # OCR fallback
    if not text_parts and use_ocr:
        try:
            from pdf2image import convert_from_path
            import pytesseract
            imgs = convert_from_path(path, dpi=200)
            text = ""
            for img in imgs:
                text += pytesseract.image_to_string(img) + "\n"
            return text
        except:
            return ""

    return "\n\n".join(text_parts)
