import mysql.connector
from dotenv import load_dotenv
import queries as qr
import os

load_dotenv()

def connect(user, password, host, database):
    try:
        connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        if connection.is_connected():
            print("Connected")
            return connection

    except mysql.connector.Error as err:
        print(f"Error Connecting: {err}")
        return None

def addTask(connection):
    

def close(connection):
    if connection:
        connection.close()
        print("Closed")
        

if __name__ == "__main__":
    connection = connect(
            os.getenv("DB_USER"),
            os.getenv("DB_PASS"),
            os.getenv("DB_HOST"),
            os.getenv("DB_NAME")
        )
    close(connection) 
