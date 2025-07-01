# utils.py

import os
from pdfminer.high_level import extract_text

def read_resume(file_path):
    """
    Reads and extracts text from a resume file (PDF or TXT).
    """
    if file_path.endswith(".pdf"):
        try:
            return extract_text(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    elif file_path.endswith(".txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    else:
        print(f"Unsupported file type: {file_path}")
        return ""
import spacy

# Load spaCy English model (make sure you've downloaded it already)
nlp = spacy.load("en_core_web_sm")

# Define keywords to look for
SKILLS = ["python", "machine learning", "data analysis", "nlp", "sql", "excel"]
EDU_KEYWORDS = ["bachelor", "master", "phd", "b.sc", "m.sc", "b.tech", "m.tech"]

def extract_entities(text):
    """
    Extract skills, education, and experience years from resume text using NLP.
    """
    doc = nlp(text.lower())  # lowercase for case-insensitive matching
    tokens = [token.text for token in doc]

    # Find skills present in text
    skills_found = [skill for skill in SKILLS if skill in tokens]

    # Find education keywords
    education = [token for token in tokens if token in EDU_KEYWORDS]

    # Naively extract years of experience from DATE entities containing "year"
    experience_years = 0
    for ent in doc.ents:
        if ent.label_ == "DATE" and "year" in ent.text.lower():
            try:
                # Extract the first digit found in the date phrase
                num = int([word for word in ent.text.split() if word.isdigit()][0])
                experience_years = max(experience_years, num)
            except (IndexError, ValueError):
                continue

    return {
        "skills": skills_found,
        "education": education,
        "experience_years": experience_years
    }
def parse_job_description(path="job_description.txt"):
    """
    Reads the job description file, extracts skills, education, and experience.
    """
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # lowercase for matching consistency
    return extract_entities(text)
def score_resume(resume_data, jd_data):
    """
    Scores a resume against the job description data.
    Parameters:
      - resume_data: dict with keys 'skills', 'education', 'experience_years'
      - jd_data: dict with keys 'skills', 'education', 'experience_years'
    Returns:
      - final_score: float between 0 and 1 (higher is better)
    """
    # Skill match ratio (0 to 1)
    skill_overlap = len(set(resume_data['skills']) & set(jd_data['skills'])) / max(1, len(jd_data['skills']))

    # Education match (0 or 1)
    edu_match = 1 if len(set(resume_data['education']) & set(jd_data['education'])) > 0 else 0

    # Experience score normalized to max 1 (assuming 5+ years is ideal)
    exp_score = min(resume_data['experience_years'] / 5, 1.0)

    # Weighted sum of components
    final_score = (0.5 * skill_overlap) + (0.2 * edu_match) + (0.3 * exp_score)

    return final_score
