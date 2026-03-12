# Input first number
result = float(input("Enter first number: "))

for i in range(9): # Nine other numbers
    result -= float(input("Enter a number: ")) # Subtract numbers to first number

print("The result is", result)# Print result
