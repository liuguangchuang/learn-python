# -*- coding: utf-8 -*-
# @Time : 2019/5/9 23:02
# @Author : laugc
# @Email : hahalgc@gmail.com
# @File : py6_for_while.py


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break 退出循环
n = 1
while n <= 100:
    if n > 10:  # 当 n = 11 时，条件满足，执行 break 语句
        break  # break 语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 退出此次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果 n 是偶数，执行 continue 语句
        continue  # continue 语句会直接继续下一轮循环，后续的 print() 语句不会执行
    print(n)
