import sqlite3
import os
import sys

from DAO import Employees, Coffee_stands, Products, Suppliers, Activities

DB_NAME = "moncafe.db"


def print_Coffee_stands(conn):
    all_Coffee_stands = Coffee_stands(conn).find_all()
    print("Coffee stand")
    for Coffee_stand in all_Coffee_stands:
        print(Coffee_stand)


def print_Activities(conn):
    print("Activities")
    all_Activities = Activities(conn).find_all()
    for Activity in all_Activities:
        print(Activity)


def print_Employees(conn):
    print("Employees")
    all_employees = Employees(conn).find_all()
    for employee in all_employees:
        print(employee)


def print_Products(conn):
    print("Products")
    all_Products = Products(conn).find_all()
    for Product in all_Products:
        print(Product)


def print_Suppliers(conn):
    print("Suppliers")
    all_Suppliers = Suppliers(conn).find_all()
    for Supplier in all_Suppliers:
        print(Supplier)


def print_all_tables(conn):
    print_Activities(conn)
    print_Coffee_stands(conn)
    print_Employees(conn)
    print_Products(conn)
    print_Suppliers(conn)


# def print_employees_report():
#     asd
#
# def print_activity_report():


conn = sqlite3.connect(DB_NAME)
print_all_tables(conn)
# print_employees_report()
