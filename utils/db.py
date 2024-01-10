# Check it out, this file creates a database for you in no time, just start it up
# It will probably help you if you need it.

import sqlite3

conn = sqlite3.connect('../data/database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.commit()
cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ('john', '123'))
conn.commit()
