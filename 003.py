# Variables and Data Types
name = "Alice"  # String variable
age = 30  # Integer variable
height = 1.75  # Float variable
is_student = True  # Boolean variable
 
# Operators
result = age + 5  # Addition operator
is_tall = height >= 1.8  # Comparison operator (>=)
greeting = "Hello, " + name  # Concatenation operator (+)
 
# Conditional Statement
if is_student:
    print("Student")
else:
    print("Not a student")
 
# Loops
print("Counting from 1 to 5:")
for i in range(1, 6):  # For loop to print numbers 1 to 5
    print(i)
 
# Function Definition
def greet(person_name, person_age):
    print(f"Hello, {person_name}!")
    print(f"You are {person_age} years old.")
 
# Function Call
greet(name, age)
