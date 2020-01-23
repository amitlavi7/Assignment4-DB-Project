import sqlite3
import sys

from DTO import Activity
from Repository import repo

DB_NAME = "moncafe.db"


def insert_to_tables():
    repo.connect()
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line[-1] == '\n':
                line = line[:-1]
            lineList = line.split(', ')
            activity = Activity(lineList[0], lineList[1], lineList[2], lineList[3])
            quantity_of_product = repo.Products.find(lineList[0]).quantity
            quantity_of_product_after_activity = quantity_of_product + int(lineList[1])
            if int(lineList[1]) > 0:
                repo.Products.update(quantity_of_product_after_activity, lineList[0])
                repo.Activities.insert(activity)
            else:
                if quantity_of_product_after_activity >= 0:
                    repo.Products.update(quantity_of_product_after_activity, lineList[0])
                    repo.Activities.insert(activity)
    repo._close()


insert_to_tables()
import printdb

