import os, sys, eel, FileComparison
from swiplserver import PrologMQI

class Compare:
    def __init__(self, name, value):
        self.name = name
        self.value = value

eel.init("web")

@eel.expose
def compare(sent_files):
    return_values = []
    files = sent_files
    compare_value = str(100*(FileComparison.cosine_similarity(files[0]['data'], files[1]['data'])))
    return_values.append(Compare("", compare_value).__dict__)
    return return_values

@eel.expose
def classify(sent_file):
    return_values = []
    last_compare_value = -sys.maxsize - 1
    last_compare = Compare("", "")
    with os.scandir("license_templates") as template_files:
        for template_file in template_files:
            with open(template_file.path, "r", encoding="utf-8") as file:
                template_data = file.read()
                compare_value = FileComparison.cosine_similarity(sent_file['data'], template_data)
                if(compare_value > .95):
                    if(compare_value > last_compare_value):
                        last_compare_value = compare_value
                        last_compare = Compare(template_file.name, str(compare_value))
    return_values.append(last_compare.__dict__)
    return return_values

eel.start("upload.html")