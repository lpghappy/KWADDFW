# -*- coding:utf-8 -*-

__author__ = 'boyanru'
__date__ = '2018/03/17'

'''---**--- CreateContacts.py 用于实现向126邮箱添加联系人的数据驱动框架部分  ---**--- '''

from . import *
from testScripts.WriteTestResult import writeTestResult

def dataDriverFun(dataSourceSheetObj, stepSheetObj):
    try:
        # 获取数据源表中是否执行行列对象
        dataIsExecuteColumn = excelObj.getColumn(dataSourceSheetObj,dataSource_isExecute)
        # 获取数据源中“电子邮箱”列对象
        emailColumn = excelObj.getColumn(dataSourceSheetObj,dataSource_email)
        # 获取测试步骤表中存在的数据区域的行数
        stepRowNums = excelObj.getRowsNumber(stepSheetObj)
        # 记录成功执行的数据条数
        succeessDatas = 0
        # 记录被设置为执行的数据条数
        requiredDatas = 0
        for idx, data in enumerate(dataIsExecuteColumn[1:]):
            # 便利数据源表，准备进行数据驱动测试
            # 因为第一行是标题行，所以从第二行开始便利
            if data.value == "y":
                print(u'开始添加联系人 %s"" ' % emailColumn[idx + 1].value)
                requiredDatas +=1
                # 定义记录执行成功步骤数量
                successSTep = 0
                for index in range(2, stepRowNums+1):
                    # 获取数据驱动测试步骤表中
                    # 第index行对象
                    rowObj = excelObj.getRow(stepSheetObj, index)
                    # 获取关键字作为调用的函数名
                    keyWord = rowObj[testStep_keyWorks - 1].value
                    # 获取操作元素的定位方式作为调用函数的参数
                    locationType = rowObj[testStep_locationType - 1].value
                    print("locationType %s" %locationType)
                    # 获取操作元素的定位表达式作为调用函数的参数
                    locatorExpression = rowObj[testStep_locatorExpression-1].value
                    print("locatorExpression %s" %locatorExpression)
                    # 获取操作值作为调用函数的参数
                    operateValue = rowObj[testStep_operateValue-1].value
                    print("operateValue %s" %operateValue)
                    if isinstance(operateValue, int):
                        operateValue=str(operateValue)
                    if operateValue and operateValue.isalpha():
                        # 如果operaValue变量不为空，说明有操作值
                        # 从数据源表中根据坐标获取对应单元格的数据
                        coordinate = operateValue+str(idx+2)
                        operateValue = excelObj.getCellOfValue(dataSourceSheetObj,
                                                               coordinate=coordinate)
                    # 构造需要执行的Python表达式，此表达式对应的是PageAction.py 文件中的页面动作函数调用的字符串表示
                    tmpStr = "'%s', '%s'" % (locationType.lower(), locatorExpression.replace("'", '"'))if locationType and locatorExpression else ""
                    if tmpStr:
                        tmpStr += ", '" + operateValue + "'" if operateValue else""
                    else:
                        tmpStr +=  "'" + operateValue + "'" if operateValue else""
                    # runStr = keyWord + '("+tmpStr")'
                    runStr = keyWord + '(' + tmpStr + ')'
                    # print runStr
                    try:
                        # 通过eval函数，将拼接的页面动作函数调用的字符串表示
                        # 当成有效的Python表达式执行，从而执行测试步骤的sheet
                        # 中关键字在ageAction.py 文件中对应的映射方法，
                        # 来完成对页面元素的操作
                        if operateValue != u"否":
                            # 当 operateValue值为否时，表示不单击星标联机人复选框
                            eval(runStr)
                    except Exception as e:
                        print(u"执行步骤'%s'发生异常" % rowObj[testStep_testStepDescribe-1].value)
                        print(traceback.print_exc())
                    else:
                        successSTep += 1
                        print(u"执行步骤'%s'成功" %rowObj[testStep_testStepDescribe-1].value)
                if stepRowNums == successSTep + 1:
                    succeessDatas += 1
                    # 如果成功执行的步骤数等于步骤表中给出的步骤数，
                    # 说明第idx+2行的数据执行通过，写入通过信息
                    writeTestResult(sheetObj=dataSourceSheetObj,
                                    rowNo=idx+2, colsNo="dataSheet",
                                    testResult="pass")
                else:
                    # 写入失败信息
                    writeTestResult(sheetObj=dataSourceSheetObj, rowNo=idx + 2, colsNo="dataSheet", testResult="faild")
            else:
                # 将不需要执行的数据行的执行时间和执行结果单元格清空
                writeTestResult(sheetObj=dataSourceSheetObj, rowNo=idx+2, colsNo="dataSheet", testResult="")
        if requiredDatas == succeessDatas:
                # 只要当成功执行的数据条数等于被设置为需要执行的数据条数，才表示调用数据驱动的测试用例执行通过
                return 1
        else:
            # 表示调用数据驱动的测试用例执行失败
            return 0

    except Exception as e:
        raise e









