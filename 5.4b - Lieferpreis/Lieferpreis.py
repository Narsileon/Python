import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, money, userinput

CATEGORIES = ["A", "B", "C"]

data = {}

def main():
    get_data()
    set_data()
    print("")
    display_data()

def get_data():
    data["Entfernung"] = userinput.get_int("Bitte geben Sie die Entfernung in Kilometern ein: ", 0, 10000)
    data["Kategorie"] = userinput.get_choice("Bitte geben Sie die Kundenkategorie ein: ", CATEGORIES)

def set_data():
    base_cost = get_base_cost(data["Entfernung"])
    data["Grundlegende Versandkosten"] = money.format_currency(base_cost, "C")
    
    customer_discount = get_customer_discount(data["Kategorie"])
    data["Kundenrabatt"] = money.format_currency(customer_discount, "C")
    
    final_cost = mathf.clamp(base_cost - customer_discount, 0.00, 100.00)
    data["Endgültige Versandkosten"] = money.format_currency(final_cost, "C")

def display_data(): 
    print("Lieferpreis:")
    
    for x, y in data.items():
        print("- {}: {}".format(x, y))
        
def get_base_cost(distance):   
    if (distance <= 30):
        return 10.00
    elif (distance <= 70):
        return 30.00
    elif (distance <= 100):
        return 50.00
    else:
        return 100.00
    
def get_customer_discount(custumer_category):
    if (custumer_category == "A"):
        return 10.00
    elif (custumer_category == "B"):
        return 20.00
    elif (custumer_category == "C"):
        return 30.00
    else:
        raise ValueError("Diese Kategorie existiert nicht.")
        
main()    
    