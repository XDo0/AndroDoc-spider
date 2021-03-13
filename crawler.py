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

def get_one_page(url):
    CON = {}  # the 2-D dict of constants
    METH = {}  # 2-D dict :api name{parameters}

    # soup=BeautifulSoup(open("test.html"),'lxml')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
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
                    val=content[-1].text.replace('\n','')
                    val=val.replace(' ','')
                    val1=val[14:]
                    addtwodimdict(CON,api_name,'value',val1)
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
                            description += str(string)
                    # 添加说明
                    addtwodimdict(METH,api_name,'meanings',description)
                    # 开始遍历表格
                    tables=tag.find_all('table')
                    for pm in tables:
                        key=str(pm.tr.th.string)
                        row = ""
                        for i in range(3,len(pm.contents)-1):
                            para_temp=pm.contents[i]
                            # print(type(para_temp))
                            print(str(para_temp))
                            if str(para_temp)!='\n':
                                para=para_temp.text
                                row+=para.replace('\n',' ')
                                row+=";"
                        addtwodimdict(METH,api_name,key,row)


                    # for tr in pm.tr.next_siblings:
                    #     row+=tr.td.string
                    #     para_td=tr.td.next_sibling
                    #     if para_td.string=="int":
                    #         row+=":"
                    #         for child in para_td.descendants:
                    #             para_tag=child.find('a')
                    #             row+=','.join(para_tag.stripped_strings)
                    #     row += ";"
                    #     addtwodimdict(METH,api_name,key,row)

                    # METH[api_name][pm.th.string]

        except Exception as e:
            print(e)
            pass
    return CON,METH
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

