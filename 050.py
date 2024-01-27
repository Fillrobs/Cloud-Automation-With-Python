# File: automation_utils.py
 
def validate_input(value):
    # Common input validation logic
    if not value:
        raise ValueError("Input value cannot be empty")
 
def log_info(message):
    # Common logging logic
    print(f"[INFO] {message}")
 
def execute_command(command):
    # Common code to execute a command
    print(f"Executing command: {command}")
    # Add logic for command execution
