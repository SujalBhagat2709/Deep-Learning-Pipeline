import pandas as pd
from tensorflow.keras.models import load_model

X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv")

model = load_model("compiled_model.h5", compile=False)

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mse"]
)

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=4,
    verbose=1
)

model.save("trained_model.h5")
print("Model training completed")