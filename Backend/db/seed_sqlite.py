import sqlite3, csv

conn = sqlite3.connect("data/inventory.db")
cur = conn.cursor()

with open("db/sqlite_init.sql") as f:
    cur.executescript(f.read())

with open("data/products_seed.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, NULL)", (
            row["sku"], row["name"], row["category"], row["unit"],
            row["safety_stock"], row["reorder_point"], row["lead_time_days"]
        ))

with open("data/suppliers_seed.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("INSERT INTO suppliers(name,email,phone,lead_time_days,rating) VALUES (?,?,?,?,?)", (
            row["name"], row["email"], row["phone"], row["lead_time_days"], row["rating"]
        ))

conn.commit()
print("SQLite seeded successfully")
