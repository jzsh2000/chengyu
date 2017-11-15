#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
Get number of search results for each idiom
'''

import sys
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def search_baidu(word):
    ''' search chengyu in baidu.com '''
    data = urllib.urlencode({'q2': word})
    request = urllib2.Request('http://www.baidu.com/s?' + data)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError:
        return 'error'

    soup = BeautifulSoup(response.read())
    return re.findall('[0-9,]+',
                      soup.find('div', class_="nums").get_text())[0]

if len(sys.argv) == 1:
    sys.stderr.write(' '.join(['python', sys.argv[0], 'chengyu.txt']) + '\n')
    sys.exit(0)
else:
    chengyu_file = sys.argv[1]

with open(chengyu_file, 'r') as chengyu_file:
    while True:
        line = chengyu_file.readline()
        if not line:
            break
        chengyu = line.strip()
        print chengyu, search_baidu(chengyu)
