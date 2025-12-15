import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load artifacts
model = joblib.load("artifacts/complaint_classifier.pkl")
vectorizer = joblib.load("artifacts/tfidf_vectorizer.pkl")
label_encoder = joblib.load("artifacts/label_encoder.pkl")

# Optional: store some training complaints for similarity search
import pandas as pd
df_train = pd.read_csv("artifacts/sample_train_complaints.csv")  # Only a subset to save memory
tfidf_train = vectorizer.transform(df_train['Consumer complaint narrative'].fillna(''))


def predict_complaint(text: str):
    X = vectorizer.transform([text])
    
    # Predict category
    probs = model.predict_proba(X)[0]
    pred_idx = np.argmax(probs)
    category = label_encoder.inverse_transform([pred_idx])[0]
    confidence = float(probs[pred_idx])

    # Tiered urgency
    urgency = "NORMAL"
    if category in ["Debt collection", "Credit reporting"]:
        if confidence > 0.75:
            urgency = "HIGH"
        else:
            urgency = "MEDIUM"
    elif category in ["Other", "Vehicle loan or lease", "Money transfer / Virtual currency"]:
        urgency = "LOW"

    # Top keywords from TF-IDF
    feature_names = vectorizer.get_feature_names_out()
    top_indices = X.toarray()[0].argsort()[-5:][::-1]
    explanation_keywords = [feature_names[i] for i in top_indices]

    # Optional: Top 2 similar past complaints
    sims = cosine_similarity(X, tfidf_train)[0]
    top_sim_indices = sims.argsort()[-2:][::-1]
    similar_complaints = df_train.iloc[top_sim_indices]['Consumer complaint narrative'].tolist()

    return {
        "category": category,
        "urgency": urgency,
        "explanation_keywords": explanation_keywords,
        "similar_complaints": similar_complaints
    }