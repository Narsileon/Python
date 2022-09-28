import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mathf, money, timeinput, userinput

SPEED = "kph"

data = {}

def main():
    get_data()
    print("")
    display_data()

def get_data():
    print("Langstreckenwandern:")
    
    index = 1
    
    while True:
        daily_data = {}
        
        date = timeinput.get_time("- Bitte geben Sie den Tag ein", "Date")
        daily_data["Datum"] = timeinput.to_string(date, "Date")
        
        daily_data["Kilometer"] = userinput.get_int("- Bitte geben Sie die Anzahl der gelaufenen Kilometer ein: ", 0, 100)
        
        time = timeinput.get_time("- Bitte geben Sie die Zeit ein", "Hour")
        daily_data["Zeit"] = timeinput.to_string(time, "Hour")
        
        average_speed = round(daily_data["Kilometer"] / (time.hour * 60 + time.minute) * 60)
        daily_data["Durchschnittsgeschwindigkeit"] = str("{} {}".format(average_speed, SPEED))    
        
        data[index] = daily_data
        
        index += 1
        
        print("")
        
        if not (userinput.get_bool("Möchten Sie eine weitere Wanderung speichern")):
            break
        
def display_data(): 
    for i in data:
        print("Wanderung n°{}:".format(i))
        for x, y in data[i].items():
            print("- {}: {}".format(x, y))
    
    print("")
    print("Gesamtdurchschnittsgeschwindigkeit: {}".format(compute_average_speed()))

def compute_average_speed():
    average_speed = 0;
    
    for i in data:
        average_speed += int(data[i]["Durchschnittsgeschwindigkeit"].removesuffix(SPEED))
    
    average_speed /= len(data)
    
    return str("{} {}".format(average_speed, SPEED))

main()
