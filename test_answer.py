# coding=utf-8
import time
from selenium import webdriver
import importlib,sys
from selenium.webdriver.common.keys import Keys
importlib.reload(sys)

#username = "500113199702287816"
#pwd = "zhu15696236105"

username = "13921599121"
pwd = "qp590cee"

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

def find_topic(title):#找到桶一道题目的标题
    file = open("maogai.txt")
    file_temp = open("temp.txt", "w+")
    keys = 0
    find_option_key = 0
    option_Number = 0
    option_flag = 0#录入选项 找到第二次换行停止
    for line in file:
        if title in line:
            keys = keys + 1#找题目
            print("找到题目")
        if keys:
            file_temp.write(line)#写入选项
            if line == "\n":
                if option_flag == 1:
                    print("录入一道题完成")
                    break
                option_flag += 1
                find_option_key = 1
            if find_option_key == 1:
                option_Number = option_Number + 1
    file.close()
    file_temp.close()
    return option_Number-1

def select(answer,key):#确定选项是否正确
    file_temp = open("temp.txt")
    for line in file_temp:
        if answer in line:
            if "?" in line:
                try:
                    click_answer = driver.find_elements_by_css_selector\
                        ("ul.exes_option > li > input")#找到所有的选项
                    driver.execute_script("arguments[0].click();", click_answer[key])
                    print(answer)
                    return 1
                except:
                    # xt_12402 > ul > li:nth-child(1) > input[type="radio"]
                    # xt_12403 > ul > li:nth-child(1)
                    # xt_12402 > p
                    print("这道题已选")
                break
            else:
                break
    file_temp.close()
    return 0

def click_ensure_submit():#提交
    try:
        click_submit = driver.find_element_by_css_selector("#s2 > a")
        driver.execute_script("arguments[0].click();",click_submit)
        click_ensure = driver.find_element_by_css_selector("body > div.aui_state_lock.aui_state_focus > div > "
           "table > tbody > tr:nth-child(2) > td.aui_c > div > table > tbody > tr:nth-child(3) "
           "> td > div > button.aui_state_highlight").click()
    except:
       print("答题已完成")

for i in range(2031, 2123):
    flag = 0
    capterKeys = "#j_%d > a" % i
    try:
        clickCapter = driver.find_element_by_css_selector(capterKeys)
        # clickCapter = driver.find_element_by_css_selector(capterKeys)
        driver.execute_script("arguments[0].click();", clickCapter)
        flag = 1
        time.sleep(3)
    except:
        print("这章没有")
        print(i)

    if flag == 1:
        topic_S = driver.find_elements_by_css_selector("ul>li>p")
        # 找到所有的选项
        Option = driver.find_elements_by_css_selector("ul.exes_option > li")
        # xt_12407 > ul > li:nth-child(1)
        # 判断哪些是单选题，哪些是多选题
        title = driver.find_elements_by_css_selector("dd.bookExes_list>ul>li>h5")
        sum_option = 0  # 每道题的选项的总和
        for i in topic_S:
            option_Number = find_topic(i.text)  # 在文件当中找到这道题,并计算这道有几个选项
            print("选项数" + str(option_Number))
            option_Number_Key = 0
            for j in range(sum_option, sum_option + option_Number):
                select(Option[j].text, j)
            sum_option += option_Number
        click_ensure_submit()
        chapter = driver.find_elements_by_css_selector("dd>ul>li>a")  # 重新获取页面，新加载的页面

