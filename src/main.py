from resume_parser import extract_text
from text_cleaner import clean_text
from matcher import calculate_match
from skills import extract_skills

# File paths
resume_path = "../data/resumes/sample_resume.pdf"
jd_path = "../data/job_descriptions/sample_jd.txt"

# Read Job Description
with open(jd_path, "r", encoding="utf-8") as file:
    jd_text = file.read()

# Process texts
resume_text = extract_text(resume_path)
jd_clean = clean_text(jd_text)
resume_clean = clean_text(resume_text)

# Match score
score = calculate_match(jd_clean, resume_clean)

# Skills
resume_skills = extract_skills(resume_text)

print("Match Score:", score, "%")
print("Skills Found:", resume_skills)
