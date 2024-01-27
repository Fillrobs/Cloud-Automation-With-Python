# File: calculator.py
 
def add(a, b):
    """
    Adds two numbers.
 
    Args:
        a (float): The first number.
        b (float): The second number.
 
    Returns:
        float: The sum of a and b.
    """
    return a + b
 
def multiply(x, y):
    """
    Multiplies two numbers.
 
    Args:
        x (float): The first number.
        y (float): The second number.
 
    Returns:
        float: The product of x and y.
    """
    return x * y
 
# File: main_script.py
 
import calculator
 
# Using the add function
result_add = calculator.add(3, 5)
 
# Using the multiply function
result_multiply = calculator.multiply(2, 4)
