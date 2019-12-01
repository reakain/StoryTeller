#Storyteller/bots/inputparser.py
import logging
import inflect

logger = logging.getLogger()
inflector = inflect.engine()

class InputParser(object):
    def __init__(self):

    def has_word(self, input_text, word):
        keywords = [word]
        return any(keyword in input_text for keyword in keywords)

    def has_number(self, input_text, number):
        word_num = inflector.word_to_number(number)
        keywords = [number, word_num]

        return any(keyword in input_text for keyword in keywords)

