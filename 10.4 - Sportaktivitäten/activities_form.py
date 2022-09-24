import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import jsonserializer, userinput

activities = []

index = 0
activity = []

def main():
    load_activities()   
    get_activity()      
    display_informations() 
    set_activity()
    save_activities()

def load_activities():
    global activities
    
    activities = jsonserializer.load_dictionary("activities.json")
    
def save_activities():
    activities[index] = activity
    jsonserializer.save_dictionary("activities.json", activities)

def get_activity():
    global activity
    global index
    
    options = []

    for i in activities:
        options.append(i['name'])
    
    index = userinput.get_choice("Bitte wählen Sie eine Aktivität: ", options)
    activity = activities[index]

def display_informations():
   
    print("")
    print("Aktivität:", activity["name"] + format_description())
    print("- Kursort:", activity["kursort"])
    print("- Kurstermin:", activity["kurstermin"])
    print("- Kursdauer:", activity["kursdauer"])
    print("- Teilnehmer: {}/{}".format(activity["current_teilnehmer"], activity["max_teilnehmer"]))
    print("")
    
def format_description():
    return "" if activity["description"] == "" else "(" + activity["description"] + ")"

def set_activity():
    beteiligung = userinput.get_bool("Möchten Sie an diesen Kurs teilnehmen")
    
    if (beteiligung and int(activity["current_teilnehmer"]) < int(activity["max_teilnehmer"])):
        activity["current_teilnehmer"] = int(activity["current_teilnehmer"]) + 1
        
main()
