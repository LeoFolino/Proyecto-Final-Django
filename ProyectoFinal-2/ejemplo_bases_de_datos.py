import sqlite3

conn = sqlite3.connect('mi-base-de-datos.sqlite3')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Rogelio', 32)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Marcela', 34)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Marcela', 34)")

conn.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close