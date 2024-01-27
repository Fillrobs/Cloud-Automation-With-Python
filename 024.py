try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handling other exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # Executed if no exception is raised
    print("Division successful.")
finally:
    # This block is always executed, whether an exception occurred or not
    print("This block is always executed.")
 
