import re

def extract_projects(text):
    """
    Detects project entries of the pattern:
    'Project Name — Tech1, Tech2 YEAR • description...'
    Returns a list of dicts, one per project.
    """

    
    pattern = re.compile(
        r'([A-Z][A-Za-z0-9\s]+(?:System|Assistant|Generator|Tool|App|Application|Model|Classifier|Predictor|Analyzer|Bot)?)\s*'
        r'[—\-]\s*'
        r'([A-Za-z0-9,\.\s]+?)\s*'
        r'((?:19|20)\d{2})\s*'
        r'((?:•[^•]+)+)'
    )

    matches = pattern.finditer(text)
    projects = []

    for match in matches:
        title = match.group(1).strip()
        tech_raw = match.group(2).strip()
        year = match.group(3).strip()
        description_raw = match.group(4).strip()

        
        technologies = [t.strip() for t in tech_raw.split(",") if t.strip()]

        
        bullets = [b.strip(" •") for b in description_raw.split("•") if b.strip(" •")]

        projects.append({
            "Project Name": title,
            "Technologies": technologies,
            "Year": year,
            "Description": bullets
        })

    return projects


def extract_github_links_for_projects(text):
    """
    Finds any GitHub repo-style links (not just profile links) that
    might be tied to specific projects, e.g. github.com/user/repo-name
    """
    pattern = r'github\.com/[A-Za-z0-9_\-]+/[A-Za-z0-9_\-]+'
    return re.findall(pattern, text, re.IGNORECASE)