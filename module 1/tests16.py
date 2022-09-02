# Write a Python program to find the first appearance of the substring 'not'
# and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
# 'not'...'poor'substring with 'good'. Return the resultng string.

str1 = str(input("enter your string : "))
n = str1.find('not')
p = str1.find('poor')

print(n)
print(p)
  
if p > n and n>0 and p>0:
    str1 = str1.replace(str1[n:(p+4)], 'good')
    print(str1)
else:
    print(str1)