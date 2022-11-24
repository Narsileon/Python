import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import money, money_change

data = {}
change = {}

def main():
    print("{}:".format(t("payment machine")))
    get_data()
    print("")
    display_data()
    
def get_data():
    global change
    
    amount_to_be_paid = money.get(t("input_amount_to_be_paid"), 0.01)
    data["amount_to_be_paid"] = money.format_currency(amount_to_be_paid, "C")
    
    amount_paid = money.get(t("input_amount_paid"), amount_to_be_paid)
    data["amount_paid"] = money.format_currency(amount_paid, "C")

    amount_due = amount_paid - amount_to_be_paid
    data["amount_due"] = money.format_currency(amount_due, "C")
    
    change = money_change.get(amount_due)
    
def display_data():   
    for x, y in data.items():
        print("{}: {}".format(t(x), y))
    
    for x, y in change.items():
        print("- {}: {}".format(x, y))

main()
