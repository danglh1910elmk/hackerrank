# 1
customers = ['big','big','zo','zo','ac','ac','ac','opp','big','big','big','big','big','big','big','big','big','big','big','big','big']
cus = sorted(list(set(customers)))
n = len(customers)
result = [cus[i] for i in range(len(cus)) if customers.count(cus[i])/n >= 0.05]
result = [c for c in cus if customers.count(c)/n >= 0.05]


# 2
a = ['hello','world','1','2']
my_dict = {item : a[index+1] for index, item in enumerate(a) if index % 2 == 0}

# 3
l = ['a','b','b','c']
dict((x,l.count(x)) for x in set(l))

# 4
from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
Counter(z)
#Counter({'blue': 3, 'red': 2, 'yellow': 1})

# 5
list('aabccdd')
# >>>['a', 'a', 'b', 'c', 'c', 'd', 'd']