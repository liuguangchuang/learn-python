# -*- coding: utf-8 -*-
# Time: 2019/5/22 23:16
# Author: laugc
# Email: hahalgc@gmail.com
# File: py47_multi_processing.py

"""
子进程
"""

import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www,python.org'])
# print('exit code: ', r)

# =============================
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('exit code: ', p.returncode)
