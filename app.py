from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/")
def home():
    return ("Hello from the API")

# @app.get("/predict")
# def predict():
    

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port= 8000)