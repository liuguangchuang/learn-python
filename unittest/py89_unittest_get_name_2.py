# -*- coding: utf-8 -*-
# Time: 2019/6/16 22:36
# Author: laugc
# Email: hahalgc@gmail.com
# File: py89_unittest_get_name_2.py

from py88_unittest_formatted_name_1 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
