import pandas as pd
from tensorflow.keras.models import load_model

X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv")

model = load_model("trained_model.h5", compile=False)

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mse"]
)

loss, mae = model.evaluate(X_test, y_test)

print("Test Loss:", loss)
print("Test MAE:", mae)