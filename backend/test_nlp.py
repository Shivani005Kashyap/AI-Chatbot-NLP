from nltk_utils import tokenize, stem

sentence = "Hello! I am learning NLP."

tokens = tokenize(sentence)

# remove punctuation for cleaner output
tokens = [t for t in tokens if t.isalnum()]

print("Tokens:", tokens)

words_to_test = ["Playing", "Running", "Studies"]

for word in words_to_test:
    print(f"{word} -> {stem(word)}")