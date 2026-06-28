import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return word_tokenize(sentence.lower())

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(words), dtype=np.float32)

    words = [stem(w) for w in words]

    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1.0

    return bag