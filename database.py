import os
import sqlite3

PATH = os.path.dirname(os.path.realpath(__file__)) + "/python.db"

connection = sqlite3.connect(PATH)
cursor = connection.cursor()

def create_table(table, fields):
    if not (exist(table)):
        cursor.execute("CREATE TABLE {}({})".format(table, fields))
    
        print("Die Tabelle '{}' wurde erfolgreich erstellt.".format(table))
        
    else:
        print("Die Tabelle '{}' wurde nicht gefunden.".format(table))

def delete_table(table):
    if (exist(table)):
        cursor.execute("DROP TABLE {}".format(table))
    
        print("Die Tabelle '{}' wurde erfolgreich gelöscht.".format(table))
        
    else:
        print("Die Tabelle '{}' wurde nicht gefunden.".format(table))

def delete_all_tables():
    res = cursor.execute("SELECT name FROM sqlite_master")   

    tables = res.fetchall()
    
    if (tables is not None):
        for table in tables:
            delete_table(table[0])
    
def insert(table, entries):
    cursor.execute("INSERT INTO {} VALUES ({})".format(table, entries))
    
    connection.commit()

def exist(table):
    res = cursor.execute("SELECT name FROM sqlite_master WHERE name='{}'".format(table))
    
    table = res.fetchone()

    return table is not None
    