import json
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/Storage/"

def load_string(filename):
    with open(PATH + filename) as file:
        return json.load(file)

def load_dictionary(filename):
    with open(PATH + filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_string(filename, string):
    with open(PATH + filename) as file:
        file.write(string)
        
def save_dictionary(filename, dictionary):
    with open(PATH + filename, 'w', encoding='utf8') as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=False)
    