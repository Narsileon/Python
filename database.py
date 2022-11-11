import os
import sqlite3

ONLINE_VIEVER = "https://inloop.github.io/sqlite-viewer/"

PATH = os.path.dirname(os.path.realpath(__file__)) + "/Database/database.db"

connection = sqlite3.connect(PATH)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def create_table(table, fields):
    if not (exist(table)):
        cursor.execute("CREATE TABLE {}({})".format(table, fields))
    
        print("Die Tabelle '{}' wurde erfolgreich erstellt.".format(table))
        
    else:
        print("Die Tabelle '{}' existiert bereits.".format(table))

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
    
def select_all(table):
    res = cursor.execute("SELECT * FROM {}".format(table))
    return res.fetchall()

def exist(table):
    res = cursor.execute("SELECT name FROM sqlite_master WHERE name='{}'".format(table))
    
    table = res.fetchone()

    return table is not None
    