# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
username = "15123406200"
pwd = "ZHONG3daxue"

driver = webdriver.Chrome()
driver.get('http://www.attop.com/wk/index.htm?id=73')
element = driver.find_element_by_link_text("登录").click()
time.sleep(1)
alert = driver.switch_to.frame("pageiframe")
time.sleep(1)#转化到登录界面的iframe
alert = driver.find_element_by_id("username").send_keys(username)
alert = driver.find_element_by_id("password").send_keys(pwd)
time.sleep(6)#等待输入验证码
alert = driver.switch_to.default_content()
select_title = driver.find_element_by_link_text("课程学习").click()
time.sleep(2)
def MedEvaluate():
    temp = 1
    for i in range(1, 90):
        temp = temp + 1
        myKeys = 0
        findEvaluate = 0
        try:
            mySelector_evaluate = "#showajaxinfo > div:nth-child(2) > dl > dd > p:nth-child(%d)" % i
            evaluate = driver.find_element_by_css_selector(mySelector_evaluate)
            # 利用css定位元素 媒体评价
        except NoSuchElementException:
            print("这个不用评")
        #    findEvaluate = findEvaluate + 1
        #if findEvaluate == 2:
        #    break
        try:
            driver.execute_script("arguments[0].click();", evaluate)
            # 利用script点击按钮，可以防止元素未出现在界面中而不能点击出现异常
            evaluate = driver.switch_to.frame("pageiframe")  # 转换到媒体评价的iframe
            evaluate = driver.find_element_by_class_name("ping_btn_3").click()  # 点击“很好”评价
            time.sleep(1)
            evaluate = driver.find_element_by_class_name("aui_state_highlight").click()  # 点击确定评价
            evaluate = driver.switch_to.default_content()  # 回到主界面不用点击关闭按钮就可以直接定位主界面的元素
            myKeys = 1
        except:
            print("进行下一个评价")
            if myKeys == 0:
                evaluate = driver.switch_to.default_content()
        else:
            print("进行下一个评价")
        print(temp)
        #最开始是2034
        # j_2046 > a
        # j_2045 > a
for i in range(2045,2123):
    flag = 0
    capterKeys = "#j_%d > a" % i
    try:
        clickCapter = driver.find_element_by_css_selector(capterKeys)
        #clickCapter = driver.find_element_by_css_selector(capterKeys)
        driver.execute_script("arguments[0].click();",clickCapter)
    except:
        print("这章没有")
        print(i)
        flag = 1
    if (flag == 0):
        MedEvaluate()
