# 函数参数

# 函数默认参数：默认参数必须指向一个不变的对象

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
print(power(2, 3))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
add_end()
add_end()
result = add_end()

print(result)

# 函数可变参数：可变参数传入的是一个tuple

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

x = calc(1, 2, 3)

print("x: ", x)

def calc2(a, *numbers):
    print(a)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def test(a, b, *l):
    print(a, b, l)

test(1, 2, 123)

# 可变参数必须在最后 
#def test2(a*, b, c)

# 关键词参数（最后一个参数为map，且为可变长度，可以不传）
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)

person('Adam', 45, gender='M', job='Engineer')

# 检查传入了什么类型的关键词参数

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 命名关键词参数：指定关键词参数需要哪个

def person(name, age, *, city, job):
    print(name, age, city, job)

# 参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。