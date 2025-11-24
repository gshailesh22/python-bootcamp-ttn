# Task 1: Convert the following values to the specified types and print the results

# 1. Convert 3.75 to an integer
value1 = 3.75
converted_int = int(value1)
print(f"Converted 3.75 to integer: {converted_int}")

# 2. Convert "123" to a float
value2 = "123"
converted_float = float(value2)
print(f"Converted '123' to float: {converted_float}")

# 3. Convert 0 to a boolean
value3 = 0
converted_boolean = bool(value3)
print(f"Converted 0 to boolean: {converted_boolean}")

# 4. Convert False to a string
value4 = False
converted_string = str(value4)
print(f"Converted False to string: '{converted_string}'")


# Task 2: Convert all characters in the string to uppercase
x = "hello"
uppercase_x = x.upper()
print(f"Original string: '{x}', converted to uppercase: '{uppercase_x}'")


# Task 3: Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. Then convert it to an integer.
x = 5
y = 3.14
z = x + y
print(f"z = x + y = {x} + {y} = {z}")
print(f"Data type of z: {type(z)}")
z_int = int(z)
print(f"Converted z to integer: {z_int}")


# Task 4: Given the string s = 'hello', perform the following operations:

s = 'hello'

# 1. Convert the string to uppercase
s_upper = s.upper()
print(f"Uppercase of 'hello': {s_upper}")

# 2. Replace 'e' with 'a'
s_replace = s.replace('e', 'a')
print(f"Replaced 'e' with 'a' in 'hello': {s_replace}")

# 3. Check if the string starts with 'he'
starts_with_he = s.startswith('he')
print(f"Does 'hello' start with 'he'? {starts_with_he}")

# 4. Check if the string ends with 'lo'
ends_with_lo = s.endswith('lo')
print(f"Does 'hello' end with 'lo'? {ends_with_lo}")

