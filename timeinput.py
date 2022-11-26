from datetime import datetime
from localization import t

import userinput

DAYS = [
    t("monday"),
    t("tuesday"),
    t("wednesday"),
    t("thursday"),
    t("friday"),
    t("saturday"),
    t("sunday")
]

MONTHS = [
    t("january"),
    t("february"),
    t("march"),
    t("april"),
    t("may"),
    t("june"),
    t("july"),
    t("august"),
    t("september"),
    t("october"),
    t("november"),
    t("december")
]

SEASONS = [
    t("spring"),
    t("summer"),
    t("autumn"),
    t("winter")
]

OPTIONS = {
    "Full": {
        "Format": "%d/%m/%Y %H:%M:%S",
        "Example": "dd/mm/YYYY HH:MM:SS",
    },
    "Date": {
        "Format": "%d/%m/%Y",
        "Example": "dd/mm/YYYY",
    },
    "Hour": {
        "Format": "%H:%M",
        "Example": "HH:MM",
    },   
}

def get_day():
    return userinput.get_choice(t("choice_day"), DAYS)

def get_month():
    return userinput.get_choice(t("choice_month"), MONTHS)

def get_season():
    return userinput.get_choice(t("choice_season"), SEASONS)

def get_time(question, option):
    time_format = OPTIONS[option]["Format"]
    time_example = OPTIONS[option]["Example"]
    
    while True:
        try:
            return datetime.strptime(input("{}({}) ".format(question, time_example)), time_format)
        except ValueError:
            print("Bitte geben Sie Ihre Antwort im angegebenen Format ein: ")
            continue

def parse_time(value, option):
    return datetime.strptime(value, OPTIONS[option]["Format"])

def to_string(date, option):
    return date.strftime(OPTIONS[option]["Format"])
    