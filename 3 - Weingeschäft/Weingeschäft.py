import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math, money, userinput

articles = {}
delivery = {}
invoice = {}

def main():
    get_articles_data()
    set_delivery_data()
    set_invoice_data()
    display_data()

def get_articles_data():
    index = 0
    
    print("Weingeschäft:")
    
    while True:
        article = {}
        
        article["Name"] = userinput.get_string("- Bitte geben Sie den Namen des Weines ein: ")
        article["Anzahl"] = userinput.get_int("- Bitte geben Sie die gewünschte Menge ein: ", 1, 99)
        article["Einzelnettopreis"] = money.get("- Bitte geben Sie den Stückpreis ein: ", 1, 99, "C")
        article["Einzelbruttopreis"] = money.netto_to_brutto(article["Einzelnettopreis"], "C") 
        
        articles[index] = article
        
        print("")
        
        if (userinput.get_bool("Möchten Sie einen zusätzlichen Wein bestellen")):
            index += 1
            continue
        else:
            break

def set_delivery_data():
    gesamtanzahl = 0
    
    for i in articles:          
        gesamtanzahl += articles[i]["Anzahl"]
    
    delivery["Gesamtanzahl"] = gesamtanzahl
    delivery["Kartons"] = math.ceil(delivery["Gesamtanzahl"] / 6)
    delivery["Freie Plätze"] = (delivery["Kartons"] * 6) - delivery["Gesamtanzahl"]
    delivery["Lieferpreis"] = "5.00€"

def set_invoice_data():
    gesamtnettopreis = 0
    gesamtbruttopreis = 0
    
    for i in articles:          
        gesamtnettopreis += money.multiply(articles[i]["Einzelnettopreis"], articles[i]["Anzahl"])
        gesamtbruttopreis += money.multiply(articles[i]["Einzelbruttopreis"], articles[i]["Anzahl"])
    
    gesamtnettopreis = money.add(gesamtnettopreis, delivery["Lieferpreis"])
    gesamtbruttopreis = money.add(gesamtbruttopreis, delivery["Lieferpreis"])
    
    invoice["Gesamtnettopreis"] = str(gesamtnettopreis) + money.CURRENCY
    invoice["Gesamtbruttopreis"] = str(gesamtbruttopreis) + money.CURRENCY 

def display_data():
    print("")
    
    print("Zusammenfassung der Bestellung:")
    
    print("")

    display_articles_data()
    display_delivery_data()
    display_invoice_data()         

def display_articles_data():
    for i in articles:
        print ("Artikel n°" + str(i) + ":")
        
        for x, y in articles[i].items():     
            print ("-", x + ":", y) 
           
        print("")    

def display_delivery_data():
    print("Zusammenfassung der Lieferung:")
    
    for x, y in delivery.items():
        print("-", x + ":", y)
        
    print("")

def display_invoice_data():
    print("Zusammenfassung der Rechnung:")
    
    for x, y in invoice.items():
        print("-", x + ":", y)
        
    print("")

main()
