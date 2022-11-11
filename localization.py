import json
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + "/Lang/"

LOCALE = "de"

def load_localization():
    with open(PATH + "{}.json".format(LOCALE), 'r', encoding='utf-8') as file:
        return json.load(file)

LOCALIZATION = load_localization()

def t(key):
    try:
        value = LOCALIZATION[key]
        return value
    except:
        return key
