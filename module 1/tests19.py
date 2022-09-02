# Write a Python function that takes a list of words and returns the length of the longest one.

list = ['php','android','python','python','c','c++']

ls=[]

for i in list:
    ls.append((len(i),i))
ls.sort()
print(ls)


print("length of the longest word is : " , ls[-1][0])

print("longest word is : " , ls[-1][1])
 

