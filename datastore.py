import random
class Datastore():
    def __init__(self):
        with open("dictionary.txt")as word_files:
            self.words= word_files.read().splitlines()
        print(self.words)
    

    def get_word(self):

        word=""
        while len(word)<3:
            word = random.choice(self.words)
        return word