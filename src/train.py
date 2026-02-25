import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# 1. Load data
data = pd.read_csv("data/data.csv")

X = data[["hours"]]
y = data["pass"]

# 2. Train model
model = LogisticRegression()
model.fit(X, y)

# 3. Save model (ARTIFACT)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")