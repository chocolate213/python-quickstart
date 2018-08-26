print(type(123))        # int
print(type("123"))      # str
print(type([1, 2, 3]))  # list
print(type(True))       # bool
print(type(None))       # NoneType

a = (1, 2, 3)
print(type(a))          # tuple

b = {1:1, 2:2}          #dict
print(type(b))


import types

c = type(abs)==types.FunctionType

print(c)

# 判断是否是某种类型
isinstance('a', str)

# dir()获取一个对象的所有属性和方法

class Animal(object):

    def __init__(self, name):
        self.__name = name

    def eat(self):
        print('animal is eating...')

    def run(self):
        print('animal is run')

    def print_name(self):
        print("name: ", self.__name)

print(dir(Animal))
print(dir(Animal.__class__.__bases__))
print(Animal.__hash__)

# 类变量与实例变量：实例变量各个实例均可访问
class Student(object):
    name = 'zhangSan'

s = Student()

print(s.name)
print(Student.name)