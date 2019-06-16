# -*- coding: utf-8 -*-
# Time: 2019/6/16 22:30
# Author: laugc
# Email: hahalgc@gmail.com
# File: py90_unittest_3.py

import unittest

from py88_unittest_formatted_name_1 import get_formatted_name

"""
单元测试
"""


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
