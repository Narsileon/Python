import database

TABLES = {
    "candidates": "id, last_name, first_name, gender, street, house_nummer, postcode, city, birth_date, salary, criminal",
    "users": "id, last_name, first_name, gender",
}

DATA = {
    "users": [
        "1, 'Rigaux', 'Jonathan'",
    ]
}

def main():
    fresh()

def fresh():
    database.delete_all_tables()
    create_tables()
    
def fresh_seeded():
    database.delete_all_tables()
    create_tables()
    run_seeders()
    
def create_tables():
    for x, y in TABLES.items():
        database.create_table(x, y)
            
def run_seeders():
    for x, y in DATA.items():
        for i in y:
            database.insert(x, i)
            
main()
