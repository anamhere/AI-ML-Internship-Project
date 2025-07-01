import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import read_resume

# 1. Read all resume text
resume_folder = "resumes"
resume_texts = []

for file in os.listdir(resume_folder):
    file_path = os.path.join(resume_folder, file)
    text = read_resume(file_path)
    resume_texts.append(text)

# 2. Read the job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# 3. Combine for vectorization
corpus = resume_texts + [jd_text]  # combine resumes and JD

# 4. Fit vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(corpus)

# 5. Save vectorizer
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ TfidfVectorizer trained and saved to models/vectorizer.pkl")
