import sqlite3
import os
import sys

DB_NAME = "moncafe.db"


def print_Coffee_stands(cur):
    cur.execute('SELECT * FROM Coffee_stands ORDER BY Coffee_stands.id ')
    list = cur.fetchall()
    print("Coffee_stands")
    i = 0
    for item in list:
        i = i + 1
        print("{}".format(str(item)))

def print_Activities(cur):
    cur.execute('SELECT * FROM Activities ORDER BY Activities.date')
    list = cur.fetchall()
    print("Activities")
    i = 0
    for item in list:
        i = i + 1
        print("{}".format(str(item)))

def print_Employees(cur):
    cur.execute('SELECT * FROM Employees ORDER BY Employees.id ')
    list = cur.fetchall()
    print("Employees")
    i = 0
    for item in list:
        i = i + 1
        print("{}".format(str(item)))

def print_Products(cur):
    cur.execute('SELECT * FROM Products ORDER BY Products.id ')
    list = cur.fetchall()
    print("Products")
    i = 0
    for item in list:
        i = i + 1
        print("{}".format(str(item)))

def print_Suppliers(cur):
    cur.execute('SELECT * FROM Suppliers ORDER BY Suppliers.id ')
    list = cur.fetchall()
    print("Suppliers")
    i = 0
    for item in list:
        i = i + 1
        print("{}".format(str(item)))

def print_all_tables(cur):
    print_Activities(cur)
    print_Coffee_stands(cur)
    print_Employees(cur)
    print_Products(cur)
    print_Suppliers(cur)


conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
print_all_tables(cur)
