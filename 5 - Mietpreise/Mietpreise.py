import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import money, userinput

FLOORS = {
    "Edgeschoss": "60.00€",
    "Erster Stock": "50.00€",
    "Zweiter Stock": "40.00€"
}

CATEGORIES = {
    "Erste Kategorie": "20.00€",
    "Zweite Kategorie": "10.00€",
    "Dritte Kategorie": "0.00€"
}

data = {}

def main():
    get_data()
    set_data()
    display_data()

def get_data():
    print("Mietpreise:")
    data["Etage"] = FLOORS[userinput.get_choice("- Bitte wählen Sie eine Etage: ", list(FLOORS))]
    data["Kategorie"] = CATEGORIES[userinput.get_choice("- Bitte wählen Sie eine Kategorie: ", list(CATEGORIES))]
    
def set_data():
    data["Quadratmetermiete"] = money.add(data["Etage"], data["Kategorie"])
    
def display_data():   
    print("")
    
    print("Zusammenfassung:")
    
    for x, y in data.items():
        print("-", x + ":", y)
        
    print("")  
    
main()
