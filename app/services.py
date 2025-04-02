import pickle
import numpy as np
from app.config import MODEL_PATH

# Load the pre-trained model
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

def predict_number(x: float):
    x_value = np.array([[x]])
    prediction = model.predict(x_value)[0]
    return {"prediction": float(prediction)}
