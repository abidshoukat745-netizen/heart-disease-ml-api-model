from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel

model = joblib.load('heart_disease_model.pkl')

app = FastAPI()

class InputData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int



@app.post("/predict")
def predict_heart_disease(input_data: InputData):
    prediction = model.predict([list(input_data.dict().values())])
    return {"prediction": int(prediction[0])}
