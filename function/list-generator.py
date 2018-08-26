# range创建list

list =  [x * x for x in range(1, 11)]

print(list)

# 可以在后面跟上判断条件

list = [x * x for x in range(1, 11) if x % 2 == 0]

print(list)

# 全排列（嵌套for）
list = [m + n for m in 'ABC' for n in 'XYZ']

print(list)


import os # 导入os模块，模块的概念后面讲到

# . 为当前文件夹
fileList = [d for d in os.listdir('.')]

print(fileList)

fileList = [d for d in os.listdir("C:/")]

print(fileList)


# 遍历map
d = {'x': 'A', 'y': 'B', 'z': 'C' }

mapList = [k + '=' + v for k, v in d.items()]

print(mapList)

# 可迭代列表：list、tuple、dict、set、str ：Iterable



