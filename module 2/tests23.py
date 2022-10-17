# Write a Python program to remove an empty tuple(s) from a list of tuples.

list = [(), (), ('canon',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list = [t for t in list if t]
print(list)

