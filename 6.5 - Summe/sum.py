import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import mathf, userinput

data = {}

def main():
    print("{}:".format(t("sum")))
    get_data()
    print("")
    display_data()
    
def get_data():
    data["start_number"] = userinput.get_int(t("input_start_number"), 1)
    data["end_number"] = userinput.get_int(t("input_end_number"), 2)
    data["result"] = mathf.sum_range(data["start_number"], data["end_number"])

def display_data():
    print ("{}:".format(t("summary")))
    for x, y in data.items():
        print("- {}: {}".format(t(x), y))

main()
