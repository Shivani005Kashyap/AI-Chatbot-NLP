import random
import json
import numpy as np
import joblib
import tensorflow as tf
import re
from nltk_utils import tokenize, bag_of_words

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

model = tf.keras.models.load_model("chatbot_model.keras")
words = joblib.load("words.pkl")
tags = joblib.load("tags.pkl")

intent_map = {i["tag"]: i for i in intents["intents"]}

def extract_name(text):
    match = re.search(r"i am (.+)|my name is (.+)", text, re.I)
    if match:
        return (match.group(1) or match.group(2)).strip()
    return None

def get_response(sentence):
    try:
        sentence = sentence.lower()

        # ---------------- RULES ----------------
        name = extract_name(sentence)
        if name:
            return f"Hi {name}! Nice to meet you 👋"

        if "how are you" in sentence:
            return random.choice(["I'm good 😊", "Doing great!"])

        if "your name" in sentence:
            return "I'm your AI chatbot 🤖"

        if "time" in sentence:
            from datetime import datetime
            return datetime.now().strftime("%H:%M")

        # ---------------- ML MODEL ----------------
        sentence_words = tokenize(sentence)
        X = bag_of_words(sentence_words, words)
        X = np.array([X])

        prediction = model.predict(X, verbose=0)

        index = np.argmax(prediction)
        confidence = float(prediction[0][index])

        if confidence > 0.5:
            tag = tags[index]
            return random.choice(intent_map[tag]["responses"])

        # ---------------- FALLBACK ----------------
        return random.choice([
            "I’m not sure, can you explain?",
            "Interesting 🤔 tell me more",
            "I’m still learning..."
        ])

    except Exception as e:
        print("ERROR:", e)
        return "Bot error occurred"