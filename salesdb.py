import sqlite3

conn = splite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    amount INTEGER,
    date TEXT
)
""")

data = [
    ("A", 100000, "2026-01-01"),
    ("B", 200000, "2026-01-02"),
    ("A", 150000, "2026-02-01"),
    ("C", 300000, "2026-02-02"),
]

cursor.executemany("INSERT INTO sales (product, amount, date) VALUES (?,?,?)",data)
conn.commit()
conn.close()