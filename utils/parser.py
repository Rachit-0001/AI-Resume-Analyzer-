import pdfplumber
import docx

def extract_text(file_path):
    if file_path.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    elif file_path.lower().endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)

    return ""
