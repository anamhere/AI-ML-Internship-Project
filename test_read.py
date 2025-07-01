# test_read.py
from utils import read_resume
import os

resume_folder = "resumes"

for file in os.listdir(resume_folder):
    file_path = os.path.join(resume_folder, file)
    text = read_resume(file_path)
    print(f"--- {file} ---")
    print(text[:500])  # Print first 500 characters
    print("\n\n")
from utils import read_resume, extract_entities

# Example:
resume_text = read_resume("resumes/john_doe.txt")
entities = extract_entities(resume_text)

print(entities)
from utils import parse_job_description

job_info = parse_job_description("job_description.txt")
print(job_info)
from utils import read_resume, extract_entities, parse_job_description, score_resume

# Parse job description info once
jd_info = parse_job_description("job_description.txt")

# Parse one resume
resume_text = read_resume("resumes/john_doe.txt")
resume_info = extract_entities(resume_text)

# Score it
score = score_resume(resume_info, jd_info)

print(f"Resume score: {score:.2f}")
