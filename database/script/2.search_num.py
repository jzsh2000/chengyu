#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
Get number of search results for each idiom
'''

import urllib
import urllib2
from bs4 import BeautifulSoup
import re

def search_baidu(word):
    data = urllib.urlencode({'q2': word})
    request = urllib2.Request('http://www.baidu.com/s?' + data)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read())
    return re.findall('[0-9,]+',
                     soup.find('div', class_="nums").get_text())[0]

def search_googld(word):
    pass

def search_bing(word):
    pass

with open('test.txt', 'r') as chengyu_file:
    while True:
        line = chengyu_file.readline()
        if not line:
            break
        chengyu = line.strip()
        print chengyu
        print search_baidu(chengyu)