
# 函数可以作为参数返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 此时返回的是一个函数：
fun = lazy_sum(1, 2, 3);

# 执行函数，拿到结果
x = fun()

# 打印结果
print(x)