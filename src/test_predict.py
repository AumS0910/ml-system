from predict import load_model, predict

model = load_model()

result = predict(model, 6)
print(result)