# Write a Python program to create a dic�onary from a string.

str = input("Enter a string: ")
dic = {}

for i in str:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)

