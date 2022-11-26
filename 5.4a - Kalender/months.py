import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import timeinput

data = {}

def main():
    print("{}:".format(t("months")))
    get_data()
    print("")
    display_data()

def get_data():
    data["month"] = timeinput.get_month()
    
def display_data():
    print("{}: {}.".format(t("month"), data["month"]))
    
main()
