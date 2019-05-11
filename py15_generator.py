# -*- coding: utf-8 -*-
# @Time : 2019/5/11 15:31
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py15_generator.py
"""
生成器
"""

# 把一个列表生成式的 [] 改成 ()，就创建了一个 generator
g = (x * x for x in range(10))
for n in g:
    print(n)


# 斐波拉契数列
# 如果一个函数定义中包含 yield 关键字，该函数是一个 generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)

# 遍历 generate
for n in fib(6):
    print(n)

# 用 for 循环调用 generator 时，拿不到 generator 的 return 语句的返回值。
# 如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中
while True:
    try:
        x = next(f)
        print('f: ', x)
    except StopIteration as e:
        print('generate return value: ', e.value)
        break
