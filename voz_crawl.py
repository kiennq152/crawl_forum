from random import randrange

from selenium import webdriver
from time import sleep
#import pandas in pd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import csv

# def compare_strings(list1,list2):
#     if len(list1)>(len(list2)):
#         for i in list2
#             if list1(i) == list2(i):
#                 i=i+1
#             if i/len(list2) >0.5: return list2
#     else
#         for i in list1
#             if list1(i) == list2(i):
#                 i=i+1
#             if i/len(list1) >0.5: return list1

browser = webdriver.Chrome(ChromeDriverManager().install())

# 1 khai bao bien browser
#browser = webdriver.Chrome(executable_path="./chromedriver")

# 2 Mo thu trang web

browser.get("https://voz.vn/f/diem-bao.33/")
topic_list = browser.find_elements_by_xpath("//div[@class='structItem-title']")
test = browser.find_elements_by_css_selector("a")
link_list = ["Test"]
i=0
for link in test:
    if link.get_attribute('href'):
        ref = link.get_attribute('href')
        if "/t/" in ref:
            if not link_list[i] in link.get_attribute('href'):
                link_list.append(link.get_attribute('href'))
                i=i+1
pp=2

while not browser.get("https://voz.vn/f/diem-bao.33/page-"+str(pp)) and pp<2:
    test = browser.find_elements_by_css_selector("a")
    for link in test:
        if link.get_attribute('href'):
            ref = link.get_attribute('href')
            if "/t/" in ref:
                if not link_list[i] in link.get_attribute('href'):
                    link_list.append(link.get_attribute('href'))
                    i = i + 1
    pp=pp+1
# i = 0
# with open('comment_list.csv', 'w', encoding="utf-8") as file:
#     writer = csv.writer(file)
#     for topic in topic_list:
#         #hien thi cac duong link
#         title = topic.text
#
#         id = topic.id
#
#         writer.writerow([str(id),':',str(title)])
#         i = i+10

# Dung 5 giay
sleep(5)

# vao link
for i in range(len(link_list)):

    browser.get(link_list[i+1])
    sleep(randrange(10))
    #quet comment
    comment_list = browser.find_elements_by_xpath("//div[@class='bbWrapper']")
    with open('comment_list.csv', 'a', encoding="utf-16") as file:
        writer = csv.writer(file)

        for comment in comment_list:
            content = comment.text
            id = comment.id
            print(id,':',content)
            writer.writerow([id+':'+content])
        #chuyen trang
        p=2
        while not browser.get(link_list[i+1]+'page-'+str(p)):
            sleep(randrange(10))
            comment_list = browser.find_elements_by_xpath("//div[@class='bbWrapper']")
            with open('comment_list.csv', 'a', encoding="utf-16") as file:
                writer = csv.writer(file)
                for comment in comment_list:
                    content = comment.text
                    id = comment.id
                    print(id, ':', content)
                    writer.writerow([id + ':' + content])
            p=p+1
    i=i+1
#  Dong
browser.close()