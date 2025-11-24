# Task 1: Ask the user for their name and greet them
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you!\n")

# Task 2: Perform basic arithmetic operations based on user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
multiplication_result = num1 * num2
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Undefined (cannot divide by zero)"

print(f"Sum: {sum_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}\n")

# Task 3: Ask the user to enter names separated by commas, split the string, and copy to a list
names_input = input("Enter names separated by commas: ")
names_list = names_input.split(",")
print("List of names:", names_list, "\n")

# Task 4: Ask the user to enter their age and check if they are eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.\n")

# Task 5: For value = 3.14159, using f-string print output for only up to 2 decimal places
value = 3.14159
print(f"{value:.2f}")

