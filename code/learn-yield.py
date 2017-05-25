# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/5/21 下午11:29
    @file:     learn-yield.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 版本1
def fab_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print '---', b
        a, b = b, a + b
        n = n + 1

print  fab_1(5)

# 结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，
# 其他函数无法获得该函数生成的数列。
# 要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：
def fab_2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

print fab_2(5)

# 改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，
# 该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
# Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

print type(Fab(5))
print [i for i in Fab(5)]

# 然而，使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。如果我们想要保持第一版 fab 函数的简洁性，
# 同时又要获得 iterable 的效果，yield 就派上用场了：
# 第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果。
def fab_4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print '----', b
        # print b
        if b > 2:
            break
        a, b = b, a + b
        n = n + 1

print [i for i in fab_4(5)]

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
# 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，
# fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。

# 也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），
# 这样我们就可以更清楚地看到 fab 的执行流程：
