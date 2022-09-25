import userinput

DAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
SEASONS = ["Frühling", "Sommer", "Herbst", "Winter"]

def get_day():
    return userinput.get_choice("Bitte wählen Sie einen Tag: ", DAYS)

def get_month():
    return userinput.get_choice("Bitte wählen Sie einen Monat: ", MONTHS)

def get_season():
    return userinput.get_choice("Bitte wählen Sie eine Jahreszeit: ", SEASONS)
