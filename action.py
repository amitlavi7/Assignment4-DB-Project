import sqlite3
import os
import sys

DB_NAME = "moncafe.db"


def insert_to_tables(conn):
    with open("action.txt", "r") as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            lineList = line.split(', ')
            conn.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                         (lineList[0], lineList[1], lineList[2], lineList[3]))


def make_activities(cur):
    activities = cur.execute("""
    SELECT name FROM sqlite_master 
    WHERE type = "table" 
    AND name = "Activities"
    """)
    # for row in cur.execute("""SELECT name FROM sqlite_master WHERE type = "table" AND name = 'Activities'"""):
    #     if row[1] > 0:
    #         add_product("SELECT name FROM Activities WHERE proudct_id=(row[0])","SELECT name FROM Activities WHERE quantity=(row[1])")
    for row in activities:
            print(row)

def add_product(id, quantity):
    print("id = " + id + "quantity = " + quantity)

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
insert_to_tables(conn)
make_activities(conn)
conn.commit()
conn.close()
