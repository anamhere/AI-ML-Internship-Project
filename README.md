# AI-ML-Internship-Project
🚀 AI Resume Screening & Ranking Tool

An intelligent AI-powered Resume Screening System that automatically ranks resumes based on a given job description using NLP, Machine Learning, and Semantic Similarity.

📌 Features
📄 Resume parsing (PDF/Text)
🧠 NLP-based entity extraction (skills, experience, etc.)
📊 Rule-based scoring system
🔍 Semantic similarity using TF-IDF + Cosine Similarity
🏆 Automatic resume ranking
⚡ Fast and scalable processing
🛠️ Tech Stack
Language: Python
Libraries: spaCy, scikit-learn, NumPy, pandas
NLP: spaCy (en_core_web_sm)
ML: TF-IDF Vectorizer + Cosine Similarity
File Handling: PDF/Text parsing
📂 Project Structure
resume_screening_tool/
│── resumes/                  # Folder containing resumes
│── job_description.txt       # Job description input
│── rank_resumes.py           # Main ranking script
│── predict_resume.py         # Prediction script
│── utils.py                  # Helper functions (NLP, scoring)
│── fit_vectorizer.py         # Train TF-IDF model
│── train_classifier.py       # ML model training (optional)
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-screening-tool.git
cd resume-screening-tool
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install spaCy Model
python -m spacy download en_core_web_sm
▶️ How to Run
Step 1: Add Resumes
Put all resumes inside the resumes/ folder
Step 2: Add Job Description
Update job_description.txt with your JD
Step 3: Run Ranking Script
python rank_resumes.py
🧠 How It Works
Text Extraction
Reads resumes and job description
Entity Extraction
Extracts skills, experience using spaCy NLP
Rule-Based Scoring
Matches keywords, skills, and experience
Semantic Similarity
Uses TF-IDF + Cosine Similarity
Final Ranking
Combines scores to rank candidates
📊 Example Output
1. resume_1.pdf → Score: 0.87
2. resume_2.pdf → Score: 0.79
3. resume_3.pdf → Score: 0.65
🚀 Future Enhancements
🔥 BERT/Transformer-based matching
📊 Dashboard (Streamlit / Web App)
📎 Support for DOCX files
🤖 AI-powered skill gap analysis
☁️ Deployment on cloud
💡 Use Cases
HR Resume Screening
Internship Selection Automation
Campus Hiring Systems
Recruitment Platforms
👨‍💻 Author

Anam Singh

💼 Aspiring Software Developer & AI Engineer
🚀 Passionate about AI, NLP & Backend Development
⭐ Contribute

Feel free to fork this repo and improve it!
Pull requests are welcome 🚀
