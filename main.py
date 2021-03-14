import os
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import writer
import crawler

URL="https://developer.android.google.cn/reference/packages?hl=en"
str1="https://developer.android.google.cn"
str2="?hl=en"

#获得侧边栏Classes目录，e.g.'/reference/android/Manifest'
def get_side_cata(URL=URL):
    urls=[]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    all_catas=soup.find_all(class_="devsite-nav-text")
    for cata in iter(all_catas):
        if cata.text=='Classes':
            cata_section=cata.parent.next_sibling
            for item in cata_section.children:
                urls.append(item.contents[0]['href'])
    return urls

if __name__ == '__main__':
    # url = "https://developer.android.google.cn/reference/android/content/pm/PackageManager?hl=en"
    # CON, METH = crawler.get_one_page(url)
    # writer.writer(CON,METH,url)
    urls=get_side_cata()
    for url in iter(urls):
        url=str1+url+str2
        CON,METH=crawler.get_one_page(url)
        writer.writer(CON,METH,url)