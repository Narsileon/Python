from datetime import datetime

import userinput

DAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
SEASONS = ["Frühling", "Sommer", "Herbst", "Winter"]

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
    return userinput.get_choice("Bitte wählen Sie einen Tag: ", DAYS)

def get_month():
    return userinput.get_choice("Bitte wählen Sie einen Monat: ", MONTHS)

def get_season():
    return userinput.get_choice("Bitte wählen Sie eine Jahreszeit: ", SEASONS)

def get_time(question, option):
    time_format = OPTIONS[option]["Format"]
    time_example = OPTIONS[option]["Example"]
    
    while True:
        try:
            return datetime.strptime(input("{} ({}): ".format(question, time_example)), time_format)
        except ValueError:
            print("Bitte geben Sie Ihre Antwort im angegebenen Format ein: ")
            continue
    
def to_string(date, option):
    return date.strftime(OPTIONS[option]["Format"])
    