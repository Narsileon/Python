import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import timeinput

data = {}

def main():
    get_data()
    print("")
    display_data()

def get_data():
    data["Monat"] = timeinput.get_month()
    
def display_data():
    print("Monat: {}.".format(data["Monat"]))
    
main()
