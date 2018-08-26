
def dubble(x):
    return 2 * x

# 第一个参数为对Iterable每个元素的操作
l = list(map(dubble, [1, 2, 3, 4, 5]))

print(list(l))

def add(x, y):
    return x + y

a = list(range(0, 101))

print(a)


# reduce 需要首先引用
from functools import reduce

# 反复迭代
l = reduce(add, a)

print(l)

# filter函数：过滤掉不需要的东西

# sorted函数：排序

s = sorted([36, 5, -12, 9, -21])

print(s)