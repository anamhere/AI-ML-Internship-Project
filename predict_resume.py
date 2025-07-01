import pickle

# Step 1: Load the saved classifier model
with open("models/classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Step 2: Define new resume features:
# Example: 3 skills matched, education matched (1), 4 years experience
new_resume_features = [[3, 1, 4]]

# Step 3: Predict fit (1 = fit, 0 = not fit)
prediction = model.predict(new_resume_features)

print("Prediction (1 = fit, 0 = not fit):", prediction[0])
