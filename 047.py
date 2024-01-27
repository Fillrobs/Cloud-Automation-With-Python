import psycopg2
import configparser
 
def read_database_config():
    # Read database configuration from a config file
    config = configparser.ConfigParser()
    config.read('database_config.ini')
 
    return {
        'host': config.get('Database', 'host'),
        'port': config.get('Database', 'port'),
        'database_name': config.get('Database', 'database_name'),
        'user': config.get('Database', 'user'),
        'password': config.get('Database', 'password')
    }
 
def connect_to_database(config):
    try:
        connection = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database_name'],
            user=config['user'],
            password=config['password']
        )
        print("Connected to the database.")
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        return None
 
# main_config_file.py - This file demonstrates the use of the script with centralized configuration
 
from DatabaseConnectionConfigFile import read_database_config, connect_to_database
 
# Read database configuration from the config file
db_config = read_database_config()
 
# Connect to the database using the configuration
db_connection = connect_to_database(db_config)
