import os
import writer
import crawler

def get_side_cata():
    print('1')

if __name__ == '__main__':
    url = "https://developer.android.google.cn/reference/android/content/pm/PackageManager?hl=en"
    CON, METH = crawler.get_one_page(url)
    writer.writer(CON,METH,url)
