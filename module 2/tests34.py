# # Write a Python program to print all unique values in a dic�onary.\

lis = [{"abc":"movies"}, {"abc": "sports"}, {"abc": "music"}, {"xyz": "music"},
 {"pqr":"music"}, {"pqr":"movies"},{"pqr":"sports"}, {"pqr":"news"}, {"pqr":"sports"}]

s = set()
for dic in lis:
   for val in dic.values():
      s.add(val)

print(s)