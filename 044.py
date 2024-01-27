# FileOperations.py - This file contains reusable functions for file operations
 
import os
import shutil
 
def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.
 
    Parameters:
    - directory_path (str): The path of the directory to be created.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
 
def copy_file(source_path, destination_path):
    """
    Copy a file from the source path to the destination path.
 
    Parameters:
    - source_path (str): The path of the source file.
    - destination_path (str): The path where the file will be copied.
    """
    try:
        shutil.copy2(source_path, destination_path)
        print(f"File '{source_path}' copied to '{destination_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while copying '{source_path}' to '{destination_path}'.")
 
# main.py - This file demonstrates the use of the reusable functions
 
from FileOperations import create_directory, copy_file
 
# Example usage
source_file = "source_folder/source_file.txt"
destination_folder = "destination_folder"
 
# Create a destination folder if it doesn't exist
create_directory(destination_folder)
 
# Copy the file to the destination folder
copy_file(source_file, os.path.join(destination_folder, "copied_file.txt"))
