# 偏函数：
import functools

# 把某个参数固定住，产生新的函数
int2 = functools.partial(int, base=2)
int2('1000000')


