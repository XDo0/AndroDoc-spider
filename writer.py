import os
import csv
# https://developer.android.google.cn/reference/android/content/pm/PackageManager?hl=en

RES_DIR= "D:\mycode\py\crawldata"
def get_dir(url):
    directory=url[:-6]
    directory=directory[46:]
    dirr=directory.split('/')
    directory=os.path.join(*dirr)
    path=os.path.join(RES_DIR,directory)
    if not os.path.exists(path):
        os.makedirs(path)
    con_file=os.path.join(path,"cons.csv")
    meth_file=os.path.join(path,"meth.csv")
    return con_file,meth_file

def init_CON(con_file):
    with open(con_file, "w", encoding="utf8", newline="") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(['constant','value','description'])


def init_METH(meth_file):
    with open(meth_file, "w", encoding="utf8", newline="") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(['method','meanings','parameters','returns','throws'])

def is_key_in_METH(METH,api_name,key,temp):
    if key in METH[api_name]:
        temp.append(METH[api_name][key])
    else:
        temp.append(" ")

def write_CON(CON,con_file):
    # constant,value,description
    init_CON(con_file)
    with open(con_file, 'a+', encoding="utf8", newline="") as csvfile:
        f=csv.writer(csvfile)
        for api_name in CON:
            temp=[]
            temp.append(api_name)
            temp.append(CON[api_name]['value'])
            temp.append(CON[api_name]['description'])
            f.writerow(temp)




def write_METH(METH,meth_file):
    #method,meanings,parameters,returns,throws
    init_METH(meth_file)
    with open(meth_file, 'a+', encoding="utf8", newline="") as csvfile:
        f=csv.writer(csvfile)
        for api_name in METH:
            temp=[]
            temp.append(api_name)
            is_key_in_METH(METH,api_name,'meanings',temp)
            is_key_in_METH(METH,api_name,'parameters',temp)
            is_key_in_METH(METH,api_name,'returns',temp)
            is_key_in_METH(METH,api_name,'throws',temp)
            f.writerow(temp)


def writer(CON,METH,url):
    con_file,meth_file=get_dir(url)
    write_CON(CON,con_file)
    write_METH(METH,meth_file)
