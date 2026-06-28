import json
import numpy as np
import joblib

from nltk_utils import tokenize, stem, bag_of_words
from model import create_model

# Load intents (FIX encoding issue)
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

all_words = []
tags = []
xy = []

# -----------------------------
# PREPROCESS INTENTS (FIXED)
# -----------------------------
for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        w = tokenize(pattern)
        w = [stem(word) for word in w]   # IMPORTANT FIX

        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ["?", "!", ".", ","]

# Stem vocabulary
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

tags = sorted(set(tags))

# -----------------------------
# Training data
# -----------------------------
X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    y_train.append(tags.index(tag))

X_train = np.array(X_train)
y_train = np.array(y_train)

print("Vocabulary size:", len(all_words))
print("Classes:", len(tags))
print("Training samples:", len(X_train))

# -----------------------------
# MODEL
# -----------------------------
model = create_model(
    input_size=X_train.shape[1],
    output_size=len(tags)
)

# -----------------------------
# TRAIN
# -----------------------------
model.fit(
    X_train,
    y_train,
    epochs=200,
    batch_size=8,
    verbose=1
)

# -----------------------------
# SAVE
# -----------------------------
model.save("chatbot_model.keras")
joblib.dump(all_words, "words.pkl")
joblib.dump(tags, "tags.pkl")

print("✅ Training complete!")