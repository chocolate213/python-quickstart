# set 同java set

# 初始化
s = {1, 2, 3, 4, 4}

print('current set: ', s)

# 初始化一个空set

s = {1, 1}

print('current set: ', s)

# set add: 添加重复元素不报错，但是集合不变

s.add(2)

print('current set: ', s)

# 移除元素：按照元素移除，不能按照角标移除
s.remove(1)

print('current set: ', s)

# set 交集并集计算

s1 = {1, 2, 3}
s2 = {4, 2, 3}

a = s1 & s2
print(a)

a = s1 | s2
print(a)

