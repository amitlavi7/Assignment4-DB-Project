import atexit
import os
import sqlite3

from DAO import Employees, Suppliers, Products, Coffee_stands, Activities

DB_NAME = "moncafe.db"


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(DB_NAME)
        self.Employees = Employees(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Products = Products(self._conn)
        self.Coffee_stands = Coffee_stands(self._conn)
        self.Activities = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
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


repo = _Repository()
atexit.register(repo._close)