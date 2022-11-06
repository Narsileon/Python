import os
import jsonserializer

LOCALE = "de"

DICTIONARY = jsonserializer.load_dictionary("{}.json".format(LOCALE))

def t(key):
    try:
        value = DICTIONARY[key]
        return value
    except:
        return key
