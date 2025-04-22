import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Veri: sadece YearsExperience ve Salary var
df = pd.read_csv("Salary_Data.csv")

# Özellik ve hedef değişken
X = df[["YearsExperience"]]  # 👈 dikkat! çift köşeli olmalı
y = df["Salary"]

# Model eğitimi
model = LinearRegression()
model.fit(X, y)

# Modeli kaydet
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model başarıyla eğitildi ve kaydedildi.")

