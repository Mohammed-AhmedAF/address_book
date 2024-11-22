import sqlite3

conn = sqlite3.connect("customer.db")

cur = conn.cursor()

# Create a table
def createDB(cur):
    cur.execute("""CREATE TABLE customers (
            first_name TEXT,
            last_name TEXT,
            email TEXT
            )""")
    conn.commit()


def addOneCustomer():
    cur.execute("INSERT INTO customers VALUES ('John','Elder','john@codemy.com')")  
    conn.commit()

addOneCustomer()
cur.execute("SELECT * FROM customers")
print(cur.fetchall()[0])


conn.close()