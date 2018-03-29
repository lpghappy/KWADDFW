# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback

# 设置此次测试的环境编码为utf-8
# import sys
# reload(sys)

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)