# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

'''---**---  ClipboardUtil.py 用于实现剪贴板功能  ---**---'''

import win32clipboard as w
import win32con

class Clipboard(object):
    '''
    模拟 Windows 设置剪贴板
    '''

    @staticmethod
    def getText():
        '''
        读取剪贴板
        '''
        w.OpenClipboard()    # 打开剪贴板
        d = w.GetClipboardData(win32con.CF_TEXT)     # 获取剪贴板中的数据
        w.CloseClipboard()    # 关闭剪贴板
        return d    # 返回剪贴板数据给调用者

    @staticmethod
    def setText(aString):
        '''
        设置剪贴板内容
        '''
        w.OpenClipboard()    # 打开剪贴板
        w.EmptyClipboard()    #清空剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)    # 将数据aString写入剪贴板
        w.CloseClipboard()    # 关闭剪贴板



