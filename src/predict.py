import pickle
import pandas as pd

def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict(model, hours):
    X = pd.DataFrame([[hours]], columns = ["hours"])
    prediction = model.predict(X)
    return prediction[0]