# -*- coding: utf-8 -*-
# Time: 2019/6/6 22:13
# Author: laugc
# Email: hahalgc@gmail.com
# File: py68_pillow_2.py

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 * 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建 Font 对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建 Draw 对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
