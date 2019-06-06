# -*- coding: utf-8 -*-
# Time: 2019/6/6 22:03
# Author: laugc
# Email: hahalgc@gmail.com
# File: py67_pillow_1.py

from PIL import Image, ImageFilter

# 打开一个 jpg 图片，当前路径
im = Image.open('cat.jpg')
# 获得图片尺寸
w, h = im.size
print('original image size: %s %s' % (w, h))
# 缩放 50%
im.thumbnail((w // 2, h // 2))
print('resize image to: %s %s' % (w // 2, h // 2))
# 保存
im.save('thumbnail.jpg', 'jpeg')
# 模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
