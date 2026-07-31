import re

ACTION_VERBS = [
    "developed", "built", "designed", "implemented", "created",
    "led", "managed", "optimized", "achieved", "improved",
    "automated", "analyzed", "deployed", "engineered", "delivered"
]

REQUIRED_SECTIONS = [
    "education", "experience", "skills", "projects"
]


def check_section_completeness(text):
    """Checks which standard resume sections are present."""
    text_lower = text.lower()
    found = {}
    for section in REQUIRED_SECTIONS:
        found[section.title()] = section in text_lower
    return found


def count_action_verbs(text):
    """Counts how many distinct action verbs appear (writing quality signal)."""
    text_lower = text.lower()
    used = [verb for verb in ACTION_VERBS if verb in text_lower]
    return used


def has_quantified_achievements(text):
    """
    Looks for numbers/percentages next to achievement language —
    e.g. '95% accuracy', '50,000+ records', '15+ tools'.
    This is a strong ATS/recruiter signal.
    """
    pattern = r'\d+[\+%]?\s*(?:%|percent|accuracy|records|users|projects|tools|hours|days)?'
    matches = re.findall(pattern, text)
   
    quantified = [m for m in matches if m and not re.fullmatch(r'(19|20)\d{2}', m)]
    return len(quantified)


def keyword_match(resume_text, job_description):
    """
    Compares resume text against a job description and returns
    which important keywords from the JD are missing from the resume.
    """
    if not job_description:
        return {"matched": [], "missing": [], "match_percent": None}

    
    jd_words = set(re.findall(r'\b[A-Za-z][A-Za-z0-9\.\+#]{3,}\b', job_description.lower()))
    resume_words = set(re.findall(r'\b[A-Za-z][A-Za-z0-9\.\+#]{3,}\b', resume_text.lower()))

    matched = sorted(jd_words & resume_words)
    missing = sorted(jd_words - resume_words)

    match_percent = round((len(matched) / len(jd_words)) * 100, 1) if jd_words else 0

    return {
        "matched": matched,
        "missing": missing,
        "match_percent": match_percent
    }


def calculate_ats_score(text, skills, job_description=None):
    """
    Combines all signals into one 0-100 ATS score.
    Weighting (adjust as you like):
      - Section completeness: 30 points
      - Skills detected: 25 points
      - Action verbs used: 15 points
      - Quantified achievements: 15 points
      - Keyword match with JD (if provided): 15 points
    """
    score = 0
    suggestions = []

    
    sections = check_section_completeness(text)
    sections_present = sum(sections.values())
    score += (sections_present / len(REQUIRED_SECTIONS)) * 30
    for section, present in sections.items():
        if not present:
            suggestions.append(f"Add a clear '{section}' section")

    
    skill_score = min(len(skills), 10) / 10 * 25
    score += skill_score
    if len(skills) < 5:
        suggestions.append("List more relevant technical skills")

    
    verbs_used = count_action_verbs(text)
    verb_score = min(len(verbs_used), 8) / 8 * 15
    score += verb_score
    if len(verbs_used) < 4:
        suggestions.append("Use more action verbs (e.g. 'built', 'led', 'optimized')")

    
    quant_count = has_quantified_achievements(text)
    quant_score = min(quant_count, 6) / 6 * 15
    score += quant_score
    if quant_count < 2:
        suggestions.append("Add measurable results (e.g. '95% accuracy', '50,000+ records')")

    
    if job_description:
        km = keyword_match(text, job_description)
        score += (km["match_percent"] or 0) / 100 * 15
        if km["missing"]:
            suggestions.append(f"Consider adding these keywords from the job description: {', '.join(km['missing'][:8])}")
    else:
       
        score += 0  

    return {
        "ATS Score": round(score),
        "Section Completeness": sections,
        "Action Verbs Used": verbs_used,
        "Quantified Achievements": quant_count,
        "Suggestions": suggestions
    }