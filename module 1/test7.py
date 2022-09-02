#Write a Python program that will return true ifthe two given integervalues
#are equal or their sum or difference is 5

x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))

if x == y or (x-y) == 5 or (x+y) == 5:
    print("True")
else:
    print("false")
