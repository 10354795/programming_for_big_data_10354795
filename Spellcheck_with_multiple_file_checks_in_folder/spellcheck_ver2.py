
# mistasdas

import os

# Must use '/' in folder names as '\' is an escape character, e.g. \n to advance a line 
# C:\Users\Family\Dropbox\DBS Data analytics course\Programming for big data\Spellchecker
# os.chdir('c:/users/10354795/downloads')
#C:\Users\Tom\Dropbox\DBS Data analytics course\Programming for big data\Spellchecker

os.chdir('c:/users/family/Dropbox/DBS Data analytics course/Programming for big data/Spellchecker')


# to begin we start with a list of words in a file called spell.words

# words = open("spell.words").readlines()

# print (words) # this prints a list of all the words in the file

# we read the file and then strip out the file endings
# Lambda is used like a function. It calls a method (strip() and aplies it toall the words.)

#words = map(lambda x: x.strip(), words)


class SpellChecker(object):  # set up a class for spell checker
    def __init__(self):
        self.words = []
 
# create a function to load the words
# we read the file and then strip out the file endings
# Lambda is used like a function. It calls a method (strip() and aplies it toall the words.)

# Read in file  and strip it
 
    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return map(lambda x: x.strip().lower(), lines)  # .lower() converts all words to lower case
 
# Create words list
 
    def load_words(self, file_name):
        self.words = self.load_file(file_name)
 
# Create a function to check a word (singular)
 
    def check_word(self, word):
#        return word in self.words
# remove full stops and ensure lower case 2 bugs fixed
        return word.strip('.').lower() in self.words
     
# Create a function to check words in a sentence
 
    def check_words(self, sentence, line_number = 0):
        words_to_check = sentence.split(' ')
        failed_words = []   # Setup an array to capture failed words
        caret_position = 0
        for word in words_to_check:
            if not self.check_word(word):
#                print('Word is misspelt : ' + word + ' on line ' + str(line_number+1) + ' pos ' + str(caret_position+1))
                failed_words.append({'word':word, 'line': line_number+1, 'pos': caret_position+1}) # append failed words to array and record line number and caret position
            caret_position = caret_position + len(word) + 1   
        return failed_words
 
    def check_multiple_words(self, sentence):
        words_to_check = sentence.split(' ')
        failed_words = []   # Setup an array to capture failed words
        for word in words_to_check:
            if not self.check_word(word):
                 print('Word is misspelt : ' + word)
                 failed_words.append(word)
        return failed_words
 
    def check_document(self, file_name):
        print ('This is the file name being checked > ',file_name)
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for sentence in self.sentences:
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        return failed_words_in_sentences
 
# Add function to check a number of files in a folder.
   
    def check_files_in_directory(self):
        basepath = ('c:/users/family/Dropbox/DBS Data analytics course/Programming for big data/Spellchecker/files/')
        for fname in os.listdir(basepath):
            file_name = fname
            print ('This is the file name being checked > ',file_name)
            self.sentences = self.load_file(file_name)
            failed_words_in_sentences = []
            index = 0
            for sentence in self.sentences:
                failed_words_in_sentences.extend(self.check_words(sentence, index))
                index = index + 1
                continue
        return failed_words_in_sentences

#        return failed_words_in_sentences 

# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
 
# Instantiate the functions in Class "SpellChecker()"
# enable functions so that this is only called when the script run from the command line
 
    spellChecker = SpellChecker()
    spellChecker.load_words('spell.words')
    print(spellChecker.check_word('misdasdas'))
    print(spellChecker.check_words('zygotic misdasdas elementary'))