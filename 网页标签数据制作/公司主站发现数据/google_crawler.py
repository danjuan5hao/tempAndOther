# -*- coding: utf-8 -*-
from selenium import webdriver 
from selenium.webdriver.common.by import By #获取元素
from selenium.webdriver.support.ui import WebDriverWait #设置获取元素超时时间，如果获取失败则抛出异常
from selenium.webdriver.support import expected_conditions as EC #获取元素
from selenium.webdriver.common.keys import Keys  #输入键盘值
from selenium.common.exceptions import TimeoutException # 超时获取元素报错原因
import time #设置延迟
import re #正则表达式模块
from pyquery import PyQuery as pq
browser = webdriver.Chrome()#打开google浏览器
urls = []
def chushi(keyword):  #初始化
    keyword = str(keyword)
    browser.get("https://www.google.com")
    wait = WebDriverWait(browser, 10) #设置获取元素的超时时间为10s
    input = wait.until(EC.presence_of_element_located((By.NAME,"q"))) #获取属性name为q的元素
    input.send_keys(keyword) #输出键盘值
    input.send_keys(Keys.ENTER) #输出回车键
    time.sleep(3) #等待3s
    geturl()

def geturl():
    html = browser.page_source
    list1 = re.findall('<cite.*?>(.*?)<span',html) #获取该标签里的内容
    urls.extend(set(list1)) #set:删除列表里的重复值 extend：在列表末尾添加内容


def next_page():
    try:
        time.sleep(3)
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#pnnext > span:nth-child(2)")))
        button.click() #模拟鼠标右键点击
        time.sleep(1)
        geturl()
    except TimeoutError:
        print("请求失败，正在重新请求")
        next_page()



def save_url():
    with open("url.txt",'w+') as f:
        url = "\n".join(urls)  #str.join：给列表里的内容之间加个换行符输出成字符串
        f.write(url)


if __name__ == '__main__':
    page = 1
    keyword = "ACC Limited"
    if page == 1:
        chushi(keyword)
    #     next_page()
    # else:
    #     chushi(keyword)ACC Limited
    #     for i in range(0, page - 1):
    #         next_page()

    save_url()