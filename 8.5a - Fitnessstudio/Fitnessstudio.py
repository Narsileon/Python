import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import userinput

GRADES = [
    "sehr schlechte Fitness",
    "schlechte Fitness",
    "durchschnittliche Fitness",
    "gute Fitness",
    "sehr gute Fitness"
]

data = {}

def main():
    print("Fitnessstudio: ")  
    get_data()    
    print("")    
    display_data()

def get_data():
    data["Punktwert"] = userinput.get_int("- Bitte geben Sie Ihren Punktwert ein: ", 0, 4)

def display_data():
    print("Auswertung: {}.".format(GRADES[data["Punktwert"]]))

main()
