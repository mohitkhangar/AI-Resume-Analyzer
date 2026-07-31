import re


ISSUERS = [
    "Google", "Microsoft", "Amazon Web Services", "AWS", "IBM",
    "Coursera", "Udemy", "edX", "Meta", "Oracle", "Cisco",
    "HackerRank", "NPTEL", "Simplilearn", "DeepLearning.AI"
]

def extract_certifications(text):
    """
    Looks for a 'Certifications' section, then extracts
    individual certification lines beneath it.
    """
    certifications = []

  
    section_match = re.search(
        r'(certification[s]?)(.*?)(?=(education|experience|skills|projects|$))',
        text, re.IGNORECASE | re.DOTALL
    )

    if not section_match:
        return certifications  

    section_text = section_match.group(2)

    
    entries = re.split(r'[•\n;]', section_text)

    for entry in entries:
        entry = entry.strip()
        if not entry or len(entry) < 5:
            continue

        
        issuer = "Not Found"
        for org in ISSUERS:
            if org.lower() in entry.lower():
                issuer = org
                break

        
        year_match = re.search(r'\b(19|20)\d{2}\b', entry)
        year = year_match.group() if year_match else "Not Found"

       
        url_match = re.search(r'https?://[^\s]+', entry)
        credential_url = url_match.group() if url_match else "Not Found"

        
        name = entry
        if issuer != "Not Found":
            name = re.sub(re.escape(issuer), '', name, flags=re.IGNORECASE)
        name = re.sub(r'\b(19|20)\d{2}\b', '', name)
        name = re.sub(r'https?://[^\s]+', '', name)
        name = re.sub(r'[-–,|]+', ' ', name).strip()

        certifications.append({
            "Certification Name": name if name else "Not Found",
            "Issued By": issuer,
            "Year": year,
            "Credential URL": credential_url
        })

    return certifications