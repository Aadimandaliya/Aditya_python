# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

s1 = str(input("enter your string s1 : "))
s2 = str(input("enter your string s2 : "))

print(s1 +' '+ s2)

str1 = s2[:2] + s1[2:]
str2 = s1[:2] + s2[2:] 

print(str1  + ' ' + str2)