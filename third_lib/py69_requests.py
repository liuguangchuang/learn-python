# -*- coding: utf-8 -*-
# Time: 2019/6/7 17:02
# Author: laugc
# Email: hahalgc@gmail.com
# File: py69_requests.py

import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)

r1 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r1.url)
print(r1.encoding)
# content 属性获得 bytes 对象
print(r1.content)

# requests 默认使用 application/x-www-form-urlencoded 对 POST 数据编码
# 如果要传递 json 数据，可以直接传入 json 参数
# 处理 json
# r2 = requests.get(
#     'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330'
#     '&format=json')
# print(r2.json())

# dict 作为 headers 参数
r3 = requests.get('https://www.douban.com/',
                  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r3.text)
# 获取响应头
print(r3.headers)
print(r3.headers['Content-Type'])
# 获取 cookie
print(r3.cookies)

# post 请求
r4 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com',
                                                              'form_password': '123456'})
# 2.5 秒后超时
r5 = requests.get('https://www.douban.com/', timeout=2.5)
