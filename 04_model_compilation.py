from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam

model = load_model("model_structure.h5")

model.compile(
    optimizer=Adam(learning_rate=0.01),
    loss="mse",
    metrics=["mae"]
)

model.save("compiled_model.h5")
print("Model compiled")