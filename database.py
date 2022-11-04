import sqlite3
import database_seeder

DB = "python.db"
cursor = None

def main():
    connect()
    
    for x, y in database_seeder.TABLES.items():
        if not(exist(x)):
            create_table(x, y)
    
    for x, y in database_seeder.DATA.items():
        for i in y:
            insert(x, i)

def connect():
    global cursor
    
    session = sqlite3.connect(DB)
    cursor = session.cursor()

def create_table(title, fields):
    cursor.execute("CREATE TABLE {}({})".format(title, fields))
    
    print("Die Tabelle {} wurde erfolgreich erstellt.".format(title))
    
def insert(table, entries):
    cursor.execute("""
        INSERT INTO {} VALUES
        {}
        """.format(table, entries))

def exist(table):
    res = cursor.execute("SELECT name FROM sqlite_master WHERE name='{}'".format(table))
    
    return res.fetchone() 

main()
    