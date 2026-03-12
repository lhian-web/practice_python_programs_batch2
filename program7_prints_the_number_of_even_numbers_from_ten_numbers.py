# Even count variable
even_count = 0

# Input numbers
for i in range(10):
    num = float(input("Enter a number: "))
    if num % 2 == 0: # Check if number is even
        even_count += 1

print("The number of even numbers is", even_count) # Print even count

