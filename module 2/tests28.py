# Write a Python script to check if a given key already exists in a dic�onary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def key_present(p):
  if p in dic:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key_present(5)
key_present(9)
