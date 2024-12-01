import mysql.connector
from dotenv import load_dotenv
import queries as qr
import os

load_dotenv()

# connect to local database
def connect(user, password, host, port, database, create_table_query):
    try:
        connection = mysql.connector.connect(
            user=user,
            password=password,
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
    try:
        task = input("Enter the name of your task: ")
        desc = input("What is this task for? ")
        freq = input("Daily or Weekly? ").lower()

        if freq not in ['daily', 'weekly']:
            print("Invalid input. Please enter 'Daily' or 'Weekly'.")
            return

        with connection.cursor() as cursor:
            cursor.execute(qr.AddTask, (task, desc, freq))
            connection.commit()
        
        print("Task added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def deleteTask(connection):
    return None

def showTask(connection, *args):
    return None

# close connection to local database
def close(connection):
    if connection:
        connection.close()
        print("Closed")
        

if __name__ == "__main__":
    connection = connect(
            os.getenv("DB_USER"),
            os.getenv("DB_PASS"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_NAME"),
            qr.CreateTable
        )
    

    addTask(connection)
    close(connection)
