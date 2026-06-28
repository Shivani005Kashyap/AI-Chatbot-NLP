import random
import json
import re
from nltk_utils import tokenize, bag_of_words

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

# Temporarily disable ML model
model = None
words = []
tags = []

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
            return random.choice([
                "I'm good 😊",
                "Doing great!",
                "I'm doing well!"
            ])

        if "your name" in sentence:
            return "I'm your AI chatbot 🤖"

        if "time" in sentence:
            from datetime import datetime
            return datetime.now().strftime("%H:%M")

        if "hello" in sentence or "hi" in sentence:
            return random.choice([
                "Hello! 👋",
                "Hi there!",
                "Hey! How can I help you?"
            ])

        if "bye" in sentence:
            return "Goodbye! Have a great day! 😊"

        # ---------------- FALLBACK ----------------

        return random.choice([
            "I'm still learning. Can you explain differently?",
            "Interesting 🤔 Tell me more!",
            "Sorry, I don't know the answer to that yet.",
            "Could you rephrase your question?"
        ])

    except Exception as e:
        print("ERROR:", e)
        return "Bot error occurred."
