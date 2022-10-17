# Write a Python program to remove duplicates from a list.

a = [1,3,5,7,3,5,6,1,5,6,9]


unique = []
for i in a:
    if i not in unique:
        unique.append(i)
        
print(unique)
