import re

DEGREES = [
    "Bachelor of Engineering",
    "B.E.",
    "BE",
    "Bachelor of Technology",
    "B.Tech",
    "BTech",
    "M.Tech",
    "MTech",
    "MBA",
    "MCA",
    "BCA",
    "B.Sc",
    "M.Sc",
    "PhD"
]


def extract_degree(text):
    for degree in DEGREES:
        if degree.lower() in text.lower():
            return degree
    return "Not Found"


BRANCHES = [
    "Computer Engineering",
    "Computer Science",
    "Information Technology",
    "Artificial Intelligence and Data Science",
    "Artificial Intelligence",
    "Electronics and Telecommunication",
    "Electronics & Telecommunication",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Electronics Engineering",
    "Data Science"
]

def extract_branch(text):
    for branch in BRANCHES:
        if branch.lower() in text.lower():
            return branch
    return "Not Found"


UNIVERSITIES = [
    "Savitribai Phule Pune University",
    "Mumbai University",
    "Delhi University",
    "VIT",
    "BITS Pilani",
    "IIT",
    "NIT"
]


def extract_university(text):
    for university in UNIVERSITIES:
        if university.lower() in text.lower():
            return university
    return "Not Found"


cgpa_pattern = r'CGPA\s*[:\-]?\s*(\d+(?:\.\d+)?)'


def extract_cgpa(text):
    match = re.search(cgpa_pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    return "Not Found"


percentage_pattern = r'\d+(?:\.\d+)?%'


def extract_percentage(text):
    """Returns a single percentage string instead of a list."""
    match = re.search(percentage_pattern, text)
    if match:
        return match.group()
    return "Not Found"


year_pattern = r'\b(?:19|20)\d{2}\b'


def extract_passing_year(text):
    years = re.findall(year_pattern, text)
    if years:
        return years[-1]
    return "Not Found"


def extract_education(text):
    return {
        "Degree": extract_degree(text),
        "Branch": extract_branch(text),
        "University": extract_university(text),
        "CGPA": extract_cgpa(text),
        "Percentage": extract_percentage(text),
        "Passing Year": extract_passing_year(text)
    }