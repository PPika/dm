# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 15:48
# @Author  : Pikka
# @File    : mouse.py
# @Software: PyCharm
# @Doc     : 鼠标操作


from win32com.client import Dispatch
import os
import time
import win32gui

# 注册大漠插件
dm = Dispatch("dm.dmsoft")
dm.SetPath(os.getcwd())

"""
long EnableMouseAccuracy(enable)        是否打开指针精确度开关，默认是关闭



"""
