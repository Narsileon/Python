import json
import os

storage_path = os.path.dirname(os.path.realpath(__file__)) + "/Storage/"

def load_string(filename):
    with open(storage_path + filename) as file:
        return json.load(file)

def load_dictionary(filename):
    with open(storage_path + filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_string(filename, string):
    with open(storage_path + filename) as file:
        file.write(string)
        
def save_dictionary(filename, dictionary):
    with open(storage_path + filename, 'w', encoding='utf8') as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=False)
    