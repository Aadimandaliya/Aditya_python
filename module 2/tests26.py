# Write a Python script to sort (ascending and descending) a dic�onary by
# value.

my_dict = {2: 1, 1:2 , 0:0 , 4:3}
print("my dictionary is : ",my_dict)

sorted_dict = sorted(my_dict.items(),key = lambda a:a[1])  # for ascending order
print("Sorted dictionary in ascending order : ", sorted_dict)

sorted_dict1 = sorted(my_dict.items(),key = lambda a:a[1],reverse = True) # for descending order
print("Sorted dictionary in descending order : ", sorted_dict1)
