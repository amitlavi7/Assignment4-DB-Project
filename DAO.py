from DTO import Employee, Product, Coffee_stand, Supplier, Activity


class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("INSERT INTO Employees VALUES(?,?,?,?)",
                           (employee.id, employee.name, employee.salary, employee.coffee_stand))

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, salary, coffee_stand FROM Employees ORDER BY Employees.id
        """).fetchall()

        return [Employee(*row) for row in all]


class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Coffee_stand):
        self._conn.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                           (Coffee_stand.id, Coffee_stand.location, Coffee_stand.number_of_employees))

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Coffee_stands ORDER BY Coffee_stands.id
        """).fetchall()

        return [Coffee_stand(*row) for row in all]

class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Product):
        self._conn.execute("INSERT INTO Products VALUES(?,?,?,?)",
                           (Product.id, Product.description, Product.price, Product.quantity))

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Products ORDER BY Products.id
        """).fetchall()

        return [Product(*row) for row in all]


class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Activity):
        self._conn.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                           (Activity.product_id, Activity.quantity, Activity.activator_id, Activity.date))

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Activities ORDER BY Activities.date
        """).fetchall()

        return [Activity(*row) for row in all]

class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Supplier):
        self._conn.execute("INSERT INTO Suppliers VALUES(?,?,?)",
                           (Supplier.id, Supplier.name, Supplier.contact_information))

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Suppliers ORDER BY Suppliers.id
        """).fetchall()

        return [Supplier(*row) for row in all]
