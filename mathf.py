from datetime import date

def clamp(name, value, minValue, maxValue):
    if value < minValue:
        print("'{}' war kleiner als {} und wurde geklemmt.".format(name, minValue))
        return minValue
    elif value > maxValue:
        print("'{}' war größer als {} und wurde geklemmt.".format(name, maxValue))
        return maxValue
    else:
        return value

def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age