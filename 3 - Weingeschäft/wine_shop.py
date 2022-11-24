import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import math, money, userinput

articles = {}
delivery = {}
invoice = {}

delivery_price = "5.00€"

def main():
    get_articles_data()
    set_delivery_data()
    set_invoice_data()
    print("")
    display_data()

def get_articles_data():
    index = 0
    
    print("{}:".format(t("wine_shop")))
    
    while True:
        article = {}
        
        article["name"] = userinput.get_string(t("input_wine_name"))
        article["quantity"] = userinput.get_int(t("input_quantity"), 1, 99)
        article["single_net_price"] = money.get(t("input_unit_price"), 1, 99, "C")
        article["single_gross_price"] = money.netto_to_brutto(article["single_net_price"], "C") 
        
        articles[index] = article
        
        print("")
        
        if (userinput.get_bool(t("Would you like to order an additional wine?"))):
            index += 1
            continue
        else:
            break

def set_delivery_data():
    total_quantity = 0
    
    for i in articles:          
        total_quantity += articles[i]["quantity"]
    
    delivery["total_quantity"] = total_quantity
    delivery["cartons"] = math.ceil(total_quantity / 6)
    delivery["free_slots"] = (delivery["cartons"] * 6) - total_quantity
    delivery["delivery_price"] = delivery_price

def set_invoice_data():
    total_net_price = 0
    total_gross_price = 0
    
    for i in articles:          
        total_net_price += money.multiply(articles[i]["single_net_price"], articles[i]["quantity"])
        total_gross_price += money.multiply(articles[i]["single_gross_price"], articles[i]["quantity"])
    
    total_net_price = money.add(total_net_price, delivery_price)
    total_gross_price = money.add(total_gross_price, delivery_price)
    
    invoice["total_net_price"] = str(total_net_price) + money.CURRENCY
    invoice["total_gross_price"] = str(total_gross_price) + money.CURRENCY 

def display_data():
    print("{}:".format(t("order_summary")))   
    print("")
    display_articles_data()
    print("")
    display_delivery_data()
    print("")
    display_invoice_data()         

def display_articles_data():
    for i in articles:
        print("Artikel n°" + str(i) + ":")
        
        for x, y in articles[i].items():     
            print("- {}: {}".format(t(x), y))  

def display_delivery_data():
    print("{}:".format(t("delivery_summary")))
    
    for x, y in delivery.items():
        print("- {}: {}".format(t(x), y))

def display_invoice_data():
    print("{}:".format(t("invoice_summary")))
    
    for x, y in invoice.items():
        print("- {}: {}".format(t(x), y))

main()
