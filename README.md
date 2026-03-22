# 🤖 AI-Based Resume Screening Tool

An intelligent resume screening system that uses **NLP**, **spaCy NER**, and **TF-IDF** to automatically extract skills, education, and experience from PDF resumes — and ranks candidates against a job description using a weighted scoring algorithm.

---

## 📌 Project Overview

This tool was built as part of an AI/ML internship project at **Mishka Tech**. It solves the problem of manually reviewing hundreds of resumes by automating:

- **Entity extraction** from PDF resumes (skills, education, experience)
- **Candidate scoring** against a given job description
- **Ranked output** of candidates from most to least suitable

---

## 🗂️ Folder Structure

```
resume_screening_tool/
├── resumes/                  # Input PDF resumes
├── models/
│   ├── classifier.pkl        # Trained classifier model
│   └── vectorizer.pkl        # Fitted TF-IDF vectorizer
├── output/                   # Ranked results output
├── venv/                     # Virtual environment
├── fit_vectorizer.py         # Fits and saves TF-IDF vectorizer
├── main.py                   # Main entry point
├── predict_resume.py         # Predicts score for a single resume
├── rank_resumes.py           # Ranks all resumes in /resumes folder
├── job_description.txt       # Job description input file
├── utils.py                  # Helper functions (scoring, extraction)
└── README.md
```

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| NLP | spaCy, NLTK |
| ML | scikit-learn (TF-IDF, cosine similarity) |
| PDF Parsing | pdfminer.six |
| Model Persistence | pickle |
| Entity Extraction | Named Entity Recognition (NER) |

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/anamhere/AI-ML-Internship-Project.git
cd AI-ML-Internship-Project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download spaCy language model

```bash
python -m spacy download en_core_web_sm
```

---

## 🧠 How It Works

### Step 1 — PDF Parsing
Resumes in PDF format are parsed using `pdfminer.six` to extract raw text.

### Step 2 — Entity Extraction (NER)
spaCy's Named Entity Recognition model extracts structured information:
- **SKILL** — e.g., Python, Machine Learning, FastAPI
- **EDUCATION** — e.g., B.Tech, Computer Science
- **EXPERIENCE** — e.g., 2 years, 3+ years

### Step 3 — TF-IDF Vectorization
The extracted resume text and job description are vectorized using a fitted **TF-IDF vectorizer** (`vectorizer.pkl`) to convert text into numerical feature vectors.

### Step 4 — Weighted Scoring Algorithm
Each candidate is scored using a weighted formula:

```
final_score = (0.5 × skill_overlap) + (0.3 × experience_score) + (0.2 × education_match)
```

| Component | Weight | Description |
|---|---|---|
| Skill Overlap | 50% | Ratio of matched skills to required skills |
| Experience Score | 30% | Normalized years of experience (max 5 years = 1.0) |
| Education Match | 20% | Binary match of education level (0 or 1) |

### Step 5 — Ranking
All candidates are ranked by `final_score` in descending order and the output is saved to the `/output` folder.

---

## ▶️ Usage

### 1. Add your job description

Edit `job_description.txt` with the role requirements:

```
Looking for a Python developer with experience in Machine Learning,
NLP, and FastAPI. B.Tech in Computer Science preferred.
```

### 2. Add resumes

Place candidate PDF resumes inside the `resumes/` folder.

### 3. Fit the vectorizer (first time only)

```bash
python fit_vectorizer.py
```

### 4. Rank all resumes

```bash
python rank_resumes.py
```

### 5. Predict score for a single resume

```bash
python predict_resume.py --resume resumes/candidate.pdf
```

---

## 📊 Sample Output

```
Rank | Candidate         | Score
-----|-------------------|-------
  1  | john_doe.pdf      | 0.87
  2  | jane_smith.pdf    | 0.74
  3  | raj_kumar.pdf     | 0.61
  4  | alice_brown.pdf   | 0.45
```

---

## 📦 Requirements

Create a `requirements.txt` with:

```
spacy==3.7.2
scikit-learn==1.3.0
pdfminer.six==20221105
nltk==3.8.1
```

---

## 🔮 Future Improvements

- Add a Streamlit web interface for uploading resumes and JD
- Integrate a custom-trained spaCy NER model for better entity extraction
- Support DOCX resume format in addition to PDF
- Add email notification for top-ranked candidates
- Export ranked results to Excel/CSV

---

## 👩‍💻 Author

**Anam Singh**
AI/ML Intern — Mishka Tech
[LinkedIn](https://linkedin.com/in/anam-singh-142182231) | [GitHub](https://github.com/anamhere)

---

## 📄 License

This project is licensed under the MIT License.
