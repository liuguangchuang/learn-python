# -*- coding: utf-8 -*-
# author: laugc
# email: hahalgc@gmail.com
# time: 2019/7/27 23:09
# file: py96_python_repos.py

import requests
import pygal
import sys
import importlib
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

importlib.reload(sys)

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)

# 将 api 响应存储到一个变量中
response_dict = r.json()
# print(response_dict.keys())
print('Total repositories:', response_dict['total_count'])

# 仓库有关信息
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names = []
plt_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plt_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        # 添加连接
        'xlink': repo_dict['html_url']
    }
    plt_dicts.append(plt_dict)
# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()  # 用于定制图表的外观
my_config.x_label_rotation = 45  # 标签绕 x 轴旋转 45 度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 设置图表标题的字体大小
my_config.label_font_size = 14  # 设置图副标签的字体大小
my_config.major_label_font_size = 18  # 设置主标签的字体大小
my_config.truncate_label = 15  # 仅显示 15 个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000  # 设置自定义宽度

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python projects on Github'
chart.x_labels = names
chart.add('', plt_dicts)
chart.render_to_file('Python_repos.svg')

# 第一个仓库
# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print('Selected information about first repository......')
# for repo_dict in repo_dicts:
#     print()
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
