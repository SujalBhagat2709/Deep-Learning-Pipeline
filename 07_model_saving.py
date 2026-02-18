from tensorflow.keras.models import load_model

model = load_model("trained_model.h5", compile=False)

model.save("final_deep_learning_model.h5")

print("Final model saved successfully")