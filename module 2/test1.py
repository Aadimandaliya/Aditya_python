#Write a Python function to get the largest number,smallest num and sum of all from a list.

list1 = [1,5,7,9,4,2]

list1.sort()

print("largest element in the list is : ", list1[-1])

print("smallest element in the list is : ", list1[0])

sum = sum(list1)

print("sum of all in the list : ",sum)