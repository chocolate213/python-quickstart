
# for x in list: 
# for语句之后必须缩进

names = ['zhangSan', 'liSi', 'wangWu']

for name in names:
    print(name)

# range: 生成一个序列

r = range(3)

print(r)

# 将range转化为list
r = list(r)

print(r)

a = range(101)

a = list(a)

sum = 0
for n in a: 
    sum = sum + n

print(sum)

# while 注意冒号 break continue

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')