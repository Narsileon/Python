import os
import jsonserializer

LOCALE = "de.json"

DICTIONARY = jsonserializer.load_dictionary(LOCALE)

def t(key):
    return DICTIONARY[key]
