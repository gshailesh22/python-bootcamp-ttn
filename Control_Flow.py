# 1. Check if a number is even or odd
num = int(input("Enter a number to check if it's even or odd: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.\n")

# 2. Reverse a string using a for loop and check if it is a palindrome
strings = ["civic", "hello"]
for s in strings:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    if s == reversed_str:
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
print()

# 3. Generate the first N numbers of the Fibonacci sequence
n = int(input("Enter how many Fibonacci numbers you want: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 4. Find two numbers from the list that sum to 9
numbers = [1, 2, 3, 4, 5]
target_sum = 9
print("Finding two numbers that add up to 9:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            print(f"Pair that adds up to {target_sum}: {numbers[i]}, {numbers[j]}")
            break
print()

# 5. Print all even numbers between 1 and 20 using a while loop
print("Even numbers between 1 and 20 using while loop:")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print("\n")

# 6. Find the first occurrence of a number in a list and stop further searching
numbers = [10, 20, 30, 40, 50]
search_for = 30
print(f"Searching for {search_for} in the list:")
for num in numbers:
    if num == search_for:
        print(f"Found {num} in the list.")
        break
print()

# 7. Using continue statement, print only the odd numbers from 1 to 10
print("Odd numbers from 1 to 10 using continue statement:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

# 8. What will be the output for the given code using pass
print("Output of pass statement example:")
for i in range(5):
    if i == 3:
        pass  # The pass statement does nothing, just continues the loop.
    print(i)
print()

# 9. Using match statement to determine if it's a weekday or weekend
day = input("Enter a day of the week: ").lower()
print("Day of the week check using match:")
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is a weekday.")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is a weekend.")
    case _:
        print("Invalid day.")

