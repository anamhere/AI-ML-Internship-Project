import os
import csv
import pickle
from utils import read_resume, extract_entities, score_resume, parse_job_description
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_folder="resumes", jd_path="job_description.txt"):
    # Load vectorizer
    with open("models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    # Load and parse JD
    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = f.read()
    jd_info = parse_job_description(jd_path)
    jd_vec = vectorizer.transform([jd_text])

    results = []

    for file in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, file)

        # 1. Extract text
        resume_text = read_resume(file_path)

        # 2. Extract NLP features
        resume_info = extract_entities(resume_text)

        # 3. Rule-based score
        rule_score = score_resume(resume_info, jd_info)

        # 4. Semantic similarity score
        resume_vec = vectorizer.transform([resume_text])
        semantic_score = cosine_similarity(resume_vec, jd_vec)[0][0]

        # 5. Combine scores (60% rule-based, 40% semantic)
        final_score = 0.6 * rule_score + 0.4 * semantic_score

        results.append((file, final_score))

    # Sort by final score
    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results

def save_to_csv(results, output_path="output/ranked_candidates.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "score"])
        for name, score in results:
            writer.writerow([name, round(score, 2)])
    print(f"✅ Results saved to: {output_path}")

# Entry point
if __name__ == "__main__":
    ranked = rank_resumes()
    save_to_csv(ranked)

    print("\n📊 Ranked Candidates:")
    for name, score in ranked:
        print(f"{name}: {score:.2f}")
