# ---- lambda, map, filter, reduce --------------

# Given a list let's see how to double each element of the given list. Using map()

a = [1, 2, 3, 4]
doubled_list = list(map(lambda x: x * 2, a))
print("Doubled list is: ", doubled_list)


# Use filter() and lambda to extract all even numbers from a list of integers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers in the list are: ", even_numbers)


# Use reduce() and lambda to find the longest word in a list of strings.

from functools import reduce
words = ["apple", "bananaa", "cherry", "date"]
longest_word = reduce(lambda acc, x: acc if len(acc) > len(x) else x, words)
print("Longest word: ", longest_word)


# Use map() to square each number in the list and round the result to one decimal place.

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_my_floats = list(map(lambda x: round(x ** 2, 1), my_floats))
print("Squares of the floating numbers are: ", squared_my_floats)


# Use filter() to select names with 7 or fewer characters from the list.

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filtered_names = list(filter(lambda x: len(x) <= 7, my_names))
print("Names with 7 or fewer characters: ", filtered_names)


# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]
sum_of_nums = reduce(lambda acc, x: acc + x, nums)
print("Sum of all numbers in list is: ", sum_of_nums)



# ---------all and any -----------

# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()

import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
print(all(numbers >= 0))


# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()

numbers = np.array([1, 3, 5, 7, 8])
print(any(numbers % 2 == 0))


# Determine if any number in a list is divisible by 5 an print.

numbers = np.array([11, 23, 15, 7, 8])
print(any(numbers % 5 == 0))



#--------------Enumerate--------------

# 1. Using below list and enumerate(), print index followed by value. 

fruits = ["apple", "banana", "cherry"]
for index, element in enumerate(fruits):
    print(index, element)


# 2. Using below dict and enumerate, print key followed by value

person = {"name": "Alice", "age": 30, "city": "New York"}
for index, key in enumerate(person):
    print(key, person[key])


# 3. Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
tuple_list = []
for index, item in enumerate(fruits):
    if index % 2 == 0:
        tuple_list.append((index, item))
print(tuple_list)



# -----------------Min and Max ---------------

# 1. Find the Maximum and Minimum Values in a List

numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print("Min value in list: ", min(numbers))
print("Max value in list: ", max(numbers))


# 2. Given a set of numbers, find the maximum and minimum values.

setn = {5, 10, 3, 15, 2, 20}
print("Min value in set: ", min(setn))
print("Max value in set: ", max(setn))


# 3. Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.

def min_and_max(words):
    return (min(words, key=len), max(words, key=len))
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
output_tuple = min_and_max(words)
print(output_tuple)




# ----------Exception Handling ---------------------

# 1. Write a Python program that attempts to divide two numbers a = 10  b = 0
#and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the #exception and print the error

a = 10
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print("A number can not be divided by zero")
    
    
# 2. Apply exception handling to below code and handle an exception if the index is out of range. 
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range!")
    
    
# 3. Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both values must be numbers.")
    finally:
        print("Execution completed")

safe_divide(1,0)
safe_divide(1,"a")



# ---------Decorator --------------
# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
import datetime

def add_time(function):
    def wrapper():
        start_time = datetime.datetime.now()
        function()
        end_time = datetime.datetime.now()
        time_taken = end_time - start_time
        print("Start Time: ", start_time)
        print("End Time: ", end_time)
        print("Total Time Taken: ", time_taken)
    return wrapper

@add_time
def append_numbers():
	nums = []
	for i in range(1, 1000 + 1):
	    nums.append(i)
	    
append_numbers()


# 2. Create a parameterised decorator retry that retries a function a specified number of times.

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == times:
                        print(f"All {times} retries failed.")
                        raise
        return wrapper
    return decorator

        

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")
    raise ValueError("Something went wrong!")
    
may_fail("Shailesh")



# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.

def check_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return func(x)
    return wrapper

@check_positive
def square_root(x):
    return x ** 0.5
    
print(square_root(-3))


# 4. Create a decorator cache that caches the result of a function based on its arguments.
def cache(func):
    memo = {}  
    def wrapper(*args, **kwargs):
        if args in memo:
            return memo[args]
        result = func(*args, **kwargs)
        memo[args] = result
        return result
    return wrapper
    

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x
	
print(expensive_computation(5))
print(expensive_computation(5))


# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.

def requires_permission(func):
    def wrapper(user, user_id):
        permissions = user.get('permissions')
        if 'admin' not in permissions:
            raise Exception("Permission Denied")
        func(user, user_id)
    return wrapper
    
@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test’']}

delete_user(user1, 101)
delete_user(user2, 101)
delete_user(user3, 101)


# -----------Generator------------

# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers Of 10  numbers 

def fibonaci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_generator = fibonaci()

for i in range(10):
    print(next(fib_generator))
    
    
# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.

def infinite_multiples(num):
    multiplier = 1
    while True:
        yield num * multiplier
        multiplier += 1

multiples_generator = infinite_multiples(3)

for i in range(20):
    print(next(multiples_generator))
    
    
# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
# word = “hello”
# times = 5

def repeat_word(word, times):
    for _ in range(times):
        yield word

for w in repeat_word("hello", 5):
    print(w)
    
    
    
# --------------- File Handling -------------

# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.

with open('Contacts.txt', 'r') as rf:
    for line in rf:
        print(line, end='')
        
        
# 2. Write a Python program to count the number of words in a file named words.txt

with open('Contacts.txt', 'r') as rf:
    f_content = rf.read()
    words = f_content.split()
    print("Total Number of words are: ", len(words))
    
    
# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.

with open('output.txt', 'w') as wf:
    wf.write("Hello, Python!")
    print("The file has been updated")
    
    
# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
import csv
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open('students.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in data:
        csv_writer.writerow(row)
        
        
# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def file_reader(file):
    with open(file, 'r') as rf:
        for line in rf:
            yield line
            
f_content = file_reader('Contacts.txt')

for line in f_content:
    print(line)
    
    
    
    
# ---------- Class -----------

# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
person_1 = Person('Shailesh', 27)
print("Name: ", person_1.name)
print("Age: ", person_1.age)


# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
    
    def deposit_amount(self, amount):
        self.balance = self.balance + amount
        print(f"Amount {amount} deposited successfully")
        
    def withdraw_amount(self, amount):
        if amount > self.balance:
            print("Insuffuient balance")
        else:
            self.balance = self.balance - amount
            print(f"Amount {amount} withdrawn successfully")
            
    def check_balance(self):
        print("Balance: ", self.balance)
        
account_1 = BankAccount('1234', 27000.50, 'Shailesh')
account_1.deposit_amount(50000)
account_1.check_balance()
account_1.withdraw_amount(20000)
account_1.check_balance()


# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
# book = Book.from_string("Python Programming, John Doe")

class Book:
    def __init__(self, book_string):
        self.book_name = book_string.split(',')[0]
        self.author = book_string.split(',')[1]
        
book_1 = Book("Python Programming, John Doe")
print("Book Name: ", book_1.book_name)
print("Author: ", book_1.author)


# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(this):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(this):
        print("Dog barks")
        
class Cat(Animal):
    def sound(this):
        print("Cat meoww")
        
dog = Dog() 
dog.sound()

cat = Cat()
cat.sound()


# 5. Write a code to perform multiple inheritance.
class Animal:
    def eat(self):
        print("Animal is eating")
        
class Pet:
    def sleep(self):
        print("Pet is sleeping")

class Dog(Animal, Pet):
    def sound(this):
        print("Dog barks") 
        
dog = Dog() 
dog.sound()
dog.eat()
dog.sleep()




# -----------datetime, sys, os----------------

from datetime import datetime, timedelta
import os

# 1. Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time

original_date = datetime(2020, 3, 22, 10, 0, 0)
new_date = original_date + timedelta(weeks=1, hours=12)
print("Original Date & Time:", original_date)
print("New Date & Time     :", new_date)


# 2. Code to get the dates of yesterday, today, and tomorrow.

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today    :", today)
print("Tomorrow :", tomorrow)


# 3. Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create folder "test" if it does not exist
folder_name = "test"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

# List all files and folders
for item in os.listdir():
    print(" -", item)

# Remove the test directory
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' removed.")


# 4. Write a Python program to rename a file from old_name.txt to new_name.txt.

old_name = "old_name.txt"
new_name = "new_name.txt"

with open(old_name, "w") as f:
    f.write("This is a sample file.")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}'")
else:
    print("File to rename does not exist.")


# 5. Create a file and Write a Python program to get the size of a file named example.txt 

file_name = "example.txt"
with open(file_name, "w") as f:
    f.write("Hello! This is a test file.")

file_size = os.path.getsize(file_name)
print(f"Size of '{file_name}': {file_size} bytes")


# 6. Convert the string "Feb 25 2020 4:20PM" into a Python datetime object 
# O/P: 2020-02-25 16:20:00

date_str = "Feb 25 2020 4:20PM"
converted_date = datetime.strptime(date_str, "%b %d %Y %I:%M%p")

print("Converted datetime:", converted_date)


# 7. Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18

given_date = datetime(2025, 2, 25)
new_date = given_date - timedelta(days=7)

print("New date:", new_date.date())   # 2025-02-18


# 8. Format the date 2020-02-25 as "Tuesday 25 February 2020"

date_to_format = datetime(2020, 2, 25)
formatted_date = date_to_format.strftime("%A %d %B %Y")

print("Formatted Date:", formatted_date)












		
