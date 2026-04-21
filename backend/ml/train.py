import os
import xgboost as xgb
import pandas as pd
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "dropout_model.json")

def train_dummy_model():
    """Trains a dummy XGBoost model and saves it."""
    # Synthetic data
    np.random.seed(42)
    n_samples = 1000
    
    # Features
    attendance_rate = np.random.uniform(0.5, 1.0, n_samples)
    gpa = np.random.uniform(1.0, 4.0, n_samples)
    financial_aid = np.random.randint(0, 2, n_samples)
    failed_courses = np.random.randint(0, 5, n_samples)
    extracurricular = np.random.randint(0, 2, n_samples)
    
    X = pd.DataFrame({
        "attendance_rate": attendance_rate,
        "gpa": gpa,
        "financial_aid": financial_aid,
        "failed_courses": failed_courses,
        "extracurricular_activities": extracurricular
    })
    
    # Target (1 = Dropout, 0 = Retained)
    # Higher risk if attendance is low, gpa is low, failed courses are high
    risk_score = (1.0 - attendance_rate) * 2 + (4.0 - gpa) * 0.5 + failed_courses * 0.2
    y = (risk_score > 1.5).astype(int)
    
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X, y)
    model.save_model(MODEL_PATH)
    print(f"Model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_dummy_model()
