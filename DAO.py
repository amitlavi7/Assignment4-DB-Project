class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("INSERT INTO Employees VALUES(?,?,?,?)",
                           (employee.id, employee.name, employee.salary, employee.coffee_stand))
    # def print(self,)://TODO: need to make function print for each one

class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Coffee_stand):
        self._conn.execute("INSERT INTO Coffee_stands VALUES(?,?,?)",
                           (Coffee_stand.id, Coffee_stand.location, Coffee_stand.number_of_employees))


class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Product):
        self._conn.execute("INSERT INTO Products VALUES(?,?,?,?)",
                           (Product.id, Product.description, Product.price, Product.quantity))

class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Activity):
        self._conn.execute("INSERT INTO Activities VALUES(?,?,?,?)",
                           (Activity.product_id, Activity.quantity, Activity.activator_id, Activity.date))

class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Supplier):
        self._conn.execute("INSERT INTO Suppliers VALUES(?,?,?)",
                           (Supplier.id, Supplier.name, Supplier.contact_information))
