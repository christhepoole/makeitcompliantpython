import numpy as np

import nltk
import os
from swiplserver import PrologMQI

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
            prologFacts.write(
                prologFactsReadOnly.read() + "license_a" + "(\"" + last_compare.replace(".txt", "") + "\").")

    return last_compare.replace(".txt", "")


def classify(file_a_string, file_b_string):
    last_compare_value = -1
    with os.scandir("license_templates") as template_files:
        for template_file in template_files:
            with open(template_file, "r", encoding="utf-8") as file:
                template_data = file.read()
                compare_value = cosine_similarity(file_a_string, template_data)
                if compare_value > last_compare_value:
                    last_compare_value = compare_value
                    last_compare_a = template_file.name
    last_compare_value = -1
    with os.scandir("license_templates") as template_files:
        for template_file in template_files:
            with open(template_file, "r", encoding="utf-8") as file:
                template_data = file.read()
                compare_value = cosine_similarity(file_b_string, template_data)
                if compare_value > last_compare_value:
                    last_compare_value = compare_value
                    last_compare_b = template_file.name

    # Prolog Linking
    with open("allLicenseFacts.pl", "w") as prologFacts:
        with open("allLicenseFactsBaseCopy.pl", "r") as prologFactsReadOnly:
            prologFacts.write(
                prologFactsReadOnly.read() + "license_a" + "(\"" + last_compare_a.replace(".txt", "") + "\").\n")
            prologFacts.write(
                prologFactsReadOnly.read() + "license_b" + "(\"" + last_compare_b.replace(".txt", "") + "\").\n")

    return [last_compare_a.replace(".txt", ""), last_compare_b.replace(".txt", "")]


def get_permissions():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult(\"allLicenseFacts.pl\").")

            license_a = prolog_thread.query("license_a_permission(X).")
            license_b = prolog_thread.query("license_b_permission(X).")
            if license_a is not False:
                permission_list_a = []
                for permission in license_a:
                    permission_list_a.append(permission['X'])
            else:
                permission_list_a = False

            if license_b is not False:
                permission_list_b = []
                for permission in license_b:
                    permission_list_b.append(permission['X'])
            else:
                permission_list_b = False

            return [permission_list_a, permission_list_b]


def get_conditions_for_distribution():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult(\"allLicenseFacts.pl\").")

            license_a = prolog_thread.query("license_a_conditions_before_distribution(X).")
            license_b = prolog_thread.query("license_b_conditions_before_distribution(X).")

            if license_a is not False:
                conditions_list_a = []
                for condition in license_a:
                    conditions_list_a.append(condition['X'])
            else:
                conditions_list_a = False

            if license_b is not False:
                conditions_list_b = []
                for condition in license_b:
                    conditions_list_b.append(condition['X'])
            else:
                conditions_list_b = False

            return [conditions_list_a, conditions_list_b]


def get_conditions_for_modification():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult(\"allLicenseFacts.pl\").")

            license_a = prolog_thread.query("license_a_conditions_before_modification(X).")
            license_b = prolog_thread.query("license_b_conditions_before_modification(X).")

            if license_a is not False:
                conditions_list_a = []
                for condition in license_a:
                    conditions_list_a.append(condition['X'])
            else:
                conditions_list_a = False

            if license_b is not False:
                conditions_list_b = []
                for condition in license_b:
                    conditions_list_b.append(condition['X'])
            else:
                conditions_list_b = False

            return [conditions_list_a, conditions_list_b]


def get_limitations():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult(\"allLicenseFacts.pl\").")

            license_a = prolog_thread.query("license_a_limitation(X).")
            license_b = prolog_thread.query("license_b_limitation(X).")

            if license_a is not False:
                limitation_list_a = []
                for limitation in license_a:
                    limitation_list_a.append(limitation['X'])
            else:
                limitation_list_a = False

            if license_b is not False:
                limitation_list_b = []
                for limitation in license_b:
                    limitation_list_b.append(limitation['X'])
            else:
                limitation_list_b = False

            return [limitation_list_a, limitation_list_b]


def query(query):
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult(\"allLicenseFacts.pl\").")
            return prolog_thread.query(query)


def define(prolog_fact_header):
    if prolog_fact_header == "can_use_commercially":
        return "You can use the software licensed under this license commercially"
    elif prolog_fact_header == "can_distribute":
        return "You can distribute the software licensed under this license without any additional conditions"
    elif prolog_fact_header == "can_modify":
        return "You can modify the software licensed under this license without any additional conditions"
    elif prolog_fact_header == "can_use_privately":
        return "You can use the software licensed under this license privately"
    elif prolog_fact_header == "patent_use":
        return "You can use the patent of the software licensed under this license"
    elif prolog_fact_header == "disclose_source_code":
        return "When distributing the software licensed under this license, you must disclose the source code"
    elif prolog_fact_header == "copyright_license_with_source_code":
        return "You must include a copy of this license and copyright notice with the source code when distributing " \
               "software licensed under this license"
    elif prolog_fact_header == "copyright_license_with_binaries":
        return "You must include a copy of this license and copyright notice with the binaries when distributing " \
               "software licensed under this license"
    elif prolog_fact_header == "network_use_is_distribution":
        return "Users who interact with the licensed software over a network should be able to obtain a copy of the " \
               "source code"
    elif prolog_fact_header == "same_license":
        return "Any modifications of the licensed code must be distributed under the same license. With some " \
               "licenses, a similar license is acceptable"
    elif prolog_fact_header == "same_license_modded_files":
        return "Any modifications of existing files must be distributed under the same license. With some " \
               "licenses, a similar license is acceptable"
    elif prolog_fact_header == "same_license_library":
        return "Any modifications of the licensed code must be distributed under the same license. With some " \
               "licenses, a similar license is acceptable, or may not apply for software that uses the licensed " \
               "software as a library"
    elif prolog_fact_header == "document_changes":
        return "You must document any changes you make to the licensed software"
    elif prolog_fact_header == "liability":
        return "The license includes a limitation of liablity"
    elif prolog_fact_header == "l_patent_use":
        return "You can't use the patent of the software licensed under this license"
    elif prolog_fact_header == "warranty":
        return "No warranty is provided"
    elif prolog_fact_header == "trademark_use":
        return "You can't use the trademark of the software licensed under this license"
    else:
        return False
