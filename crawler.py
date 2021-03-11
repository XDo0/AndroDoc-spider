from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re
import pandas
import os

def addtwodimdict(thedict, key_a, key_b, val):
  if key_a in thedict:
    thedict[key_a].update({key_b: val})
  else:
    thedict.update({key_a:{key_b: val}})

CON={}#the 2-D dict of constants
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
            api_name=child_tag['data-text']
            if api_name.isupper():#字母全为大写
                content=tag.find_all('p')
                # get constant value,at index 27
                addtwodimdict(CON,api_name,'value',(content[-1].string[27]))
                # get all of descriptions
                description=""
                for data in iter(content[:-1]):
                    for string in data.stripped_strings:
                        description+=string
                addtwodimdict(CON,api_name,'description',description)

            elif api_name[0].islower(): # 第一个字母小写表示是method
                content = tag.find_all('p')
                description = ""
                for data in iter(content):
                    for string in data.stripped_strings:
                        description += string
                addtwodimdict(METH,api_name,'meanings',description)








    except Exception as e:
        print(e)
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

