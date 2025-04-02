from pydantic import BaseModel

class PredictionInput(BaseModel):
    x: float
