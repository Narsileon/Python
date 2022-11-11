import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database, jsonserializer

TABLE = "activities"

FIELD_NAME = "name"
FIELD_DESCRIPTION = "description"
FIELD_LOCATION = "location"
FIELD_DATES = "dates"
FIELD_DURATION = "duration"
FIELD_PARTICIPANTS_NUMBER = "participants_number"
FIELD_PARTICIPANTS_NUMBER_MAX = "participants_number_max"

ACTIVITIES = jsonserializer.load_dictionary("activities.json")

def main():
    delete_table()
    create_table()
    seed_table()
    
def create_table():
    fields = ', '.join(value for name, value in globals().items() if name.startswith('FIELD'))
    
    database.create_table(TABLE, fields)

def delete_table():  
    database.delete_table(TABLE)
    
def seed_table():
    for i in ACTIVITIES:
        fields = ', '.join("'" + str(x) + "'" for x in i.values())
        
        database.insert(TABLE, fields) 
    
main()