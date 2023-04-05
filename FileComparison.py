import numpy as np

import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_text(textstring):
    punctuation = string.punctuation
    remove_punctuation = dict((ord(char), None) for char in punctuation)
    return nltk.word_tokenize(textstring.lower().translate(remove_punctuation))


vectorizer = TfidfVectorizer(use_idf=True, tokenizer=preprocess_text, stop_words="english")


def cosine_similarity(file_a, file_b):
    tfidf = vectorizer.fit_transform([file_a, file_b])
    return ((tfidf * tfidf.T).toarray())[0, 1]


def jaccard_similarity(file_a, file_b):
    set_a = set(file_a.split())
    set_b = set(file_b.split())
    intersection = set_a.intersection(set_b)
    return float(len(intersection)/(len(set_a) + len(set_b) - len(intersection)))


def file_to_string(filename):
    file = open(filename, encoding="utf8")
    file_list = file.readlines()
    text = ""
    for i in file_list:
        text += i + " "
    return text

