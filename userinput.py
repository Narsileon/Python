from datetime import datetime
from decimal import Decimal

ErrorMessage = "Bitte geben Sie eine gültige Antwort. "

def get_string(question, minLen = 3, maxLen = 255):
    while True:
        try:
            value = str(input(question))
        except ValueError:
            print(ErrorMessage)
            continue
        if (minLen <= len(value) <= maxLen):
            return value
        else:
            print(ErrorMessage + "Die Antwort muss zwischen {} und {} Zeichen lang sein".format(minLen, maxLen))
            continue
        
def get_int(question, minValue = -9223372036854775808, maxValue = 9223372036854775807):
    while True:
        try:
            value = int(input(question))
        except ValueError:
            print(ErrorMessage)
            continue
        if (minValue <= value <= maxValue):
            return value
        else:
            print(ErrorMessage + "Die Antwort muss zwischen {} und {} liegen.".format(minValue, maxValue))
            continue  

def get_bool(question):
    while True:
        try:
            value = str(input(question + " (Ja/Nein)? "))
        except ValueError:
            print(ErrorMessage)
        if (value == "Ja" or value == "ja"):
            return True
        if (value == "Nein" or value == "nein"):
            return False
        else:
            print(ErrorMessage)
            continue

def get_date(question):
    while True:
        try:
            value = str(input(question + " (01.01.2000): "))
            day, month, year = map(int, value.split('.'))
            datum = datetime(year, month, day)
        except ValueError:
            print(ErrorMessage)
            continue
        else:
            return datum
        
def get_choice(question, options):
    print(question)

    for x, element in enumerate(options):
        print("  {}) {}".format(x + 1, element))

    return options[get_int("  => Auswahl (Nummer): ", 1, len(options)) - 1]
        