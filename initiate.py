import sqlite3
import os
import sys

from DAO import Employees, Coffee_stands, Products, Suppliers
from DTO import Employee, Coffee_stand, Supplier, Product

DB_NAME = "moncafe.db"


def create_tables(conn):
    conn.executescript("""
                    CREATE TABLE Employees(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL, 
                    salary REAL NOT NULL, 
                    coffee_stand INTEGER REFERENCES Coffee_stand(id)
                    );

                    CREATE TABLE Suppliers(
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    contract_information TEXT
                    );

                    CREATE TABLE Products(
                    id INTEGER PRIMARY KEY, 
                    description TEXT NOT NULL, 
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL
                    );

                    CREATE TABLE Coffee_stands(
                    id INTEGER PRIMARY KEY, 
                    location TEXT NOT NULL, 
                    number_of_employees INTEGER
                    );
                    CREATE TABLE Activities(
                    product_id INTEGER INTEGER REFERENCES product(id), 
                    quantity INTEGER NOT NULL,
                    activator_id INTEGER NOT NULL, 
                    date DATE NOT NULL
                    );
                """)


def insert_to_tables(conn):
    with open("config.txt", "r") as file:
        Employees_holder = Employees(conn)
        Coffee_stands_holder = Coffee_stands(conn)
        Products_holder = Products(conn)
        Suppliers_holder = Suppliers(conn)
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            lineList = line.split(', ')
            if lineList[0] == "C":
                coffee_stand = Coffee_stand(lineList[1], lineList[2], lineList[3])
                Coffee_stands_holder.insert(coffee_stand)
                # conn.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                #              (lineList[1], lineList[2], lineList[3]))
            elif lineList[0] == 'S':
                supplier = Supplier(lineList[1], lineList[2], lineList[3])
                Suppliers_holder.insert(supplier)
                # conn.execute("INSERT INTO Suppliers VALUES(?,?,?)",
                #              (lineList[1], lineList[2], lineList[3]))
            elif lineList[0] == 'E':
                employee = Employee(lineList[1], lineList[2], lineList[3], lineList[4])
                Employees_holder.insert(employee)
                # conn.execute("INSERT INTO Employees VALUES(?,?,?,?)",
                #              (lineList[1], lineList[2], lineList[3], lineList[4]))
            elif lineList[0] == 'P':
                product = Product(lineList[1], lineList[2], lineList[3], 0)
                Products_holder.insert(product)
                # conn.execute("INSERT INTO Products VALUES(?,?,?,?)",
                #              (lineList[1], lineList[2], lineList[3], 0))



if os.path.isfile(DB_NAME):
    os.remove("moncafe.db")

if not os.path.isfile(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    insert_to_tables(conn)
    conn.commit()
    conn.close()
