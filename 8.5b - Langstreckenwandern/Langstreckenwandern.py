import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, money, timeinput, userinput

data = []

def main():
    get_data()
    display_data()

def get_data():
    daily_data = {}
    
    while True:      
        daily_data["Datum"] = timeinput.get_time("Bitte geben Sie den Tag ein", "Date")
        daily_data["Kilometer"] = userinput.get_int("Bitte geben Sie die Anzahl der gelaufenen Kilometer ein: ", 0, 100)
        daily_data["Zeit"] = timeinput.get_time("Bitte geben Sie die Zeit ein", "Hour")
        
        data.append(daily_data)
        
        print("")
        
        if (userinput.get_bool("Möchten Sie eine weitere Wanderung speichern")):
            continue
        else:
            break
        
def display_data():
    for i in data:
        for x, y in i.items():
            print("- {}: {}".format(x, y))    


main()
