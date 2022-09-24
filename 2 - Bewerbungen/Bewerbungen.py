import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, money, userinput

data = {}

geschlecht = ["Männlich", "Weiblich"]

allowedRegionen = ["40", "42", "45", "46", "47", "48", "58", "59"]

def main():
    get_data()
    display_data()
    validate_bewerber()

def get_data():
    print("Bewerbung:")
    data["Bewerbernummer"] = userinput.get_int("- Bitte geben Sie Ihre Bewerbernummer ein: ", 0)
    data["Nachname"] = userinput.get_string("- Bitte geben Sie Ihr Nachnamen ein: ")
    data["Vorname"] = userinput.get_string("- Bitte geben Sie Ihr Vornamen ein: ")
    data["Geschlecht"] = userinput.get_choice("- Bitte geben Sie Ihr Geschlecht ein: ", geschlecht)   
    data["Straße"] = userinput.get_string("- Bitte geben Sie Ihre Straße ein: ") 
    data["Hausnummer"] = userinput.get_int("- Bitte geben Sie Ihre Hausnummer ein: ", 1, 999)
    data["Postleitzahl"] = userinput.get_int("- Bitte geben Sie Ihr Postleitzahl ein: ", 10000, 99999)
    data["Stadt"] = userinput.get_string("- Bitte geben Sie Ihre Stadt ein: ") 
    data["Geburtsdatum"] = userinput.get_date("- Bitte geben Sie Ihr Geburtsdatum ein")
    data["Gehaltsvorstellung"] = money.get("- Bitte geben Sie Ihr Gehaltsvorstellung ein: ", 1000, 10000)
    data["Vorstrafen"] = userinput.get_bool("- Wurden Sie schon mal verurteilt")

def display_data():
    print("")
    
    print("Zusammenfassung:")
    
    for x, y in data.items():
        print("-", x + ":", y)
        
    print("")

def validate_bewerber():  
    if not (data["Vorstrafen"]) and validate_age() and validate_region():
        print("Wir haben Ihnen eine Einladung zu einem Vorstellungsgespräch zugeschickt!")
    else:
        print("Leider entspricht Ihr Profil nicht unseren Erwartungen.")

def validate_age():
    age = mathf.get_age(data["Geburtsdatum"])
    return age < 50

def validate_region():
    region = str(data["Postleitzahl"])[0: 2]
    return region in allowedRegionen
    
main()
