#Storyteller/bots/storybuilder.py
from __future__ import unicode_literals
import logging
import inflect
from random import randint
import markovify
import re
import spacy
import codecs

logger = logging.getLogger()
inflector = inflect.engine()


class Storybuilder(object):
    def __init__(self):
        with codecs.open("source_text/robinhood.txt", encoding="utf-8") as f:
            text1 = repr(f.read())
        with codecs.open("source_text/kingarther.txt", encoding="utf-8") as f:
            text2 = f.read()
        with codecs.open("source_text/knights.txt", encoding="utf-8") as f:
            text3 = repr(f.read())
        with codecs.open("source_text/grimm.txt", encoding="utf-8") as f:
            text4 = repr(f.read())
        m_text1 = markovify.Text(text1)
        m_text2 = markovify.Text(text2)
        m_text3 = markovify.Text(text3)
        m_text4 = markovify.Text(text4)

        self.storyblock = markovify.combine([ m_text1, m_text2, m_text3, m_text4 ], [ 1, 1, 1, 1 ])
    
    def make_tweet(self):
        tweet = self.build_tweet()
        while(len(tweet) > 130):
            tweet = self.build_tweet()

        return tweet

    def build_tweet(self):
        tweet = self.storyblock.make_sentence_with_start("Once", strict=True, max_word=10)
        tweet += " " + self.get_sentence()
        tweet += " " + self.get_sentence()
        return tweet

    def get_sentence(self):
        sent = self.storyblock.make_short_sentence(40)
        while(sent == None):
            sent = self.storyblock.make_short_sentence(40)
        return sent

nlp = spacy.load("en_core_web_sm")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


if __name__ == "__main__":
    storybuilder = Storybuilder()
    tweet = storybuilder.make_tweet()
    print(len(tweet))
    print(tweet)
