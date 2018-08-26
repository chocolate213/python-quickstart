# __slots__: 给对象绑定固定的实例

class User(object):
    __slots__ = ('name', 'age')  # 用tuple来定义属性名称

    def to_string(self):
        print('name: %s, age: %s' % (self.name, self.age))

u = User()

u.name='zhangSan'
u.age=23

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

class Screen(object):

    @property
    def width(self):
        return self._width

    @property.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._width


