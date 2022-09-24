from datetime import date

def clamp(name, value, minValue, maxValue):
    if value < minValue:
        print("{} was less than {} and has been clamped.".format(name, minValue))
        return minValue
    elif value > maxValue:
        print("{} was greater than {} and has been clamped.".format(name, maxValue))
        return maxValue
    else:
        return value

def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age