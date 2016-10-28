import re
import string
from nltk.corpus import stopwords

def remove_punctuation(s):
    "see http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python"
    table = string.maketrans("","")
    return s.translate(table, string.punctuation)

def remove_stop_words(words):
    return [word for word in words if word not in set(stopwords.words('english')) and len(word)>2]


def tokenize(text):
    text = remove_punctuation(text)
    text = text.lower()
    words = re.split("\W+", text)
    words = remove_stop_words(words)
    return words

def count_words(words):
    wc = {}
    for word in words:
        wc[word] = wc.get(word, 0.0) + 1.0
    return wc

if __name__ == '__main__':
    s = "Hello my name, is Greg. My favorite food is pizza."
    print count_words(tokenize(s))
        
