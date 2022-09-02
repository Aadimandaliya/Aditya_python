# Write a Python function to reverses a string if its length is a multiple of 4.

s1 = str(input("enter your string : "))

if len(s1) %4 == 0 :
    print(''.join(reversed(s1)))
else:
    print(s1)