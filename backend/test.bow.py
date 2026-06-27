from nltk_utils import tokenize, bag_of_words

sentence = "Hello how are you"

words = ["hi", "hello", "i", "you", "bye", "thank", "cool", "how", "are"]

tokenized = tokenize(sentence)

bag = bag_of_words(tokenized, words)

print(tokenized)
print(bag)