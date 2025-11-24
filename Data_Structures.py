# 1. Find and print the maximum and minimum values from the list
nums = [1, 2, 3, 4, 5]
max_value = max(nums)
min_value = min(nums)
print(f"Max value: {max_value}, Min value: {min_value}\n")

# 2. Merge two lists and print the result
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
merged_list = a + b
print(f"Merged list: {merged_list}\n")

# 3. Print the number of times the value 3 appears in the list
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
count_of_3 = a.count(3)
print(f"Number of times 3 appears: {count_of_3}\n")

# 4. Sort the list and print the result
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print(f"Sorted list: {a}\n")

# 5. Add the element 6 to the set and print the updated set
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(f"Updated set after adding 6: {numbers}\n")

# 6. Remove the element 3 from the set and print the updated set
numbers.remove(3)  # This will raise a KeyError if 3 is not found, but we're assuming 3 is in the set.
print(f"Updated set after removing 3: {numbers}\n")

# 7. Find and print the intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print(f"Intersection of sets: {intersection}\n")

# 8. Count and print the number of occurrences of 'apple' in the tuple
fruits = ('apple', 'banana', 'apple', 'cherry')
apple_count = fruits.count('apple')
print(f"Number of occurrences of 'apple': {apple_count}\n")

# 9. Concatenate two tuples and print the result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}\n")

# 10. Access and print the value associated with the key "age" from the dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
age_value = person["age"]
print(f"Age: {age_value}\n")

# 11. Add a new key "gender" to the dictionary and print the updated dictionary
person["gender"] = "M"
print(f"Updated dictionary with gender: {person}\n")

# 12. Remove the key "city" from the dictionary and print the updated dictionary
person.pop("city")
print(f"Updated dictionary after removing 'city': {person}\n")

# 13. Merge two dictionaries and print the result
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")

