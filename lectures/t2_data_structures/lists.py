my_list = [1, 2, 3, 4, 5]
print(my_list) # Output: [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list) # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0) # Insert number 0 at position 0
print(my_list) # Output: [0, 1, 2, 3, 4, 5]

unsorted_list = [3, 1, 4, 1, 5, 9, 2]
unsorted_list.sort()
print(unsorted_list) # Output: [1, 1, 2, 3, 4, 5, 9]