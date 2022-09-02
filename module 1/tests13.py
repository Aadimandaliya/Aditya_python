# Write a Python program to count the occurrences of each word in a given
# sentence

str1 = 'i am aditya mandaliya i am doing python. .'

cn = dict()
wrd = str1.split()
print(wrd)

for i in wrd:
    if i in cn:
        cn[i]+=1
    else:
        cn[i]=1
print(cn)