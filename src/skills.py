SKILLS = [
    "python", "java", "sql", "django", "flask",
    "machine learning", "nlp", "aws", "docker"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]
