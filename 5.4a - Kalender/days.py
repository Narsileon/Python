import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import timeinput

data = {}

def main():
    print("{}:".format(t("days")))
    get_data()
    print("")
    display_data()

def get_data():
    data["day"] = timeinput.get_day()
    
def display_data():
    print("{}: {}.".format(t("day"), data["day"]))
    
main()
