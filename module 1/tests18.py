# Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. Ifthe string length islessthan 2,return instead
# of the empty string.
# o Sample String:w3resource'
# o Expected Result: 'w3ce'
# o Sample String: 'w3'
# o Expected Result: 'w3w3'
# o Sample String: ' w'
# o Expected Result: Empty String


s1 = str(input("enter your stirng : "))

if len(s1)<2:
    print(" ")
else:
    print(s1[:2] + s1[-2:])