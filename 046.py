# DatabaseConnectionParameterized.py - This file contains a script with parameterized database connection details
 
import psycopg2
 
def connect_to_database(host, port, database_name, user, password):
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
 
# main_parameterized.py - This file demonstrates the use of the script with parameterization
 
from DatabaseConnectionParameterized import connect_to_database
 
# Database connection details are provided as parameters
db_connection = connect_to_database(
    host="localhost",
    port="5432",
    database_name="mydatabase",
    user="myuser",
    password="mypassword"
)
