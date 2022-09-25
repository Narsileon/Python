import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, userinput

data = {}

def main():
    print("Summme:")
    get_data()
    print("")
    display_data()
    
def get_data():
    data["Startnummer"] = userinput.get_int("- Bitte geben Sie die Startnummer ein: ", 1)
    data["Endnummer"] = userinput.get_int("- Bitte geben Sie die Endnummer ein: ", 2)
    data["Ergebnis"] = mathf.sum_range(data["Startnummer"], data["Endnummer"])

def display_data():
    print ("Zusammenfassung:")
    for x, y in data.items():
        print("- {}: {}".format(x, y))

main()
