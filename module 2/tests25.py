# Write a Python program to convert a list of tuples into a dic�onary.


list1 = [("camera", 'canon'), ("camera", 'nikon'), ("camera", 'sony'), ("camera man", 'aditya'), ("camera man", 'nandan'), ("city", 'dhoraji')]
dict = {}
for x , y in list1:
    dict.setdefault(x, []).append(y)
print (dict)
