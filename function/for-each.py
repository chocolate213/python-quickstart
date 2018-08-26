# 迭代map

m = {'k1':'v1', 'k2':'v2', 'k3':'v3'}

print("for each key: ")
for key in m:
    print(key)

print("for each value: ")
for value in m.values():
    print(value)

print("for each items: ")
for item in m.items():
    print(item)

# 判断是否可以迭代
from collections import Iterable

# 字符串可以迭代
x = isinstance('abc', Iterable)

x = isinstance([1,2,3], Iterable)

print(x)

# 迭代两个参数
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 迭代带角标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

    