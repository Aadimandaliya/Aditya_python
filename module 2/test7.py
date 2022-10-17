# Write a Python func�on that takes a list and returns a new list with unique
# elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,4,3,2,1,5,6,7,8,3]))





