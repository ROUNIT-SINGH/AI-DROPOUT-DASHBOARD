import os
import xgboost as xgb
import pandas as pd
import shap

MODEL_PATH = os.path.join(os.path.dirname(__file__), "dropout_model.json")
model = None

def load_model():
    global model
    if model is None:
        model = xgb.XGBClassifier()
        if os.path.exists(MODEL_PATH):
            model.load_model(MODEL_PATH)
        else:
            # Fallback if model not trained yet
            pass
    return model

def get_dropout_risk(features: dict) -> float:
    m = load_model()
    if not os.path.exists(MODEL_PATH):
        # Fallback simple heuristic
        return 0.5
        
    df = pd.DataFrame([features])
    # Predict probability of dropout (class 1)
    prob = m.predict_proba(df)[0][1]
    return float(prob)

def get_shap_values(features: dict):
    m = load_model()
    if not os.path.exists(MODEL_PATH):
        return {}
    df = pd.DataFrame([features])
    explainer = shap.TreeExplainer(m)
    shap_values = explainer.shap_values(df)
    return {k: float(v) for k, v in zip(features.keys(), shap_values[0])}
