import sqlite3

sqliteconnect = sqlite3.connect("First_database.db")
print("Database connected")

cursor = sqliteconnect.cursor()
print("Database initialized")

read_data_query = """SELECT * FROM emp;"""
cursor.execute(read_data_query)
print(cursor.fetchall())

sqliteconnect.close()