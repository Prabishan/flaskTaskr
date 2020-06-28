import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor() #cursor object to execute SQL command

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

    c.execute('INSERT INTO tasks(name,due_date,priority,status) VALUES("Finish this project","06/29/2020", 10, 1)')
