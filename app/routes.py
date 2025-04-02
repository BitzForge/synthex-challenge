from fastapi import APIRouter, HTTPException, Query
from app.models import PredictionInput
from app.services import predict_number

router = APIRouter()

@router.get("/predict")
def predict_get(x: float = Query(..., description="Numeric input for prediction")):
    try:
        return predict_number(x)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

@router.post("/predict")
def predict_post(input_data: PredictionInput):
    try:
        return predict_number(input_data.x)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
