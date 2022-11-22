import candidate as M

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import database, mathf, money, timeinput, userinput

REGIONS = [
    "40",     
    "42",
    "45",
    "46",
    "47",
    "48",
    "58",
    "59"
]

data = {}

def main():
    print("{}:".format(t("candidature")))
    get_data()
    print("")
    display_data()
    print("")
    validate_candidate()
    
    save_data()

def get_data():
    data[M.FIELD_CANDIDATE_NUMBER] = userinput.get_int(t("input_candidate_number"), 0)
    
    # Personal Informations
    data[M.FIELD_LAST_NAME] = userinput.get_string(t("input_last_name"))
    data[M.FIELD_FIRST_NAME] = userinput.get_string(t("input_first_name"))
    data[M.FIELD_GENDER] = userinput.get_choice(t("input_gender"), [
        t("male"),
        t("female")
    ])
    geburtsdatum = timeinput.get_time(t("input_birth_date"), "Date")
    data[M.FIELD_BIRTH_DATE] = timeinput.to_string(geburtsdatum, "Date")
    
    # Address
    data[M.FIELD_STREET] = userinput.get_string(t("input_street")) 
    data[M.FIELD_HOUSE_NUMBER] = userinput.get_int(t("input_house_number"), 1, 999)
    data[M.FIELD_POST_CODE] = userinput.get_int(t("input_post_code"), 10000, 99999)
    data[M.FIELD_CITY] = userinput.get_string(t("input_city"))
    
    # Additional informations
    data[M.FIELD_SALARY] = money.get(t("input_salary_expectation"), 1000, 10000, "C")
    data[M.FIELD_POLICE_RECORD] = userinput.get_bool(t("input_police_record"))

def display_data():   
    print("{}:".format(t("summary")))
    
    for x, y in data.items():
        print("- {}: {}".format(t(x), y))

def validate_candidate():  
    if not (data[M.FIELD_POLICE_RECORD]) and validate_age() and validate_region():
        print(t("We have sent you an invitation for an interview!"))
    else:
        print(t("Unfortunately, your profile does not meet our expectations."))

def validate_age():
    age = mathf.get_age(timeinput.parse_time(data[M.FIELD_BIRTH_DATE], "Date"))
    return age < 50

def validate_region():
    region = str(data[M.FIELD_POST_CODE])[0: 2]
    return region in REGIONS

def save_data():
    values = ', '.join("'" + str(x) + "'" for x in data.values())
    database.insert(M.TABLE, "{}".format(values))
    
main()
