import sqlite3
sqliteconnection = sqlite3.connect("Employee.db")
print("Database connected")
cursor = sqliteconnection.cursor()
print("Database intialized")
create_table_query = """
CREATE TABLE IF NOT EXISTS emp (id integer,name text,age integer,gender text)
"""
cursor.execute(create_table_query)
def add_new_entry(entered_id: int,N: str,A: int,G: str) -> None:
    Employee = (entered_id, N, A, G)
    insert_table_query = """
    INSERT INTO emp Values(?,?,?,?)
    """
    cursor.execute(insert_table_query, Employee)
    sqliteconnection.commit()
def listing_all_queries():
    read_data_query = """SELECT * FROM emp;"""
    cursor.execute(read_data_query)
    print(cursor.fetchall())
def deleting_data(deleting_id: int)-> None:
    delete_data = (deleting_id, )
    cursor.execute("DELETE FROM emp WHERE id = ?",delete_data)
word = ''
while word.lower() != 'exit':
    print(f"Enter add to store new entry in database\nEnter list to see all the entries in the database")
    print(f"Enter delete to delete a entry in database\nEnter exit to exit")
    word = input("Enter the function: ")
    match(word):
        case 'add':
            id_1 = int(input("Enter the id of employee: "))
            name = input("Enter the name of employee: ")
            age = int(input("Enter the age: "))
            gender = input("Enter the gender: ")
            add_new_entry(id_1,name,age,gender)
            print("Information added")
        case 'list':
            print("Here's the data")
            listing_all_queries()
        case 'delete':
            listing_all_queries()
            deleting_id = int(input("Enter the id to be deleted: "))
            deleting_data(deleting_id)
        case 'exit':
            break
sqliteconnection.close()