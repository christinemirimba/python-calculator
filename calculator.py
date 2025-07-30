# Ask user to input two numbers 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Define operations 
sum = num1 + num2
difference = num1 - num2
product = num1 * num2

# Handle division (avoiding division by zero)
try:
    quotient = num1 / num2
except ZeroDivisionError:
    quotient = "Error: Division by zero"

# Display results
print("Results:")
print(f"sum = {num1} + {num2} = {sum}")
print(f"difference = {num1} - {num2} = {difference}")
print(f"product = {num1} * {num2} = {product}")
print(f"quotient = {num1} / {num2} = {quotient}")