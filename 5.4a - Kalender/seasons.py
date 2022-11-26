import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import timeinput

data = {}

def main():
    print("{}:".format(t("seasons")))
    get_data()
    print("")
    display_data()

def get_data():
    data["season"] = timeinput.get_season()
    
def display_data():
    print("{}: {}.".format(t("season"), data["season"]))
    
main()
