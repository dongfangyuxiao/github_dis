#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import math
import time
import random
headers = {
    'Accept': '*/*',
    'Referer': 'https://github.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0 ',
    'Cache-Control': 'no-cache',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cookie': '_ga=GA1.2.338497014.1545292375; _octo=GH1.1.1984643585.1545292378; tz=Asia%2FShanghai; has_recent_activity=1; user_session=JwIq47d4aYaDg1JKDDmoeuSqJJMEqSKhPI9fAEDuoSw9AGxa; __Host-user_session_same_site=JwIq47d4aYaDg1JKDDmoeuSqJJMEqSKhPI9fAEDuoSw9AGxa; logged_in=yes; dotcom_user=dongfangyuxiao; _gat=1; _gh_sess=UXBScm5YWWx5dDV0bVFJZFNtM0RNZEEvcEFMcmtaaWFYeFF6T3dKSDcxR3NtUXB3NlJkaHVsemI5YWRlS1RTOUg2Sit3bWxaNFg0UWh4Wmg2R09IK3FLeURSSnd0ajQ2K2xnOUVLR1phb3ZaYy82akcycmxYNnpsODVOQ2M5cTgwaVZxV0lMRGJ0S3hYZ0thN1hiNFRWWlBmZ0tsY3JZTEhtRWFvVVNybDBOTnFvTzhFWDFWR3hrbWY4bFcwR1grRU43dWFBNlBCeEUxdG5ZSldrSCsvOVV6ZEpydDk4d3AvNGhPV1YyRnVaNnZEc1hWUkhmT2xOd05YOU5PdHd1Ny0tMHlwMXE2WUhrcC9vbVN3OXkvQk0yUT09--3ecd9e84d753e82c9d56bd7c63272b1154a826ca'
}

def write(line):
    with open('github.txt','a+') as f:
        f.write(line+'\n')

def exceptwrite(line):
    with open('exceptwrite.txt','a+') as f:
        f.write(line+'\n')
def search(keyword,type):
    pattern = re.compile('data-search-type="Code">(\d+)</span>')
    url = "https://github.com/search?q={0}+{1}&type=Code".format(keyword,type)
    write(keyword+type)
    print url
    try:
        res = requests.get(url,headers=headers,timeout=3,verify=False)
        #print res.content
        pages = pattern.findall(res.content)
        pmax = int(math.ceil(int(pages[0])/10)+2)
        #print pmax
        code_pattern = re.compile('href="(.*?)#')
        time.sleep(random.uniform(1, 2))
        for p in range(1,pmax):
            courl = "https://github.com/search?p={0}&q={1}+{2}&type=Code".format(p,keyword,type)
            try:
                resc = requests.get(courl,headers=headers,timeout=5,verify=False)
                code_list = code_pattern.findall(resc.content)
                for x in code_list:
                    if '.html' in x:
                        pass
                    elif '.js' in x:
                        pass
                    else:
                        write(x)
                    #print x
                #time.sleep(random.uniform(1, 3))
            except Exception as e:
                print e
                exceptwrite(courl)


    except Exception as e:
        print e
        exceptwrite(url)

def main():
    keywords = []
    types = []
    fk = open('keyword.txt','rb')
    fl = open('type.txt','rb')
    for line in fk.readlines():
        line = line.strip()
        keywords.append(line)
    for  line2 in fl.readlines():
        line2 = line2.strip()
        types.append(line2)
    for keyword in keywords:
        for type in types:
            search(keyword,type)

if __name__ == "__main__":
    main()
