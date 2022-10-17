# Write a Python func�on that takes two lists and returns true if they have at least one common member.

def data(list1, list2):
     result = False
     for i in list1:
         for j in list2:
             if i == j:
                 result = True
                 return result
print(data([1,2,3,4,5], [4,5,6,7,8,9]))
print(data([1,2,3,4,5], [6,7,8,9]))


