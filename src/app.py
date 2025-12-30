from flask import Flask, render_template, request
from resume_parser import extract_text
from text_cleaner import clean_text
from matcher import calculate_match
from skills import extract_skills
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

UPLOAD_FOLDER = os.path.join(BASE_DIR, "data", "resumes")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []

    if request.method == "POST":
        jd_text = request.form["job_description"]
        resume = request.files["resume"]

        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
        resume.save(resume_path)

        resume_text = extract_text(resume_path)

        jd_clean = clean_text(jd_text)
        resume_clean = clean_text(resume_text)

        score = calculate_match(jd_clean, resume_clean)
        skills = extract_skills(resume_text)

    return render_template("index.html", score=score, skills=skills)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
