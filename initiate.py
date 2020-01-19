import sqlite3
import os

databaseexisted = os.path.isfile('moncafe.db')

dbcon = sqlite3.connect('moncafe.db')

with dbcon:
    cursor = dbcon.cursor()
    if not databaseexisted:  # First time creating the database. Create the tables
        cursor.execute(
            "CREATE TABLE Employees(id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary REAL NOT NULL, coffee_stand INTEGER REFERENCES Coffee_stand(id))")  # create table Employees
        cursor.execute(
            "CREATE TABLE Suppliers(id INTEGER PRIMARY KEY, name TEXT NOT NULL, contract_information TEXT)")  # create table Suppliers
        cursor.execute(
            "CREATE TABLE Products(id INTEGER PRIMARY KEY, description TEXT NOT NULL, price REAL NOT NULL, quantity INTEGER NOT NULL)")  # create table Products
        cursor.execute(
            "CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY, location TEXT NOT NULL, number_of_employees INTEGER)")  # create table Coffee_stands
        cursor.execute(
            "CREATE TABLE Activities(product_id INTEGER INTEGER REFERENCES Product(id), quantity INTEGER NOT NULL, activator_id INTEGER NOT NULL, date DATE NOT NULL )")  # create table Activities
        config = os.open("config.txt", "r")
        print(config.read())
        for line in config:
            print(line.read())
