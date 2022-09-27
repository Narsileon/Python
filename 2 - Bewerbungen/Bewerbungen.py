import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, money, timeinput, userinput

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

def get_data():
    data["Bewerbernummer"] = userinput.get_int("- Bitte geben Sie Ihre Bewerbernummer ein: ", 0)
    data["Nachname"] = userinput.get_string("- Bitte geben Sie Ihr Nachnamen ein: ")
    data["Vorname"] = userinput.get_string("- Bitte geben Sie Ihr Vornamen ein: ")
    data["GENDER"] = userinput.get_choice("- Bitte geben Sie Ihr GENDER ein: ", GENDER)   
    data["Straße"] = userinput.get_string("- Bitte geben Sie Ihre Straße ein: ") 
    data["Hausnummer"] = userinput.get_int("- Bitte geben Sie Ihre Hausnummer ein: ", 1, 999)
    data["Postleitzahl"] = userinput.get_int("- Bitte geben Sie Ihr Postleitzahl ein: ", 10000, 99999)
    data["Stadt"] = userinput.get_string("- Bitte geben Sie Ihre Stadt ein: ") 
    data["Geburtsdatum"] = timeinput.get_time("- Bitte geben Sie Ihr Geburtsdatum ein", "Date")
    data["Gehaltsvorstellung"] = money.get("- Bitte geben Sie Ihr Gehaltsvorstellung ein: ", 1000, 10000, "C")
    data["Vorstrafen"] = userinput.get_bool("- Wurden Sie schon mal verurteilt")

def display_data():   
    print("Zusammenfassung:")
    
    for x, y in data.items():
        print("- {}: {}".format(x, y))

def validate_bewerber():  
    if not (data["Vorstrafen"]) and validate_age() and validate_region():
        print("Wir haben Ihnen eine Einladung zu einem Vorstellungsgespräch zugeschickt!")
    else:
        print("Leider entspricht Ihr Profil nicht unseren Erwartungen.")

def validate_age():
    age = mathf.get_age(timeinput.parse_time(data["Geburtsdatum"], "Date"))
    return age < 50

def validate_region():
    region = str(data["Postleitzahl"])[0: 2]
    return region in REGIONS
    
main()
