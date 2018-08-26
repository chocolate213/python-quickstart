
# 定义函数

# def functionName(param1, param2)
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

x = my_abs(-1000)

print("x: ", x)

def sum(x, y):
    return y + x;

s = sum(1, 2)

print("s: ", s)

# pass为占位符，可以定义一个空函数，空函数返回值为None
def abc():
    pass

x = abc()
print(x)

# 返回多个结果: 返回的结果是一个tuple(不可变数组)

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print("x: ", x, " y:", y)

z = move(100, 100, 60, math.pi / 6)

print("z: ", z) 