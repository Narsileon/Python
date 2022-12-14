import table as M

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from localization import t

import database, mathf, money, timeinput, userinput

data = {}

def main():
    print("{}:".format(t("candidature")))
    get_data()
    print("")
    display_data()
    
    save_data()

def get_data():
    data[M.FIELD_CANDIDATE_NUMBER] = userinput.get_int(t("input_candidate_number"), 0)
    
    # Personal informations
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

def save_data():
    values = ', '.join("'" + str(x) + "'" for x in data.values())
    database.insert(M.TABLE, "{}".format(values))
    
main()
