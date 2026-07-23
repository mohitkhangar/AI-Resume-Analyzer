def extract_skills(text):

    skills = [

        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",

        "SQL",
        "MySQL",
        "MongoDB",

        "Machine Learning",
        "Deep Learning",
        "Data Science",

        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Scikit-learn",

        "TensorFlow",
        "PyTorch",

        "Flask",
        "Django",

        "Git",
        "GitHub",

        "Docker",
        "Kubernetes",

        "AWS",
        "Azure",
        "GCP"

    ]

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills