# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero

x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
z = int(input("enter the value of z:"))

if x == y or y == z or x==z:
     print("sum = 0")
else:
    print("sum = x + y + z = ",x+y+z)

