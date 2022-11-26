import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import mathf, money, userinput

CATEGORIES = [
    "A",
    "B",
    "C"
]

data = {}

def main():
    print("{}:".format(t("delivery_prices")))
    get_data()
    set_data()
    print("")
    display_data()

def get_data():
    data["distance"] = userinput.get_int(t("input_distance").format("(km)"), 0, 10000)
    data["customer_category"] = userinput.get_choice(t("input_customer_category"), CATEGORIES)

def set_data():
    base_cost = get_base_cost(data["distance"])
    data["basic_shipping_costs"] = money.format_currency(base_cost, "C")
    
    customer_discount = get_customer_discount(data["customer_category"])
    data["customer_discount"] = money.format_currency(customer_discount, "C")
    
    final_cost = mathf.clamp(base_cost - customer_discount, 0.00, 100.00)
    data["final_shipping_costs"] = money.format_currency(final_cost, "C")

def display_data(): 
    print("{}:".format(t("delivery_price")))
    
    for x, y in data.items():
        print("- {}: {}".format(t(x), y))
        
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
        raise ValueError("This category doesn't exist.")
        
main()    
    