import candidate as M

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database, mathf, money, timeinput, userinput
from localization import t

GENDER = ["Männlich", "Weiblich"]
REGIONS = ["40", "42", "45", "46", "47", "48", "58", "59"]

data = {}

def main():
    print("Bewerbung:")
    get_data()
    print("")
    display_data()
    print("")
    validate_bewerber()
    
    save_data()

def get_data():
    data[M.FIELD_CANDIDATE_NUMBER] = userinput.get_int("- Bitte geben Sie Ihre Bewerbernummer ein: ", 0)
    data[M.FIELD_LAST_NAME] = userinput.get_string("- Bitte geben Sie Ihr Nachnamen ein: ")
    data[M.FIELD_FIRST_NAME] = userinput.get_string("- Bitte geben Sie Ihr Vornamen ein: ")
    data[M.FIELD_GENDER] = userinput.get_choice("- Bitte geben Sie Ihr Gender ein: ", GENDER)   
    data[M.FIELD_STREET] = userinput.get_string("- Bitte geben Sie Ihre Straße ein: ") 
    data[M.FIELD_HOUSE_NUMBER] = userinput.get_int("- Bitte geben Sie Ihre Hausnummer ein: ", 1, 999)
    data[M.FIELD_POST_CODE] = userinput.get_int("- Bitte geben Sie Ihr Postleitzahl ein: ", 10000, 99999)
    data[M.FIELD_CITY] = userinput.get_string("- Bitte geben Sie Ihre Stadt ein: ")
    
    geburtsdatum = timeinput.get_time("- Bitte geben Sie Ihr Geburtsdatum ein", "Date")
    data[M.FIELD_BIRTH_DATE] = timeinput.to_string(geburtsdatum, "Date")
    
    data[M.FIELD_SALARY] = money.get("- Bitte geben Sie Ihr Gehaltsvorstellung ein: ", 1000, 10000, "C")
    data[M.FIELD_POLICE_RECORD] = userinput.get_bool("- Wurden Sie schon mal verurteilt")

def display_data():   
    print("Zusammenfassung:")
    
    for x, y in data.items():
        print("- {}: {}".format(t(x), y))

def validate_bewerber():  
    if not (data[M.FIELD_POLICE_RECORD]) and validate_age() and validate_region():
        print("Wir haben Ihnen eine Einladung zu einem Vorstellungsgespräch zugeschickt!")
    else:
        print("Leider entspricht Ihr Profil nicht unseren Erwartungen.")

def validate_age():
    age = mathf.get_age(timeinput.parse_time(data[M.FIELD_BIRTH_DATE], "Date"))
    return age < 50

def validate_region():
    region = str(data[M.FIELD_POST_CODE])[0: 2]
    return region in REGIONS

def save_data():
    values = ', '.join("'" + str(x) + "'" for x in data.values())
    database.insert(M.TABLE, "{}".format(values))
    
main()
