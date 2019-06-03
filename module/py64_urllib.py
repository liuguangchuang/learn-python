# -*- coding: utf-8 -*-
# Time: 2019/6/3 22:53
# Author: laugc
# Email: hahalgc@gmail.com
# File: py64_urllib.py

from urllib import request, parse

"""
urllib 提供了一系列用于操作 URL 的功能
"""

with request.urlopen('https://movie.douban.com/top250')as f:
    data = f.read()
    print('status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('data: ', data.decode('utf-8'))

print("====================")
# get 请求
req = request.Request('https://movie.douban.com/top250')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
               'Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req)as f:
    print('status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('data: ', f.read().decode('utf-8'))

print("====================")
# post 请求
print('Login to weibo.cn...')
email = input('Email: ')
password = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
               'Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# handler
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html')as f:
    pass
