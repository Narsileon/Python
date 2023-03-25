import table as M

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database, jsonserializer, userinput

from localization import t

activities = []
activity = []

def main():
    get_activity()
    print("")
    display_data()
    
    set_activity()
    
def get_activity():
    global ACTIVITIES
    global activity
    global activity_index
    
    ACTIVITIES = database.select_all(M.TABLE)
    activity_name_list = list((x[M.FIELD_NAME]) for x in ACTIVITIES)
    
    activity_name = userinput.get_choice(t("choice_activity"), activity_name_list)
    
    activity = next(x for x in ACTIVITIES if x[M.FIELD_NAME] == activity_name)

def display_data():   
    print("- {}:".format(t("Activity")), activity[M.FIELD_NAME], format_description())
    print("- {}:".format(t(M.FIELD_LOCATION)), activity[M.FIELD_LOCATION])
    print("- {}:".format(t(M.FIELD_DATES)), activity[M.FIELD_DATES])
    print("- {}:".format(t(M.FIELD_DURATION)), activity[M.FIELD_DURATION])
    print("- {}: {}/{}".format(t("participants"), activity[M.FIELD_PARTICIPANTS_NUMBER], activity[M.FIELD_PARTICIPANTS_NUMBER_MAX]))

def set_activity():
    if (int(activity[M.FIELD_PARTICIPANTS_NUMBER]) < int(activity[M.FIELD_PARTICIPANTS_NUMBER_MAX])):
        if (userinput.get_bool(t("Would you like to take this course?"))):
            database.update(
                M.TABLE,
                "{}={}+1".format(M.FIELD_PARTICIPANTS_NUMBER, M.FIELD_PARTICIPANTS_NUMBER),
                "{}='{}'".format(M.FIELD_NAME, activity[M.FIELD_NAME])
            )
            
            if (userinput.get_bool(t("Would you like to choose another course?"))):
                main()
        else:
            if (userinput.get_bool(t("Would you like to choose a different course?"))):
                main()
    else:
        print(t("Unfortunately, this course is already full."))

        if (userinput.get_bool(t("Would you like to choose a different course?"))):
            main()
        
def format_description():
    return "" if activity[M.FIELD_DESCRIPTION] == "" else "(" + activity[M.FIELD_DESCRIPTION] + ")"
        
main()
