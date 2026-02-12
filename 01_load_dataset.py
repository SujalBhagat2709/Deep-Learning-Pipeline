import pandas as pd

df = pd.read_csv("dataset.csv")

print("Dataset loaded")
print("Shape:", df.shape)
print("\nSample rows:")
print(df.head())

df.to_csv("step1_loaded.csv", index=False)