from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(16, activation="relu", input_shape=(3,)))
model.add(Dense(8, activation="relu"))
model.add(Dense(1))

model.summary()

model.save("model_structure.h5")