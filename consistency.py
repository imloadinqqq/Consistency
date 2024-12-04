import mysql.connector
from dotenv import load_dotenv
import queries as qr
import os
from tabulate import tabulate

load_dotenv(dotenv_path='./.env')

# connect to local database
def connect(user, host, port, database, create_table_query):
    try:
        connection = mysql.connector.connect(
            user=user,
            host=host,
            port=port,
            database=database
        )
        if connection.is_connected():
            print("Connected")
            
            if create_table_query:
                with connection.cursor() as cursor:
                    cursor.execute(create_table_query)
                    print("Created Table")

            return connection

    except mysql.connector.Error as err:
        print(f"Error Connecting: {err}")
        return None

# add task to database
def addTask(connection):
    if not connection.is_connected():
        print("Re-establishing the database connection...")
        connection.reconnect(attempts=3, delay=5)
    if connection:
        try:
            task = input("Enter the name of your task: ")
            desc = input("What is this task for? ")
            freq = input("Daily or Weekly? ").lower()

            if freq not in ['daily', 'weekly']:
                print("Invalid input. Please enter 'Daily' or 'Weekly'.")
                return
            data = (task, desc, freq)
            print("right before connection.cursor in addTask()")
            with connection.cursor() as cursor:
                print("Begin cursor in addTask")
                
                cursor.execute(qr.AddTask, data)
                connection.commit()
                    
                cursor.execute(qr.ShowTasks)
                results = cursor.fetchall()
                for row in results:
                    print(row)

            
            print("Task added successfully.")
        except mysql.connector.Error as err:
            print(f"Error in addTask: {err}, {err.errno}")

# delete a task based on id
def deleteTask(connection, task):
    try:
        with connection.cursor() as cursor:
            cursor.execute(qr.DeleteTask, task)
            print(f"Task {task} deleted")
    except mysql.connector.Error as err:
        print(f"Error in deleteTask: {err}")

# show tasks in db form, can take input for specific id
def showTask(connection, *args):
    try:
        with connection.cursor() as cursor:
            cursor.execute(qr.ShowTasks)
    except mysql.connector.Error as err:
        print(f"Error in showTask: {err}")
    
# print tabular format of weekly tasks
def printTableForm(data, headers):
    if data:
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No tasks available.")

if __name__ == "__main__":
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_PORT:", os.getenv("DB_PORT"))
    print("DB_NAME:", os.getenv("DB_NAME"))

    conn = connect(
            os.getenv("DB_USER"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_NAME"),
            qr.CreateTable
        )
    if conn:
        try:
            print("beginning try block main")
            addTask(conn)
            deleteTask(conn, [1])
        finally:
            conn.close()
    else:
        print("Connection failed")
