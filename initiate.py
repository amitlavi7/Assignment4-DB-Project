import sqlite3
import os
import sys

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
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            lineList = line.split(', ')
            if lineList[0] == "C":
                conn.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                             (lineList[1], lineList[2], lineList[3]))
            elif lineList[0] == 'S':
                conn.execute("INSERT INTO Suppliers VALUES(?,?,?)",
                             (lineList[1], lineList[2], lineList[3]))
            elif lineList[0] == 'E':
                conn.execute("INSERT INTO Employees VALUES(?,?,?,?)",
                             (lineList[1], lineList[2], lineList[3], lineList[4]))
            elif lineList[0] == 'P':
                conn.execute("INSERT INTO Products VALUES(?,?,?,?)",
                             (lineList[1], lineList[2], lineList[3], 0))



if os.path.isfile(DB_NAME):
    os.remove("moncafe.db")

if not os.path.isfile(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    insert_to_tables(conn)
    conn.commit()
    conn.close()
