# DatabaseConnection.py - This file contains a script with hardcoded database connection details
 
import psycopg2
 
def connect_to_database():
    # Hardcoded database connection details
    host = "localhost"
    port = "5432"
    database_name = "mydatabase"
    user = "myuser"
    password = "mypassword"
 
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database_name,
            user=user,
            password=password
        )
        print("Connected to the database.")
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        return None
 
# main.py - This file demonstrates the use of the script without parameterization
 
from DatabaseConnection import connect_to_database
 
# Connect to the database using the script with hardcoded details
db_connection = connect_to_database()
