import json
import numpy as np
import joblib

from nltk_utils import tokenize, stem, bag_of_words
from model import create_model 

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

all_words = []
tags = []
xy = []

# Read intents
for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

# Ignore punctuation
ignore_words = ["?", "!", ".", ","]

# Stem words
all_words = sorted(set([stem(w) for w in all_words if w not in ignore_words]))
tags = sorted(set(tags))

# Training data
X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

print("Vocabulary:", len(all_words))
print("Classes:", len(tags))
print("Training Samples:", len(X_train))

print("\nShape of X:", X_train.shape)
print("Shape of y:", y_train.shape)

# -----------------------------
# Create Neural Network
# -----------------------------
model = create_model(
    input_size=X_train.shape[1],
    output_size=len(tags)
)

# -----------------------------
# Train Model
# -----------------------------
model.fit(
    X_train,
    y_train,
    epochs=200,
    batch_size=8,
    verbose=1
)

# -----------------------------
# Save Model
# -----------------------------
model.save("chatbot_model.keras")

# Save vocabulary and tags
joblib.dump(all_words, "words.pkl")
joblib.dump(tags, "tags.pkl")

print("\n✅ Model trained successfully!")
print("✅ chatbot_model.keras saved")
print("✅ words.pkl saved")
print("✅ tags.pkl saved")