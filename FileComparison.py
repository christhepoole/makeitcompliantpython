import numpy as np

import nltk
import os

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


def file_to_string(filename):
    file = open(filename, encoding="utf8")
    file_list = file.readlines()
    text = ""
    for i in file_list:
        text += i + " "
    return text


def classify(file_string):
    last_compare_value = -1
    with os.scandir("license_templates") as template_files:
        for template_file in template_files:
            with open(template_file, "r", encoding="utf-8") as file:
                template_data = file.read()
                compare_value = cosine_similarity(file_string, template_data)
                if compare_value > last_compare_value:
                    last_compare_value = compare_value
                    last_compare = template_file.name

    # Prolog Linking
    with open("allLicenseFacts.pl", "w") as prologFacts:
        with open("allLicenseFactsBaseCopy.pl", "r") as prologFactsReadOnly:
            prologFacts.write(prologFactsReadOnly.read() + "license_a(\"" + last_compare.replace(".txt", "") + "\").")

    return last_compare.replace(".txt", "")
