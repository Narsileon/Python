import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import money, userinput

FLOORS = {
    "{} 0".format(t("floor")): "60.00€",
    "{} 1".format(t("floor")): "50.00€",
    "{} 2".format(t("floor")): "40.00€"
}

CATEGORIES = {
    "{} 1".format(t("category")): "20.00€",
    "{} 2".format(t("category")): "10.00€",
    "{} 3".format(t("category")): "0.00€"
}

data = {}

def main():
    print("{}:".format(t("rental_prices")))
    get_data()
    set_data()
    print("")
    display_data()

def get_data():
    
    data["floor"] = FLOORS[userinput.get_choice(t("choice_floor"), list(FLOORS))]
    data["category"] = CATEGORIES[userinput.get_choice(t("choice_category"), list(CATEGORIES))]
    
def set_data():
    data["rent_square_metre"] = money.add(data["floor"], data["category"], "C")
    
def display_data():
    print("{}:".format(t("summary")))
    
    for x, y in data.items():
        print("- {}: {}".format(t(x), y))
    
main()
