# Validate input before processing
def validate_input(user_input):
    if not user_input.isalnum():
        raise ValueError("Invalid input. Only alphanumeric characters allowed.")
 
