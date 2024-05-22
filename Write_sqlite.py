import sqlite3

sqliteconnect = sqlite3.connect("First_database.db")
print("Database connected")

cursor = sqliteconnect.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS emp (id integer primary key AUTOINCREMENT,name text,age integer,gender text)
"""

cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO emp(name,age,gender) Values("Shaswat",14,"Male")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name,age,gender) Values("Neha",30,"Female")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name,age,gender) Values("Tanmay",19,"Male")
"""
cursor.execute(insert_table_query)
sqliteconnect.commit()

sqliteconnect.close()