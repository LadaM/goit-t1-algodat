my_dict = {"name": "John", "age": 25}
print(my_dict)  # Output: {'name': 'John', 'age': 25}

# accessing value by key
print(my_dict["name"])  # Output: John

# assignment
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'John', 'age': 26}

# adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# deleting key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 26}
