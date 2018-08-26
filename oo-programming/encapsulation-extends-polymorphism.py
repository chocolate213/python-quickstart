# 封装、继承、多态


# 面向对象：封装

# 实例变量使用双下划线开头就无法直接访问（也可以访问，使用_User__username访问），必须使用set、get方法访问
class User(object):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def to_string(self):
        print('username: %s, password: %s' % (self.__username, self.__password))

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

u = User('zhangSan', 123)

u.to_string()

u.set_password('456')

u.to_string()

password = u.get_password()

print(password)

# 面向对象：继承，可以继承父类中的方法

class Animal(object):

    def __init__(self, name):
        self.__name = name

    def eat(self):
        print('animal is eating...')

    def run(self):
        print('animal is run')

    def print_name(self):
        print("name: ", self.__name)

class Dog(Animal):

    def __init__(self, name):
        self.__name = name

    def run(self):
        print('dog is run')

    def print_name(self):
        print("name: ", self.__name)

class Cat(Animal):

    def __init__(self, name):
        self.__name = name

    def run(self):
        print('cat is run')

    def print_name(self):
        print("name: ", self.__name)

cat1 = Cat("zhangSan")

cat1.eat()
cat1.print_name()

# 面向对象：多态

def animal_run(animal):
    animal.run()

animal_run(cat1)

# Cat 即是Animal也是Cat
is_animal = isinstance(cat1, Animal)
is_cat = isinstance(cat1, Cat)

print(is_animal)
print(is_cat)