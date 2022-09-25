import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math, money

CHANGES = {
    "500-Euro-Scheine": "500.00€",
    "200-Euro-Scheine": "200.00€",
    "100-Euro-Scheine": "100.00€",
    "50-Euro-Scheine": "50.00€",
    "20-Euro-Scheine": "20.00€",
    "10-Euro-Scheine": "10.00€",
    "5-Euro-Scheine": "5.00€",
    "2-Euro-Münzen": "2.00€",
    "1-Euro-Münzen": "1.00€",
    "50-Cent-Münzen": "0.50€",
    "20-Cent-Münzen": "0.20€",
    "10-Cent-Münzen": "0.10€",
    "5-Cent-Münzen": "0.05€",
    "2-Cent-Münzen": "0.02€",
    "1-Cent-Münzen": "0.01€"
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
