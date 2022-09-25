import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import money, moneychange

data = {}
change = {}

def main():
    get_data()
    print("")
    display_data()
    
def get_data():
    global change
    
    amount_to_pay = money.get("Bitte geben Sie den zu zahlenden Betrag ein: ", 0.01)
    data["Zu zahlender Betrag"] = money.format_currency(amount_to_pay, "C")
    
    amount_paid = money.get("Bitte geben Sie den gezahlten Betrag ein: ", amount_to_pay)
    data["Gezahlter Betrag"] = money.format_currency(amount_paid, "C")

    change = moneychange.get(amount_paid - amount_to_pay)
    
def display_data():   
    for x, y in data.items():
        print("{}: {}".format(x, y))
    
    for x, y in change.items():
        print("- {}: {}".format(x, y))

main()
