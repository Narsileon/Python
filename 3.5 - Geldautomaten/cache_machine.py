import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import money, money_change

data = {}
change = {}

def main():
    print("{}:".format(t("cash_machine")))
    get_data()
    print("")
    display_data()
    
def get_data():
    global change
    
    value = money.get(t("input_amount"), 0.01)  
    data["amount"] = money.format_currency(value, "C")
    
    change = money_change.get(value)
    
def display_data():
    for x, y in data.items():
        print("{}: {}".format(t(x), y))
    
    for x, y in change.items():
        print("- {}: {}".format(x, y))

main()
