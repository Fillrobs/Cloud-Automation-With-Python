# Define a variable
$Name = "John"
 
# Print a message using the variable
Write-Host "Hello, $Name! Welcome to the PowerShell scripting world."
 
# Using a conditional statement
if ($Name -eq "John") {
    Write-Host "You are using the default name."
} else {
    Write-Host "You have a different name."
}
 
# Using a loop to print numbers from 1 to 5
Write-Host "Counting from 1 to 5:"
1..5 | ForEach-Object {
    Write-Host $_
}
 
# Function definition
function Greet {
    param(
        [string]$Person
    )
    Write-Host "Have a great day, $Person!"
}
 
# Function call
Greet -Person $Name
 
# Command-line argument processing
if ($args.Count -gt 0 -and $args[0] -eq "help") {
    Write-Host "This script greets the user."
    Write-Host "Usage: script_name.ps1 [name]"
}
