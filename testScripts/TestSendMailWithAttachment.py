# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

'''---**--- TestSendMailWithAttachment.py 用于实现具体测试逻辑  ---**---'''

from util.ObjectMap import *
from util.KeyBoardUtil import KeyboardKeys
from util.ClipboardUtil import Clipboard
from util.WaitUtil import WaitUtil
from selenium import webdriver
from action.PageAction import *
import time

def TestSendMailWithAttachment():
    print("启动Chrome浏览器")
    open_browser("chrome")
    maximize_browser()
    print("访问126邮箱登录页...")
    visit_url("http://mail.126.com")
    time.sleep(5)
    assert_string_in_pagesource(u"你的专业电子邮局")    # 断言页面出现的关键内容
    print("访问126邮箱登录页成功")
    waitFrameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")    # 显示等待id= "x-URS-iframe"的框架出现，并切换进去
    print("输入登录用户名")
    input_string("xpath", "//input[@name='email']", "boyanru")
    print("输入登录密码")
    input_string("xpath", "//input[@name='password']", "15114644868byr")
    print("登录")
    click("id", "dologin")
    time.sleep(5)
    assert_title(u"网易邮箱")
    print("登录成功")
    print("添加联系人")
    waitVisibilityOfElementLocated("xpath", \
        "//div[text()='通讯录']")    # 显示等待通讯录连接页面元素的出现
    click("xpath", "//div[text()='通讯录']")    # 单机通讯录连接
    click("xpath", "//span[text()='新建联系人']")    # 单击新建联系人按钮
    input_string("xpath",
        "//a[@title='编辑详细姓名']/preceding-sibling::div/input","lily")    # 输入联系人姓名
    input_string("xpath", \
        "//*[@id='iaddress_MAIL_wrap']//input", "lily@qq.com")    # 输入联系人邮箱
    click("xpath", "//span[text()='设为星标联系人']/preceding-sibling::span/b")    # 单击星标联系人复选框
    input_string("xpath", "//*[@id='iaddress_TEL_wrap']//dd//input", "18846937013")    # 输入手机号
    input_string("xpath", "//textarea", "朋友")    # 输入备注信息
    click("xpath", "//span[text()='确 定']")
    time.sleep(1)
    assert_string_in_pagesource("lily@qq.com")
    print("添加联系人成功")
    time.sleep(2)
    click("xpath", "//div[.='首页']")
    waitVisibilityOfElementLocated("xpath", "//span[text()='写 信']")
    click("xpath", "//span[text()='写 信']")
    print("开始写信")
    print("输入收件人地址")
    input_string("xpath", \
        "//div[contains(@id,'_mail_emailinput')]/input", "boyanru_kindy@163.com")
    print("输入邮件主题")
    input_string("xpath", \
        "//div[@aria-label='邮件主题输入框，请输入邮件主题']//input", "新邮件")
    print("单击上传附件按钮")
    click("xpath", "//div[contains(@title,'点击添加附件')]")
    time.sleep(2)
    print("上传附件")
    paste_string("a.txt")
    press_enter_key()     # 按Enter回车键，上传附件
    waitVisibilityOfElementLocated("xpath", '//span[text()="上传完成"]')
    print("上传附件成功")
    waitFrameToBeAvailableAndSwitchToIt("xpath", "//iframe[@tabindex=1]")    # 切换进邮件正文的frame
    print("写入邮件正文")
    input_string("xpath", "/html/body", "发给关荣之路的一封信")
    switch_to_default_content()    # 切出邮件正文的frame框
    print("写信完成")
    click("xpath", "//header//span[text()='发送']")
    print("开始发送邮件...")
    time.sleep(3)
    assert_string_in_pagesource("发送成功")
    print("邮件发送成功")
    close_browser()


if __name__ == '__main__':
    TestSendMailWithAttachment()













