from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


if __name__ == "__main__":
    file_path = "CHINMAY SEHGAL AI python intern resume dce.pdf"   
    extracted_text = extract_text_from_pdf(file_path)

    print("----- Extracted Resume Text -----\n")
    print(extracted_text)