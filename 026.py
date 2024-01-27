try:
    # Code that may raise an exception
    result = int("abc")  # This will raise a ValueError
except Exception as e:
    # Handling any exception
    print(f"An unexpected error occurred: {e}")
