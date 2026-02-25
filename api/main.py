from fastapi import FastAPI
from src.predict import load_model,predict

app = FastAPI()

model = load_model()

@app.on_event("startup")
def load_model_on_startup():
    global model
    model = load_model()

@app.get("/predict")
def predict_endpoint(hours: float):
    if hours < 0:
        return {"error" : "Hours cannot be negative"}
    
    result = predict(model, hours)
    return {"prediction": int(result)}