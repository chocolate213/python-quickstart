# 定义对象

## 定义一个对象，括号中的object代表继承了哪个对象
class Student(object):
    pass

s1 = Student()

print(s1)

print(Student)

# 通过函数绑定属性
class Teacher(object):
    # 相当于构造函数，第一个参数为对象本身，可以将属性绑定到对象本身上
    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id

    # 简单实现toString函数
    def to_string(self):
        print('%s is %d years old.' % (self.name, self.age))

t1 = Teacher(1, "zhangSan", 23)

print("name: ", t1.name)
print("age: ", t1.age)
print("id: ", t1.id)

t1.to_string()
