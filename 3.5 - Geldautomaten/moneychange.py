import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import math, money

CHANGES = {
    "500-{}".format(t("euro_bills")): "500.00€",
    "200-{}".format(t("euro_bills")): "200.00€",
    "100-{}".format(t("euro_bills")): "100.00€",
    "50-{}".format(t("euro_bills")): "50.00€",
    "20-{}".format(t("euro_bills")): "20.00€",
    "10-{}".format(t("euro_bills")): "10.00€",
    "5-{}".format(t("euro_bills")): "5.00€",
    "2-{}".format(t("euro_coins")): "2.00€",
    "1-{}".format(t("euro_coins")): "1.00€",
    "50-{}".format(t("cent_coins")): "0.50€",
    "20-{}".format(t("cent_coins")): "0.20€",
    "10-{}".format(t("cent_coins")): "0.10€",
    "5-{}".format(t("cent_coins")): "0.05€",
    "2-{}".format(t("cent_coins")): "0.02€",
    "1-{}".format(t("cent_coins")): "0.01€"
}

def get(value):
    data = {}
    
    while value > 0.00:  
        for x, y in CHANGES.items():
            amount = math.floor(money.divide(value, y))
            
            if (amount > 0):
                data[x] = amount
                change = money.multiply(y, amount)
                value -= change
                
    return data
