# Write a Python program to combine two dic�onary adding values for
# common keys.
# o d1 = {'a': 100, 'b': 200, 'c':300}
# o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300, 'e':100}
d2 = {'a': 300, 'b': 200, 'd':400, 'e':600}

d = Counter(d1) + Counter(d2)
print(d)
