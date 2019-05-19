# -*- coding: utf-8 -*-
# Time: 2019/5/19 16:48
# Author: laugc
# Email: hahalgc@gmail.com
# File: py38_unit_test.py

"""
单元测试
"""

import unittest


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
