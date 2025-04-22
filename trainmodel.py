import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("Salary_Data.csv")

X = df[["YearsExperience"]]  
y = df["Salary"]

# Model eğitimi
model = LinearRegression()
model.fit(X, y)

# Modeli kaydet
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model başarıyla eğitildi ve kaydedildi.")

