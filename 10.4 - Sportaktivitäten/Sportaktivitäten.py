import activity as M

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database, jsonserializer, userinput

from localization import t

ACTIVITIES = database.select_all(M.TABLE)

activity = {}

def main():
    get_activity()
    print("")
    display_data()
    
    set_activity()
    #save_activities()
    
def save_activities():
    activities[activity["Name"]] = activity["Data"]
    
    jsonserializer.save_dictionary("activities.json", activities)

def get_activity():
    activity_list = list((x["name"]) for x in ACTIVITIES)
    
    activity = userinput.get_choice("Bitte wählen Sie eine Aktivität: ", activity_list)

def display_data():
    print("Aktivität:", activity[M.FIELD_NAME], format_description())
    print("- {}:".format(t(M.FIELD_LOCATION)), activity["Data"]["Kursort"])
    print("- {}:".format(t(M.FIELD_DATES)), activity["Data"]["Kurstermin"])
    print("- {}:".format(t(M.FIELD_DURATION)), activity["Data"]["Kursdauer"])
    print("- {}: {}/{}".format(t("participants"), activity["Data"]["Teilnehmerzahl"], activity["Data"]["Teilnehmerzahl_Max"]))

def set_activity():
    beteiligung = userinput.get_bool("Möchten Sie an diesen Kurs teilnehmen")
    
    if (beteiligung and int(activity["Data"]["Teilnehmerzahl"]) < int(activity["Data"]["Teilnehmerzahl_Max"])):
        activity["Data"]["Teilnehmerzahl"] = int(activity["Data"]["Teilnehmerzahl"]) + 1
        
def format_description():
    return "" if activity["Data"]["Bezeichnung"] == "" else "(" + activity["Data"]["Bezeichnung"] + ")"
        
main()
