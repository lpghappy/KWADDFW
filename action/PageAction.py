# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

'''---**--- TestSendMailWithAttachment.py 用于实现具体测试逻辑  ---**---'''

from selenium import webdriver
from config.VarConfig import ieDriverFilePath
from config.VarConfig import chromeDriverFilePath
from config.VarConfig import firefoxDriverFilePath
from util.ObjectMap import getElement
from util.ClipboardUtil import Clipboard
from util.KeyBoardUtil import KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import WaitUtil
from selenium.webdriver.chrome.options import Options
import time

'# --* 定义全局变量 *-- # '
driver = None
'# --* 全局的等待类实例对象 *-- # '
waitUtil = None

'# --* 打开浏览器 *-- # '
def open_browser(browserName, *arg):
    global driver, waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            chrome_options = Options()    # 创建Chrome 浏览器的一个Option实例对象
            chrome_options.add_experimental_option("excludeSwitches",
                    ["ignore - certificate - errors"])    # 添加屏蔽-- "ignore - certificate - errors 提示信息的设置参数
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath,
                                      chrome_options=chrome_options)
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

'# --* 访问某个网站 *-- # '
def visit_url(url, *arg):
    global driver
    try:
        print(driver)
        driver.get(url)
    except Exception as e:
        raise e

'# --* 关闭浏览器 *-- # '
def close_browser(*arg):
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

'# --* 强制等待 *-- # '
def sleep(sleepSections, *arg):
    try:
        time.sleep(int(sleepSections))
    except Exception as e:
        raise e

'# --* 清除输入框默认内容 *-- # '
def clear(locationType, locatorExpression, *arg):
    global driver
    try:
        getElement(driver, locationType, locatorExpression).clear()
    except Exception as e:
        raise e

'# --* 在页面输入框输入数据 *-- # '
def input_string(locationType, locatorExpression, inputContent):
    global driver
    try:
        getElement(driver, locationType,\
                   locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

'# --* 单机页面元素 *-- # '
def click(locationType, locatorExpression, *arg):
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e

'# --* 断言页面源码是否存在某关键字或关键字符串 *-- # '
def assert_string_in_pagesource(assertString, *arg):
    global driver
    try:
        assert assertString in driver.page_source,\
            u"%s not found in page source!" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

'# --* 断言页面标题是否存在给定的关键字符串 *-- # '
def assert_title(titleStr, *arg):
    global driver
    try:
        assert titleStr in driver.title, u"%r not found in title!" % titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

'# --* 获取页面标题 *-- # '
def getTitle(*arg):
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

'# --* 获取页面源码 *-- # '
def getPageSource(*arg):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

'# --* 切换进入frame *-- # '
def switch_to_frame(locationType, frameLocatorExpression, *arg):
    global driver
    try:
        driver.switch_to.frame(getElement(\
            driver, locationType, frameLocatorExpression))
    except Exception as e:
        print("frame error")
        raise e

'# --* 切出frame，回到默认对话框中 *-- # '
def switch_to_default_content(*arg):
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

'# --* 模拟 Ctrl+V 操作 *-- # '
def paste_string(pasteString, *arg):
    try:
        Clipboard.setText(pasteString)
        time.sleep(2)    # 等待两秒 防止代码执行太快 而未成功粘贴内容
        KeyboardKeys.twoKeys("ctrl", "v")
    except Exception as e:
        raise e

'# --* 模拟 Tab键 操作 *-- # '
def press_tab_key(*arg):
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

'# --* 模拟 enter键 操作 *-- # '
def press_enter_key(*arg):
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

'# --* 窗口最大化 *-- # '
def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

'# --* 截图屏幕图片 *-- # '
def capture_screen(*arg):
    global driver
    currTime = getCurrentTime()    # 获取当前时间，精确到毫秒
    picNameAndPath = str(createCurrentDateDir()) + "//" + str(currTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('//', r'//'))    # 截图屏幕图片，并保存为本地文件
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType, locatorExpression, *arg):
    '''显示等待页面元素出现在DOM树种，但并不一定可见，
        存在测返回该页面元素对象
    '''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise

def waitFrameToBeAvailableAndSwitchToIt(locationType, locatorExpression, *arg):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType, locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType, locatorExpression, *arg):
    '''显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise e





