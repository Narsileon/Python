import sqlite3
from localization import t

import os

ONLINE_VIEVER = "https://inloop.github.io/sqlite-viewer/"

PATH = os.path.dirname(os.path.realpath(__file__)) + "/Database/database.db"

connection = sqlite3.connect(PATH)

connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def create_table(table, fields):
    if not (exist(table)):
        cursor.execute("CREATE TABLE {}({})".format(table, fields))
    
        print(t("table_created").format(table))
        
    else:
        print(t("table_exist").format(table))

def delete_table(table):
    if (exist(table)):
        cursor.execute("DROP TABLE {}".format(table))
    
        print(t("table_deleted").format(table))
        
    else:
        print(t("table_not_found").format(table))

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
    