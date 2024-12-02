from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

if __name__ == "__main__":
    conn = mysql.connector.connect(
        user=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()

    cursor.execute("DROP DATABASE habits;")
    conn.close()
