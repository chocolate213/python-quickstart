# __slots__: 给对象绑定固定的实例
class User(object):
    __slots__ = ('name', 'age')  # 用tuple来定义属性名称

    def to_string(self):
        print('name: %s, age: %s' % (self.name, self.age))


u = User()

u.name = 'zhangSan'
u.age = 23

# 将会报错
# u.gender='male'

u.to_string()


# 使用@property把一个getter方法变为属性
class Student(object):

    # 相当于getter方法
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def to_string(self):
        print("score: ", self._score)


s = Student()

s.score = 100

s.to_string()


# getter and setter
class Screen(object):

    def __init__(self, height, width):
        self._resolution = None
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        pass

    @property
    def height(self):
        return self._width

    @height.setter
    def height(self, height):
        pass

    @property
    def resolution(self):
        return self._resolution

    def to_string(self):
        print('width: %s height: %s, resolution: %s' % (self._height, self._width, self._resolution))


a = Screen(100, 200)

a.height = 100
a.width = 200

a.to_string()

""" python支持多重继承 """


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


def run():
    print('Running...')


class Runnable(object):
    pass


def fly():
    print('Flying...')


class Flyable(object):
    pass


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


d = Dog()
run()

b = Bat()
fly()