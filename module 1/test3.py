#swap variable without or with temp variable

x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

#x, y = y, x   #without temp variable

temp = x      #with temp variable
x=y
y=temp
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

