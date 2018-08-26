#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 前两行固定，第一行可以让python脚本直接在linux中执行，第二行声明该文档格式为utf-8

# 声明模块名
' a test module '

# 声明作者
__author__ = 'Michael Liao'

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
import sys

# sys.argv 变量指向了所有传递给该模块的参数，第一个参数默认指向模块名（可执行文件全路径）

def test():
    # 第一个参数默认指向模块名
    print("model name: ", sys.argv[0])
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，所以在这个文件中可以执行测试，但是如果其他文件引用了这个文件，就无法执行测试
if __name__=='__main__':
    test()



# 在python中，_或者__开头的变量、函数为private，不是不能引用，而是不建议引用

# 安装第三方模块

