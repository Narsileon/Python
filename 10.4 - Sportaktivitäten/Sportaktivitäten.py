import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import jsonserializer, userinput

activities = []
activity = {}

def main():
    load_activities()   
    get_activity()      
    display_data() 
    set_activity()
    save_activities()

def load_activities():
    global activities
    
    activities = jsonserializer.load_dictionary("activities.json")
    
def save_activities():
    activities[activity["Name"]] = activity["Data"]
    
    jsonserializer.save_dictionary("activities.json", activities)

def get_activity():
    activity["Name"] = userinput.get_choice("Bitte wählen Sie eine Aktivität: ", list(activities))
    activity["Data"] = activities[activity["Name"]]

def display_data():
    print("")
    print("Aktivität:", activity["Name"], format_description())
    print("- Kursort:", activity["Data"]["Kursort"])
    print("- Kurstermin:", activity["Data"]["Kurstermin"])
    print("- Kursdauer:", activity["Data"]["Kursdauer"])
    print("- Teilnehmer: {}/{}".format(activity["Data"]["Teilnehmerzahl"], activity["Data"]["Teilnehmerzahl_Max"]))
    print("")

def set_activity():
    beteiligung = userinput.get_bool("Möchten Sie an diesen Kurs teilnehmen")
    
    if (beteiligung and int(activity["Data"]["Teilnehmerzahl"]) < int(activity["Data"]["Teilnehmerzahl_Max"])):
        activity["Data"]["Teilnehmerzahl"] = int(activity["Data"]["Teilnehmerzahl"]) + 1
        
def format_description():
    return "" if activity["Data"]["Bezeichnung"] == "" else "(" + activity["Data"]["Bezeichnung"] + ")"
        
main()
