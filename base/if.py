# -*- coding: utf-8 -*-

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

age = 20

if age > 10:
    print('age > 10')
elif age > 5:
    print('age > 10')
else:
    print('age < 5')


# if判断条件还可以简写，比如写：

# if x:
#     print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

# if语句可以不缩进

a = []

if a:
    print('a is not null')
else:
    print('a is null')

# int()函数可以把非字符串转换为字符串

b = '1000'

b = int(b)

c = 1000

print(b + c)

d = 'abc'

# 非字符串无法转换
# d = int(d)

