import os
import shutil
import subprocess
 
# Files and Directories
file_path = 'example.txt'
directory_path = 'example_dir'
 
# Create a file and directory
with open(file_path, 'w') as file:
    file.write('Example content')
os.mkdir(directory_path)
 
# Check file existence and permissions
if os.path.exists(file_path):
    print(f"{file_path} exists")
    print(f"Permissions for {file_path}: {os.access(file_path, os.R_OK)}")
 
# Processes
try:
    output = subprocess.check_output(['ls', '-l'])
    print("Process output:")
    print(output.decode('utf-8'))
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
 
# Environment Variables
os.environ['MY_VARIABLE'] = '123'
print(f"Value of MY_VARIABLE: {os.environ.get('MY_VARIABLE')}")
 
# System Configurations (requires elevated permissions)
# Example: uncomment to try changing system time (requires appropriate permissions)
# subprocess.run(['date', '2024-01-01'])
