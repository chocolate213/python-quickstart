# list

users = ['zhangSan', 'liSi', 'wangWu']


l = len(users)

print("users length: ", l)

user1 = users[0]
user2 = users[1]
user3 = users[2]

print('users: ', users)

print('user1: ', user1)
print('user2: ', user2)
print('user3: ', user3)


# list可以倒着获取，但是如果越界也会抛出IndexError: list index out of range
print('last user: ', users[-1])

# list中添加元素：append
users.append("user4")

print("current user list: ", users)

# 将元素插入到list的指定位置(其他元素顺延)
users.insert(0, "zhangSanSan")

print("current user list: ", users)

# pop() 删除元素末尾的一个元素

users.pop()

print("current user list: ", users)

# 移除指定位置的元素, 将会返回被移除的元素
p = users.pop(0)

print("removed element: ", p)

# list里面的元素可以不同

# list可以嵌套数组（多维数组）

# 空的list

emptyList = [1, 2, 3]

print("empty list: ", emptyList)