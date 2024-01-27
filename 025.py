def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Valid age: {age}"
 
try:
    result = validate_age(-5)
    print(result)
except ValueError as ve:
    print(f"Error: {ve}")
