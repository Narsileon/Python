from datetime import date
from localization import t

def clamp(value, minValue, maxValue, name = None):
    if value < minValue:
        if (name):
            print(t("value_clamped_up").format(name, minValue))
        return minValue
    elif value > maxValue:
        if (name):
            print(t("value_clamped_down").format(name, maxValue))
        return maxValue
    else:
        return value

def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def sum_range(start, end):
    return (end * (end + 1) - start * (start - 1)) / 2
