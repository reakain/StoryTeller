import nltk
import random

TEXT = nltk.corpus.gutenberg.words('austen-emma.txt')

# NLTK shortcuts :)
bigrams = nltk.bigrams(TEXT)
cfd = nltk.ConditionalFreqDist(bigrams)

# pick a random word from the corpus to start with
word = random.choice(TEXT)
# generate 15 more words
for i in range(15):
    print(word),
    if word in cfd:
        key_list = cfd[word].keys()
        word = random.choice(list(key_list))
    else:
        break
