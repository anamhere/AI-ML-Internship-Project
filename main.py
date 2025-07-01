# main.py
import os
from utils import read_resume, extract_entities, parse_job_description, score_resume
import pandas as pd

def main():
    jd_data = parse_job_description()
    results = []

    for filename in os.listdir("resumes"):
        filepath = os.path.join("resumes", filename)
        resume_text = read_resume(filepath)
        resume_data = extract_entities(resume_text)
        score = score_resume(resume_data, jd_data)
        results.append({"name": filename, "score": score})

    # Rank and save
    df = pd.DataFrame(results).sort_values(by="score", ascending=False)
    df.to_csv("output/ranked_candidates.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()
