# fruits = ("apple", "banana", "cherry",)
# print(fruits[0])  # Output: apple
# print(fruits[1])  
# print(fruits[-1]) 

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5)
# combined_tuple = tuple1 + tuple2
# print(combined_tuple)  # Output: (1, 2, 3, 4, 5)

# repeated_tuple = ("hello",) * 3
# print(repeated_tuple)  # Output: ('hello', 'hello', 'hello')

# numbers = (1, 2, 2, 3, 2, 4)
# print(numbers.count(2)) # Output: 3

# print(fruits.index("banana")) # Output: 1

my_set = {1, 2, 3, "hello", 3.14, True}
another_set = {3, 4, 5}
empty_set = set()

print(len(my_set))  # Output: 5 (True is considered the same as 1)

my_set.add(5)
print(my_set)      # Output: {1, 2, 3, 'hello', 3.14, 5}
my_set.update([6, 7, 3])
print(my_set)      # Output: {1, 2, 3, 'hello', 3.14, 5, 6, 7}