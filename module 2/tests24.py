# Write a Python program to unzip a list of tuples into individual lists.

data = [('1','aayush','std-9'),('2','yashvi','std-10'),('3','parth','std-11')]

print(list(zip(*data)))
