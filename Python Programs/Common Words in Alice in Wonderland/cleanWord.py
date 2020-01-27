# module to remove extra characters from words that show up in typical English text.
import string

def clean(word):
        # convert whole word to lower case
        word = word.lower()
        # trim off punctuation at the end and beginning
        word = word.strip(string.punctuation)
        return word
