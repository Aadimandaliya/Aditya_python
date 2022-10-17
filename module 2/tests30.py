# Write a Python program to check mul�ple keys exists in a dic�onary
student = {'id':101,'name': 'Aadi','class': 12,'school': 'dream','city':'dhoraji'}


print(student.keys() >= {'class', 'name','city'})
print(student.keys() >= {'name', 'branch'})
print(student.keys() >= {'stream', 'name'})
