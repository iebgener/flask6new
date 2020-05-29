import sqlite3
import os

os.remove('data.db')
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

user = (None, 'bob', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(create_table)
connection.commit()
cursor.execute(insert_query, user)
connection.commit()

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)
connection.commit()

add_item = "INSERT INTO items VALUES (NULL, 'table', 33.99)"
cursor.execute(add_item)
connection.commit()
connection.close()
