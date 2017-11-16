#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
Get number of search results for each idiom
'''

import sys
import httplib
import socket
import urllib
import urllib2
import re
import time
import random
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def search_baidu(word):
    ''' search chengyu in baidu.com '''
    data = urllib.urlencode({'q2': word})
    request = urllib2.Request('http://www.baidu.com/s?' + data)

    retry_count = 0
    while True:
        try:
            response = urllib2.urlopen(request, timeout = 1)
            soup = BeautifulSoup(response.read(), "html.parser")
        except socket.timeout:
            sys.stderr.write('Retry [' + word + ']: ' + str(retry_count) + '\n')
            time.sleep(8 + 2 * random.random())
            retry_count += 1
        except urllib2.HTTPError:
            return 'error'
        except httplib.IncompleteRead:
            sys.stderr.write('Retry [' + word + ']: ' + str(retry_count) + '\n')
            time.sleep(3 + 2 * random.random())
            retry_count += 1
        else:
            break

    return re.findall('[0-9,]+',
                      soup.find('div', class_="nums").get_text())[0]

if len(sys.argv) <= 1:
    sys.stderr.write(' '.join(['python', sys.argv[0],
                               'chengyu.txt', '[chengyu.baidu.txt]']) + '\n')
    sys.exit(0)
else:
    chengyu_file = sys.argv[1]
    chengyu_out_file = None
    if len(sys.argv) > 2:
        chengyu_out_file = sys.argv[2]

with open(chengyu_file, 'r') as chengyu_file:
    while True:
        line = chengyu_file.readline()
        if not line:
            break
        chengyu = line.strip()
        chengyu_baidu_res = search_baidu(chengyu)
        if chengyu_out_file is None:
            print chengyu,chengyu_baidu_res
        else:
            with open(chengyu_out_file, 'a') as out_file:
                out_file.write(chengyu + ' ' + chengyu_baidu_res + '\n')

