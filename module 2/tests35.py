# Write a Python program to create and display all combina�ons of le�ers,
# selec�ng each le�er from a different key in a dic�onary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']}
# o Expected Output:
# o ac ad bc bd

my_dict= {'1':['a', 'b'], '2':['c', 'd']}
my_list= list(my_dict.values())

for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)