import math

from decimal import Decimal

CURRENCY = "€"
TAX = 19.00

def get(question, minValue = -9223372036854775808, maxValue = 9223372036854775807, format_option = "D"):
    while True:
        try:
            value = float(input(question))
            value = Decimal("%.2f" % value)
            
        except ValueError:
            print("Bitte geben Sie eine gültige Antwort: ")
            continue
        
        if (minValue <= value <= maxValue):
            return format_currency(value, format_option)
        
        else:
            print("Bitte geben Sie eine Antwort zwischen {} und {}: ".format(minValue, maxValue))
            continue

def add(a, b, format_option = "D"):
    a = validate_currency(a)
    b = validate_currency(b)
    
    value = a + b
    
    return format_currency(value, format_option)

def subtract(a, b, format_option = "D"):
    a = validate_currency(a)
    b = validate_currency(b)
    
    value = a - b
    
    return format_currency(value, format_option)

def multiply(a, x, format_option = "D"):
    a = validate_currency(a)
    x = validate_currency(x)
    
    value = a * x
    
    return format_currency(value, format_option)

def divide(a, x, format_option = "D"):
    a = validate_currency(a)
    x = validate_currency(x)
    
    value = a / x
    
    return format_currency(value, format_option)

def netto_to_brutto(netto, format_option = "D"):
    netto = validate_currency(netto)
    
    brutto = netto / (1 + Decimal(TAX / 100))
    
    return format_currency(brutto, format_option)

def brutto_to_netto(brutto, format_option = "D"):
    brutto = validate_currency(brutto)
    
    netto = brutto * Decimal(1 + (TAX / 100))
    
    return format_currency(netto, format_option)
        
def validate_currency(currency):
    if (
        isinstance(currency, int) or
        isinstance(currency, float) or
        isinstance(currency, Decimal)
    ):
        return Decimal("%.2f" % currency)
    
    elif currency[-1] == CURRENCY:
        return Decimal(currency[:-1])

def format_currency(currency, f):
    currency = Decimal("%.2f" % currency)
    
    if (f == "C"):
        return str(currency) + CURRENCY
    
    elif (f == "D"):
        return currency
    