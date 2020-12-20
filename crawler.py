from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re
import pandas
import os


CON={}#the dict of constants
METH={}#2-D dict :api name{parameters}
# response = requests.get("https://developer.android.google.cn/reference/android/content/pm/PackageManager?hl=en#setApplicationEnabledSetting(java.lang.String,%20int,%20int)n")
# soup=BeautifulSoup(response.content,'lxml')
soup=BeautifulSoup(open("test.html"),'lxml')
all_tags=soup.find_all("div",attrs={"data-version-added":True})
for tag in all_tags:
    try:
        child_tag=tag.h3
        #判断是否为method/constant
        if child_tag['class'][0]=="api-name":#多值属性的返回类型是list:
            api_name=child_tag.string
            if api_name.isupper():#字母全为大写
                CON[api_name]=(tag.find_all('p')[-1].string[27])#get constant value,at index 27
            elif api_name[0].islower():
                METH







    except:
        pass

# api_tag=SoupStrainer(class_="api-name")
# # for tag in soup.find_all(api_tag):
# #     print(tag.next_siblings)
# for tag in soup.find_all('div'):
#     # todo:comments
#     print(tag)

    
#     if tag.name.isupper():
#         try:
#
#
#
# response.enconding = "utf-8"
# print(type(response.text))
# with open("test.html", 'w',encoding='utf-8') as f:
#     f.write(response.text)
# f.close()
#<div data-version-added="1" data-version-deprecated="15">


'''
//*[@id="addPackageToPreferred(java.lang.String)"]
//*[@id="addPermission(android.content.pm.PermissionInfo)"]
'''

