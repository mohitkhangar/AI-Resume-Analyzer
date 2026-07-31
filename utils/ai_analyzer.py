import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def get_ai_resume_review(resume_text, education, experience, skills):

    prompt = f"""
You are an expert technical recruiter and career coach.

Review this resume.

Resume:

{resume_text[:4000]}

Skills:
{', '.join(skills)}

Education:
{education}

Experience:
{experience}

Provide your response in exactly this format.

STRENGTHS:
- ...

WEAKNESSES:
- ...

SKILL GAPS:
- ...

RECOMMENDATION:
...
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def parse_ai_review(raw_text):

    sections = {
        "Strengths": [],
        "Weaknesses": [],
        "Skill Gaps": [],
        "Recommendation": ""
    }

    current_section = None

    for line in raw_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        upper = line.upper()

        if "STRENGTHS" in upper:
            current_section = "Strengths"
            continue

        elif "WEAKNESSES" in upper:
            current_section = "Weaknesses"
            continue

        elif "SKILL GAPS" in upper:
            current_section = "Skill Gaps"
            continue

        elif "RECOMMENDATION" in upper:
            current_section = "Recommendation"
            continue

        if current_section in ("Strengths", "Weaknesses", "Skill Gaps"):
            sections[current_section].append(
                line.lstrip("-• ").strip()
            )

        elif current_section == "Recommendation":
            sections["Recommendation"] += " " + line

    return sections