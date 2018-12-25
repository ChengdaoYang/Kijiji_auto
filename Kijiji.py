import time
import random
import os
from selenium import webdriver

# 尝试login 账号
login_url = "https://www.kijiji.ca/t-login.html"

#set chrome driver to headerless
#option_ = Options()
#option_.add_argument('--headless')

#create driver to scrape
driver = webdriver.Chrome()
driver.implicitly_wait(0.01)
driver.get(login_url)
time.sleep(2)

#输入 账号&密码 登陆
# driver.find_element_by_xpath("//input[@id='LoginEmailOrNickname']").click()
driver.find_element_by_xpath("//input[@id='LoginEmailOrNickname']").clear()
driver.find_element_by_xpath("//input[@id='LoginEmailOrNickname']").send_keys('')
time.sleep(random.random())
driver.find_element_by_xpath("//input[@id='login-password']").clear()
driver.find_element_by_xpath("//input[@id='login-password']").send_keys('')
time.sleep(random.random())
driver.find_element_by_xpath("//button[@id='SignInButton']").click()
time.sleep(4)

#创建广告
ad_url = 'https://www.kijiji.ca/p-select-category.html'
driver.get(ad_url)
driver.implicitly_wait(0.8)
time.sleep(4)

#输入 标题
title_text = """Gardening K-florist"""
driver.find_element_by_xpath("//textarea[@class='textArea-3119612379']").send_keys(title_text)
driver.implicitly_wait(1)
driver.find_element_by_tag_name("button").click()
time.sleep(5)

#选择 categories
cate_buttons = driver.find_elements_by_tag_name('button')
cate_buttons[5].click()
time.sleep(3.3)

sub_cate_buttons = driver.find_elements_by_tag_name('button')
sub_cate_buttons[13].click()
time.sleep(3.5)

subsub_cate_buttons = driver.find_elements_by_tag_name('button')
subsub_cate_buttons[-1].click()
time.sleep(3.2)

#编写内容
description_text = 'xxxxxxxx'
driver.find_element_by_xpath("//textarea[@id='pstad-descrptn']").send_keys(description_text)
time.sleep(1)

address_text = 'l4a 0r7'
driver.find_element_by_xpath("//input[@id='pstad-map-address']").send_keys(address_text)
time.sleep(1.2)

phone_text = '6478668912'
driver.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_text)
time.sleep(0.8)

#upload photos
driver.find_element_by_id('ImageUploadButton').send_keys(os.getcwd()+"/Excel.png")
time.sleep(1)

#choose Free package
pkg_buttons = driver.find_elements_by_xpath("//button[@color='blue']")
pkg_buttons[1].click()
