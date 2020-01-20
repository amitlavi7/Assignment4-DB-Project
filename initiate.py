import sqlite3
import os
import sys

from DAO import Employees, Coffee_stands, Products, Suppliers
from DTO import Employee, Coffee_stand, Supplier, Product
from Repository import repo

DB_NAME = "moncafe.db"

def insert_to_tables():
    with open("config.txt", "r") as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            lineList = line.split(', ')
            if lineList[0] == "C":
                coffee_stand = Coffee_stand(lineList[1], lineList[2], lineList[3])
                repo.Coffee_stands.insert(coffee_stand)
            elif lineList[0] == 'S':
                supplier = Supplier(lineList[1], lineList[2], lineList[3])
                repo.Suppliers.insert(supplier)
            elif lineList[0] == 'E':
                employee = Employee(lineList[1], lineList[2], lineList[3], lineList[4])
                repo.Employees.insert(employee)
            elif lineList[0] == 'P':
                product = Product(lineList[1], lineList[2], lineList[3], 0)
                repo.Products.insert(product)


if os.path.isfile(DB_NAME):
    os.remove(DB_NAME)
#
if not os.path.isfile(DB_NAME):
    repo.__init__()
    repo.create_tables()
    insert_to_tables()
