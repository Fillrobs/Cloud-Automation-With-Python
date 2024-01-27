# FileManipulation.py - This file contains a script for file manipulation with error handling and logging
 
import os
import shutil
import logging
 
# Set up logging
logging.basicConfig(filename='file_manipulation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
def copy_file(source_path, destination_path):
    try:
        # Check if the source file exists
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file '{source_path}' not found.")
 
        # Copy the file to the destination
        shutil.copy2(source_path, destination_path)
        logging.info(f"File '{source_path}' copied to '{destination_path}'.")
        print(f"File '{source_path}' copied to '{destination_path}'.")
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
    except PermissionError as e:
        logging.error(f"Error: Permission denied - {e}")
        print(f"Error: Permission denied - {e}")
    except Exception as e:
        logging.error(f"Error: An unexpected error occurred - {e}")
        print(f"Error: An unexpected error occurred - {e}")
 
# main.py - This file demonstrates the use of the script with error handling and logging
 
from FileManipulation import copy_file
 
# Example usage with error scenarios
source_file = "nonexistent_file.txt"
destination_folder = "destination_folder"
 
# Attempt to copy a non-existent file
copy_file(source_file, os.path.join(destination_folder, "copied_file.txt"))
