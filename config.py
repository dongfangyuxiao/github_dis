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
    'Cookie': '_'
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
