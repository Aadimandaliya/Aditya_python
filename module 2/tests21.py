# Write a Python program to replace last value of tuples in a list.

t1 = [(10,20,30),(70,40,50),(20,40,60)]

for t in t1:
    print(t[:-1] + (100,) ,end='')