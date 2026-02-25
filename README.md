# End-to-End ML System (Pass Prediction API)

## 📌 Problem Statement
Predict whether a student will pass based on study hours.

---

## 🧠 System Architecture

Training Pipeline:
Data → Preprocess → Train Model → Save Artifact (model.pkl)

Inference Pipeline:
API Request → Preprocess → Load Model → Predict → JSON Response

Training and inference are separated to avoid retraining during requests.

---

## 📁 Project Structure

project-1-ml-system/
│
├── data/              # Training dataset
├── src/
│   ├── train.py       # Training pipeline
│   ├── predict.py     # Inference logic
│
├── api/
│   └── main.py        # FastAPI server
│
├── model.pkl          # Saved model artifact
├── requirements.txt
├── Dockerfile
└── README.md

---

## ⚙️ How to Run Locally

1. Install dependencies: ```pip install -r requirements.txt```
2. Train model: ```python src/train.py```
3. Start API: ```uvicorn api.main:app --reload```
4. Test: ```http://127.0.0.1:8000/predict?hours=6```


---

## 🐳 Run with Docker

Build: ```docker build -t ml-app```
Run: ```docker run -p 80:80 ml-app```
Test:```http://localhost/predict?hours=6```


---

## 🏗 Engineering Principles Applied

- Clear separation between training and inference
- Model saved as artifact (`model.pkl`)
- Input validation implemented
- Consistent feature formatting between training and prediction
- No hidden global state
- Dockerized for reproducibility
- Dependency management using `requirements.txt`

---

## 🧪 Example Prediction Logic

The model is trained using Logistic Regression on a simple tabular dataset.  
Input: number of study hours  
Output: 0 (Fail) or 1 (Pass)

---

## 🚀 Future Improvements

- Add automated unit tests
- Add model versioning
- Add logging and monitoring
- Deploy to cloud (AWS/GCP/Azure)
- Replace synthetic dataset with real-world dataset

---

## 🎯 Purpose of This Project

This project demonstrates:

- Understanding of ML system design
- Artifact-based model management
- API deployment of ML models
- Containerization with Docker
- Clean, modular architecture

It is intentionally simple in modeling but strong in engineering discipline.