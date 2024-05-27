import sqlite3 as sql
sqlconnection = sql.connect("Students.db")
cursor = sqlconnection.cursor()
create_table_query ="""
CREATE TABLE IF NOT EXISTS students(name text,gender text,address text,phone integer,
grade text,birthday text,math integer,science integer,english integer,computer integer,
average integer)"""
cursor.execute(create_table_query)
def insert_data(data: tuple)-> None:
    insert_data_query = """
    INSERT INTO students Values(?,?,?,?,?,?,?,?,?,?,?)"""
    cursor.execute(insert_data_query,data)