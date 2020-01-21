import atexit
import os
import sqlite3

from DAO import Employees, Suppliers, Products, Coffee_stands, Activities
from DTO import Activity_report, Activity, Product

DB_NAME = "moncafe.db"


class _Repository:
    # def __init__(self):
    #     if os.path.isfile(DB_NAME):
    #         os.remove(DB_NAME)
    #     self._conn = sqlite3.connect(DB_NAME)
    #     self.Employees = Employees(self._conn)
    #     self.Suppliers = Suppliers(self._conn)
    #     self.Products = Products(self._conn)
    #     self.Coffee_stands = Coffee_stands(self._conn)
    #     self.Activities = Activities(self._conn)

    def connect(self):
        # if os.path.isfile(DB_NAME):
        #     os.remove(DB_NAME)
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
        # if os.path.isfile(DB_NAME):
        #     os.remove(DB_NAME)
        # if not os.path.isfile(DB_NAME):
        #     self._conn = sqlite3.connect(DB_NAME)
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

    def get_activity_report(self):
        cur = self._conn.cursor()
        all = cur.execute("""
            SELECT Activities.date, Products.description, Activities.quantity, Employees.name, Suppliers.name
                FROM Activities
                LEFT JOIN Products ON Activities.product_id = Products.id
                LEFT JOIN Employees ON Activities.activator_id = Employees.id
                LEFT JOIN Suppliers ON Activities.activator_id = Suppliers.id
            ORDER BY Activities.date
        """).fetchall()

        return [Activity_report(*row) for row in all]

    def get_sales_income(self):
        cur = self._conn.cursor()
        all = cur.execute("""
        SELECT * FROM Activities
        """).fetchall()

        activity = [Activity(*row) for row in all]
        sellers_income = []
        for act in activity:
            if act.quantity < 0:
                jojo = cur.execute("""
                SELECT * FROM Products WHERE id = ({})""".format(act.product_id))

                pro = Product(*jojo.fetchone())
                print(pro.price)
                sellers_income.append(int(act.quantity) * -1 * float(pro.price))

        print(sellers_income)


repo = _Repository()
atexit.register(repo._close)
