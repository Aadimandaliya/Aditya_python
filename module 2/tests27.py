# Write a Python script to concatenate following dic�onaries to create a 
# new one.

dic1={1:'mohit', 2:'rohit'}
dic2={3:'virat', 4:'yamini'}
dic3={5:'yesh',6:'rahul'}

dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

