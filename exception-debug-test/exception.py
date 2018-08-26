"""
    Python异常处理语法：

    try:
        <code>
    except Exception as exceptionName:
        <code>
    except Exception2 as exceptionName2:
        <code>
    finally:
        <code>

    类似于try-cache语法

    异常及异常继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

import logging

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)

    """ 打印日志 """
    logging.exception(e)
finally:
    print('finally...')

print('END')

""" 自定义异常并抛出异常 """


# err_raise.py
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
