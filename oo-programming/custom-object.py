"""
  __str__ ：用户看到的字符串

  __repr__：开发者看到的字符串

  __iter__: 迭代器

  __next__：迭代器的next方法

  __getitem__： 按照角标取得元素

  __getattr__： 对于一个不存在的属性，返回指定值

  __call__: 调用实例本身
"""


class Student(object):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student{name = %s}' % self._name

    """ str是用户看到的字符串，repr是需要开发者看到的字符串 """
    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


s = Student("zhangSan")
print(s)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)

print()
print()
print()
print()


class Url(object):

    def __init__(self, path='http:/'):
        self._path = path

    def __getattr__(self, path):
        print("path in getstr: " + path)
        print("self._path in getstr: " + path)
        return Url('%s/%s' % (self._path, path))

    def __call__(self, path=''):
        print("path in call: " + path)
        print("self._path in call: " + path)
        return Url('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


u = Url("http://")("localhost:8080")("api")

print(u)

