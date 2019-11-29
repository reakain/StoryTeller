#QuestGiver/bots/questmaker.py
import logging
import inflect
from random import randint
import nltk
nltk.download('brown')
nltk.download('names')
nltk.download('wordnet')

logger = logging.getLogger()
inflector = inflect.engine()

class Request(object):
    def __init__(self):
        self.tagged_words = nltk.corpus.brown.tagged_words()
        self.verbs = [word for (word, tag) in self.tagged_words if tag == 'VB']
        self.nouns = [word for (word, tag) in self.tagged_words if tag == 'NN']
        self.adjs = [word for (word, tag) in self.tagged_words if tag == 'JJ']
        self.pnouns = [word for (word, tag) in self.tagged_words if tag == 'NP']
        self.preps = [word for (word,tag) in self.tagged_words if tag == 'IN']
        self.names = nltk.corpus.names.words('male.txt') + nltk.corpus.names.words('female.txt')
        self.names = list(set(self.names))

    def get_similar(self,word,pos):
        """ Returns a word or phrase similar to the word provided.

        Parameters:
            word (str): The word you want to get a similar string to

        Returns:
            similar_word (str): The string similar to "word".
        
        """
        syns = nltk.corpus.wordnet.synsets(word,pos)
        lemmas = syns[randint(0,len(syns)-1)].lemmas()
        similar_word = lemmas[randint(0,len(lemmas)-1)].name()
        similar_word = similar_word.replace("-"," ")
        similar_word = similar_word.replace("_"," ")

        return similar_word

    def get_verb(self):
        """ Returns the "verb" dialogue component between please and num.

        Returns:
            verb (str): The string denoting the verb section of quest dialogue.
        
        """
        val = randint(0,len(self.verbs)-1)
        return self.verbs[val]

    def get_adjective(self):
        """ Returns the adjective dialogue component between number and noun.

        Returns:
            adj (str): The string denoting the adjective section of quest dialogue.
        
        """
        val = randint(0,len(self.adjs)-1)
        return self.adjs[val]

    def get_noun(self):
        """ Returns the noun dialogue component between adjective and preposition.

        Returns:
            noun (str): The string denoting the noun section of quest dialogue.
        
        """
        val = randint(0,len(self.nouns)-1)
        return self.nouns[val]

    def get_preposition(self):
        """ Returns the preposition dialogue component between noun and proper noun.

        Returns:
            prep (str): The string denoting the preposition section of quest dialogue.
        
        """
        val = randint(0,len(self.preps)-1)
        return self.preps[val]

    def get_proper_noun(self):
        """ Returns the proper noun dialogue component at the end of the quest

        Returns:
            pnoun (str): The string denoting the proper noun section of quest dialogue.
        
        """
        val = randint(0,len(self.pnouns)-1)
        return self.pnouns[val]

    def get_name(self):
        """ Returns the proper noun dialogue component at the end of the quest

        Returns:
            name (str): The string denoting the proper noun section of quest dialogue.
        
        """
        val = randint(0,len(self.names)-1)
        return self.names[val]

    def generate_new_quest(self):
        """ Returns generated quest dialog.

        Format logic of returned string is always some form of greeting with then one of 
        multiple sentence structure options for the request itself.
            
        Example output:
            Greetings traveller,
            Could you please find for me three golden rocks of Lambert?

        Returns:
            quest (str): The string of complete quest dialogue to publish.
        
        """
        quest = self.get_similar("greetings",'n').capitalize() + ", "  \
            + self.get_similar("buddy",'n') + ".\n" \
            +self.get_similar("please",'r').capitalize() + " " \
            + self.get_request(randint(1,3))
        return quest

    def get_request(self,style):
        """ Switcher function for getting one of the different request styles

        Parameters:
            style (int): Which style of request to build

        Returns:
            method (): The specified method function is then called to run
        """
        method_name = 'request_'+str(style)
        method = getattr(self,method_name,lambda :'Invalid')
        return method()

    def request_1(self):
        """ Request style with form:
        [verb] for me [number] [adjective] [noun] [preposition] [proper noun]

        Returns:
            request (str): The string denoting the request portion of the dialogue.
    
        """
        val_amount = randint(1,100)
        num = inflector.number_to_words(val_amount)

        plural_noun = inflector.plural(self.get_noun(),val_amount)

        request = self.get_verb() + " for me " \
            + num + " " \
            + self.get_adjective() + " " \
            + plural_noun + " " \
            + self.get_preposition() + " " \
            + self.get_proper_noun() + "?"
        return request

    def request_2(self):
        """ Request style with form:
        get [noun], [noun], [noun], ..., and [noun] for me

        Returns:
            request (str): The string denoting the request portion of the dialogue.
    
        """
        val_amount = randint(2,8)

        nouns = []
        for x in range(val_amount):
            nouns.append(self.get_noun())
       
        nounlist = inflector.join(nouns)

        request = self.get_similar("get",'v') + " " \
            + nounlist + " for me."
        return request

    def request_3(self):
        """ Request style with form:
        kill [proper noun], [proper noun], ..., and [proper noun] for [pronoun]

        Returns:
            request (str): The string denoting the request portion of the dialogue.
    
        """
        val_amount = randint(2,8)

        nams = []
        for x in range(val_amount):
            nams.append(self.get_name())
       
        namelist = inflector.join(nams)

        request = self.get_similar("kill",'v') + " " \
            + namelist + " for me."
        return request



if __name__ == "__main__":
    quests = Request()
    for x in range(0,10):
        print(quests.generate_new_quest())
