from datetime import datetime
from localization import t

ErrorMessage =  "{} ".format(t("Please provide a valid answer."))

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
            print(ErrorMessage + t("string_length_between").format(minLen, maxLen))
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
            print(ErrorMessage + t("value_between").format(minValue, maxValue))
            continue  

def get_bool(question):
    choice = "({}/{})".format(t("yes"), t("no"))
    
    while True:
        try:
            value = str(input(question.format(choice)))
        except ValueError:
            print(ErrorMessage)
        if (value == t("yes") or value == t("yes").lower()):
            return True
        elif (value == t("no") or value == t("no").lower()):
            return False
        else:
            print(ErrorMessage)
            continue
        
def get_choice(question, options):
    print(question)

    for x, element in enumerate(options):
        print("  {}) {}".format(x + 1, element))

    return options[get_int("  => {}: ".format(t("number")), 1, len(options)) - 1]
        