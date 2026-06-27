import random
import json
import numpy as np
import joblib
import tensorflow as tf

from nltk_utils import tokenize, bag_of_words

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# Load trained model
model = tf.keras.models.load_model("chatbot_model.keras")

# Load vocabulary and tags
words = joblib.load("words.pkl")
tags = joblib.load("tags.pkl")


def get_response(sentence):
    # Tokenize the input
    sentence = tokenize(sentence)

    # Convert to Bag of Words
    X = bag_of_words(sentence, words)
    X = np.array([X])

    # Predict intent
    prediction = model.predict(X, verbose=0)

    predicted_index = np.argmax(prediction)
    confidence = prediction[0][predicted_index]
    tag = tags[predicted_index]

    # Return a response if confidence is high enough
    if confidence > 0.7:
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand. Can you rephrase?"


# This part runs ONLY when predict.py is executed directly
if __name__ == "__main__":
    print("🤖 AI Chatbot is ready!")
    print("Type 'quit' to exit.\n")

    while True:
        message = input("You: ")

        if message.lower() == "quit":
            print("Bot: Goodbye!")
            break

        response = get_response(message)
        print("Bot:", response)
        