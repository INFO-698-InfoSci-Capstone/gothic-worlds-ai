import joblib
import os

def load_model_and_vectorizer():
    model = joblib.load(os.path.join('models', 'iw_deception_score_model.pkl'))
    vectorizer = joblib.load(os.path.join('models', 'iw_deception_score_vectorizer.pkl'))
    return model, vectorizer
