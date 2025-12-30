import PyPDF2
import docx2txt

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text

    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)

    else:
        return ""
