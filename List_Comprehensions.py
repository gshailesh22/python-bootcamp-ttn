# 1. Convert a list of numeric strings into integers using list comprehension
strings = ["1", "2", "3", "4", "5"]
numbers = [int(s) for s in strings]
print("Converted numbers:", numbers)

# 2. Extract all integers from a list that are greater than 10 using list comprehension
numbers_list = [1, 5, 13, 4, 16, 7]
greater_than_10 = [num for num in numbers_list if num > 10]
print("Numbers greater than 10:", greater_than_10)

# 3. Create a list of squares for numbers from 1 to 5 using list comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares of numbers from 1 to 5:", squares)

# 4. Convert a 2D list into a 1D list using list comprehension
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened = [element for row in matrix for element in row]
print("Flattened 2D list:", flattened)

# 5. Create a dictionary from two lists using dictionary comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print("Created dictionary:", dictionary)

# 6. Create a new dictionary containing only the students who scored above 80
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
high_scores = {student: score for student, score in scores.items() if score > 80}
print("Students who scored above 80:", high_scores)

