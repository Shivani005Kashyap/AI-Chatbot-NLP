from nltk_utils import tokenize, stem

sentence = "Hello! I am learning NLP."

tokens = tokenize(sentence)
print(tokens)

print(stem("Playing"))
print(stem("Running"))
print(stem("Studies"))