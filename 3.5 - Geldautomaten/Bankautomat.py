import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import money, moneychange

data = {}
change = {}

def main():
    get_data()
    display_data()
    
def get_data():
    global change
    
    value = money.get("Bitte geben Sie den gewünschten Betrag ein: ", 0.01)  
    data["Gewünschter Betrag"] = money.format_currency(value, "C")
    
    change = moneychange.get(value)
    
def display_data():
    print("")
    
    for x, y in data.items():
        print(x + ":", y)
    
    for x, y in change.items():
        print("-", x + ":", y)

main()
