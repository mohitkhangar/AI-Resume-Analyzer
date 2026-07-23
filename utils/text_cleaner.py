import re


def clean_text(text):

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove extra newlines
    text = text.replace("\n", " ")

    # Remove tabs
    text = text.replace("\t", " ")

    return text.strip()