#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
Create chengyu database from web resource
'''

import sys
import string
import urllib2
from bs4 import BeautifulSoup

URL_BASE = 'http://chengyu.t086.com'

reload(sys)
sys.setdefaultencoding('utf-8')

def extract_chengyu(url, chengyu):
    '''
    extract detailed chengyu info from page like:
    http://chengyu.t086.com/cy0/1.html
    '''
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, err:
        sys.stderr.write(' '.join([str(err.code), err.reason]) + '\n')
        return None

    def convert_nontype(mystring):
        ''' convert nontype to empty string '''
        if mystring is None:
            mystring = ''
        return mystring

    soup = BeautifulSoup(response.read(), "html.parser")
    if not soup.find('div', id="main"):
        with open('db.err.txt', 'a') as res_file:
            res_file.write(chengyu + '\n')
    else:
        chengyu_res = soup.find('div', id="main").find('table').find_all('td')
        with open('db.txt', 'a') as res_file:
            res_file.write('\t'.join([chengyu_res[1].string,
                                      chengyu_res[3].string,
                                      convert_nontype(chengyu_res[5].string)]) +
                           '\n')

def extract_chengyu_list(url):
    '''
    extract chengyu list from page like:
    http://chengyu.t086.com/list/A_1.html
    '''
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, err:
        sys.stderr.write(' '.join([str(err.code), err.reason]) + '\n')
        return ''

    soup = BeautifulSoup(response.read(), "html.parser")
    for chengyu in soup.find('div', class_="listw").find_all('li'):
        sys.stderr.write(chengyu.a.string + '\n')
        extract_chengyu(URL_BASE + chengyu.a['href'], chengyu.a.string)
    # print soup.prettify()

    page_div = soup.find('div', class_='a2')
    for link in page_div.find_all('a'):
        if link.string == u'下一页':
            return '/'.join([URL_BASE, 'list', link['href']])
    return ''


for letter in string.ascii_uppercase:
    sys.stderr.write('== ' + letter + ' ==\n')
    curpage = letter + '_1.html'
    myurl = '/'.join([URL_BASE, 'list', curpage])
    while myurl != '':
        myurl = extract_chengyu_list(myurl)
