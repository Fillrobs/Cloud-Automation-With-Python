#!/bin/bash
 
# Define a variable
NAME="John"
 
# Print a message using the variable
echo "Hello, $NAME! Welcome to the Bash scripting world."
 
# Using a conditional statement
if [ "$NAME" == "John" ]; then
    echo "You are using the default name."
else
    echo "You have a different name."
fi
 
# Using a loop to print numbers from 1 to 5
echo "Counting from 1 to 5:"
for i in {1..5}; do
    echo $i
done
 
# Function definition
greet() {
    echo "Have a great day, $NAME!"
}
 
# Function call
greet
 
# Command-line argument processing
if [ "$1" == "help" ]; then
    echo "This script greets the user."
    echo "Usage: ./script_name.sh [name]"
fi

