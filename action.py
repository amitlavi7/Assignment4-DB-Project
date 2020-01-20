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
    activities = cur.execute('SELECT * FROM Activities')
    activity_list = activities.fetchall()
    for activity in activity_list:
        add_product(cur, activity[0], activity[1])


def add_product(cur, activity_id, quantity):
    quantity_cursor = cur.execute("SELECT quantity From Products WHERE id = ({})".format(activity_id))
    quantity_product = quantity_cursor.fetchone()[0] + quantity
    if quantity > 0:
        cur.execute("""
        UPDATE Products
        SET quantity = ({}) WHERE id = ({})
        """.format(quantity_product, activity_id))
    else:
        if quantity_product >= 0:
            cur.execute("""UPDATE Products
                        SET quantity =({}) WHERE id =({})
            """.format(quantity_product, activity_id))


conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
count = cur.execute("SELECT count(*) FROM Activities").fetchone()[0]
if count == 0:
    insert_to_tables(conn)
    make_activities(conn)
    conn.commit()
    conn.close()
