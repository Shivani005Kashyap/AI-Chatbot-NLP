import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def create_model(input_size, output_size):
    model = Sequential([
        Dense(128, activation="relu", input_shape=(input_size,)),
        Dense(64, activation="relu"),
        Dense(output_size, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model