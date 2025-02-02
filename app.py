from fastapi import FastAPI, HTTPException
import uvicorn
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load the saved model
with open("saved_model.pkl", "rb") as f:
    model = pickle.load(f)

class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # Add other features as needed

@app.get("/")
def home():
    return ("Hello from the API")

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        data = np.array([[input_data.feature1, input_data.feature2, input_data.feature3]])
        # Add other features as needed
        prediction = model.predict(data)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)