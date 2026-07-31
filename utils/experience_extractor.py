# utils/experience_extractor.py

import re

def extract_work_experience(text):
    """Extract work experience from resume text"""
    experience = []
    
    # Common experience section headers
    exp_headers = [
        r'work experience', r'experience', r'employment',
        r'work history', r'professional experience',
        r'internship', r'internships'
    ]
    
    # Find experience section
    text_lower = text.lower()
    
    # Extract years of experience
    year_patterns = [
        r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
        r'experience\s*(?:of\s*)?(\d+)\+?\s*years?',
    ]
    
    years_found = []
    for pattern in year_patterns:
        matches = re.findall(pattern, text_lower)
        years_found.extend(matches)
    
    # Extract job titles
    job_titles = [
        'software engineer', 'data scientist', 'ml engineer',
        'python developer', 'data analyst', 'backend developer',
        'frontend developer', 'full stack developer',
        'machine learning engineer', 'ai engineer',
        'software developer', 'intern', 'developer'
    ]
    
    found_titles = []
    for title in job_titles:
        if title in text_lower:
            found_titles.append(title.title())
    
    # Extract companies (simple heuristic)
    company_patterns = [
        r'at\s+([A-Z][a-zA-Z\s]+(?:Inc|Ltd|Pvt|Solutions|Technologies|Tech|Systems)?)',
        r'@\s*([A-Z][a-zA-Z\s]+)',
    ]
    
    companies = []
    for pattern in company_patterns:
        matches = re.findall(pattern, text)
        companies.extend([m.strip() for m in matches if len(m.strip()) > 2])
    
    return {
        'years': years_found[0] if years_found else 'Not specified',
        'titles': found_titles[:3],  # top 3
        'companies': list(set(companies))[:3]
    }


def extract_role(text):
    """Extract primary role from resume"""
    text_lower = text.lower()
    
    roles = [
        'machine learning engineer', 'data scientist',
        'software engineer', 'python developer',
        'data analyst', 'ai engineer', 'ml engineer',
        'backend developer', 'full stack developer',
        'software developer'
    ]
    
    for role in roles:
        if role in text_lower:
            return role.title()
    
    return 'Not specified'