# finding frequency of each element in a list

from collections import Counter

my_list = ['a','a','b','b','c','d','d','d','d','d']

count = Counter(my_list)

print(count)
# Counter({
    'd':5,
    'b':3,
    'a':2,
    'c': 1})
    
print(count['b'])
# 3

pirnt(count.most_common(1))
[('d', 5)]

