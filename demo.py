# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 8:28
# @Author  : Pikka
# @File    : demo.py
# @Software: PyCharm
# @Doc     : 

from win32com.client import Dispatch
import time
import win32gui

# 注册大漠插件
dm = Dispatch("dm.dmsoft")
dm.SetPath(r"C:\Users\haeer\Desktop\dm")

# 找到chrome页面的句柄
hwnd = (dm.EnumWindow(0, "连连看", "chrome", 1 + 4 + 8 + 16))
print(dm.GetWindowTitle(hwnd))
#
# # 把窗口置顶
# print(dm.SetWindowTransparent(hwnd, 255))
#
# # 绑定窗口
# # dm.BindWindow(hwnd, "normal", "normal", "normal", 0)
#
# print("开始获取坐标位置：")
# # 获取当前鼠标点击的坐标
#
# print("点击左上角位置：")
# dm.WaitKey(1, 0)
# left = dm.GetCursorPos()[1:]
# print(left)
#
# time.sleep(1)
#
# print("点击右下角位置：")
# dm.WaitKey(1, 0)
# right = dm.GetCursorPos()[1:]
# print(right)
#
#
# # 获取图片并且分割
# # print(dm.Capture(431, 173, 1481, 940, "demo.bmp"))
# def splitScreen(col=12, row=8):
#     dm.Capture(left[0], left[1], right[0], right[1], "demo.bmp")
#     for x in range(col):
#         for y in range(row):
#             pass
#
#
# print("ceshi")
# # 这里测试一下获取坐标内的一种颜色
while True:
    dm.WaitKey(2, 0)
    x, y = dm.GetCursorPos()[1:]
    print(x, y)
    time.sleep(2)
    print(dm.GetColorBGR(x, y))
    print(dm.GetColor(x, y))