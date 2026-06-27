import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    tokenized_sentence = [stem(word) for word in tokenized_sentence]

    bag = np.zeros(len(words), dtype=np.float32)

    for idx, word in enumerate(words):
        if word in tokenized_sentence:
            bag[idx] = 1.0

    return bag