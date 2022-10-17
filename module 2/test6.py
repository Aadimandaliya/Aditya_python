# Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.


value = list()
for i in range(1,30+1):
    value.append(i*i)

print(value[:5])
print(value[-5:])


