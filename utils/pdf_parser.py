import pdfplumber


def extract_text(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""

        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text