import re

def extract_email(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return "Not Found"


def extract_phone(text):
    pattern = r'(\+?\d{1,3}[- ]?)?\d{10}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return "Not Found"


def extract_linkedin(text):
    # Handles both "https://linkedin.com/in/..." and bare "linkedin.com/in/..."
    pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group()
    return "Not Found"


def extract_github(text):
    # Handles both "https://github.com/..." and bare "github.com/..."
    pattern = r'(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group()
    return "Not Found"


def extract_portfolio(text):
    urls = re.findall(r'https?://[^\s|]+', text)
    for url in urls:
        if "linkedin" not in url.lower() and "github" not in url.lower():
            return url
    return "Not Found"


def extract_name(text):
    """
    Grabs the name from the very start of the resume text.
    Assumes the name appears as 1-4 capitalized words before
    a phone number, digit, or '|' separator.
    """
    text = text.strip()

    # Try to capture leading capitalized words before a digit (phone number) or pipe
    match = re.match(
        r'^([A-Z][A-Za-z.]*(?:\s+[A-Z][A-Za-z.]*){0,3})(?=\s*(?:\d|\|))',
        text
    )
    if match:
        return match.group(1).strip()

    # Fallback: just take the first line, truncated to avoid dumping the whole resume
    first_line = text.split("\n")[0].strip()
    if first_line:
        return first_line[:60]  # safety cap

    return "Not Found"


def extract_contact_info(text):
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "GitHub": extract_github(text),
        "Portfolio": extract_portfolio(text)
    }