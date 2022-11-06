import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import database

TABLE = "candidates"

FIELD_CANDIDATE_NUMBER = "candidate_number"
FIELD_LAST_NAME = "last_name"
FIELD_FIRST_NAME = "first_name"
FIELD_GENDER = "gender"
FIELD_STREET = "street"
FIELD_HOUSE_NUMBER = "house_number"
FIELD_POST_CODE = "post_code"
FIELD_CITY = "city"
FIELD_BIRTH_DATE = "birth_date"
FIELD_SALARY = "salary"
FIELD_POLICE_RECORD = "police_record"

def main():
    delete_table()
    create_table()
    
def create_table():
    fields = ', '.join(value for name, value in globals().items() if name.startswith('FIELD'))
    
    database.create_table(TABLE, fields)

def delete_table():  
    database.delete_table(TABLE)
    
main()
    