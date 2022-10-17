# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

list = ['test','vivo','1211','oppo']

li = 0


for word in list:
    if len(word)>1 and word[0]==word[-1]:
        li += 1

print('number of string in the list with same staring and ending: ',li)