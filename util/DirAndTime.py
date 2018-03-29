# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

'''---**--- DirAndTime.py 用于获取当前日期及时间，以及创建异常截图存放目录  ---**--- '''

import os
import time
from datetime import datetime
from config.VarConfig import screenPicturesDir

'# --* 获取当前的日期 *-- # '
def getCurrenDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" + str(timeTup.tm_mon) + \
                  "-" + str(timeTup.tm_mday)
    return currentDate

'# --* 获取当前时间 *-- # '
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H- %M- %S- %f')
    return nowTime

'# --* 创建截图存放的目录 *-- # '
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir, getCurrenDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        return dirName

if __name__ == '__main__':
    print(getCurrenDate())
    print(createCurrentDateDir())
    print(getCurrentTime())