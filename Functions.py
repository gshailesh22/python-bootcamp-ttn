# 1. Function to calculate the area of a rectangle
def calculate_area(length, width=10):
    return length * width

print("Area Calculation :")
print(calculate_area(5))  
print(calculate_area(5, 3))  
print()

# 2. Recursive function to compute factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial :")
print(factorial(5))  
print(factorial(0))  
print(factorial(1))  
print()

# 3. Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("String Reversal :")
print(reverse_string("hello"))  
print(reverse_string("world"))  
print(reverse_string("civic"))  
print()

# 4. Function to sum all numbers in two lists
def sum_lists(a, b):
    return sum(a) + sum(b)

print("Sum of Numbers in Lists :")
a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print(sum_lists(a, b))  
print()

# 5. Function to return a sorted list with distinct elements
def distinct_sorted_list(lst):
    return sorted(set(lst))

print("Distinct and Sorted List :")
a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
print(distinct_sorted_list(a))  
print(distinct_sorted_list([10, 2, 2, 5, 5, 3]))  

