# train_classifier.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Step 1: Sample training data (features and labels)
data = [
    {"skills": 4, "education": 1, "experience": 5, "label": 1},  # Good fit
    {"skills": 2, "education": 0, "experience": 1, "label": 0},  # Poor fit
    {"skills": 5, "education": 1, "experience": 6, "label": 1},  # Good fit
    {"skills": 1, "education": 0, "experience": 2, "label": 0},  # Poor fit
    {"skills": 3, "education": 1, "experience": 4, "label": 1}   # Good fit
]

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Separate features (X) and label (y)
X = df[["skills", "education", "experience"]]
y = df["label"]

# Step 4: Train the model
model = LogisticRegression()
model.fit(X, y)

# Step 5: Save model to models/classifier.pkl
os.makedirs("models", exist_ok=True)  # Ensure models/ directory exists
with open("models/classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as models/classifier.pkl")
