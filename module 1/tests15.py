# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add 'ly'
# insteadif the string length of the given string is less than 3, leave it
# unchanged.

str1 = str(input("enter your string: "))
length = len(str1)

if length >2:  #true
    if str1[-3:] == 'ing':  #true
      str1 += 'ly'
    else:                #false
      str1 += 'ing'

print(str1)      