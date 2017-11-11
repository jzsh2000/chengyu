#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import sys
import string
import urllib2
from bs4 import BeautifulSoup

url_base = 'http://chengyu.t086.com'

reload(sys)
sys.setdefaultencoding('utf-8')

def extract_chengyu(url):
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        sys.stderr.write(' '.join([str(e.code), e.reason]) + '\n')
        return None

    def convert_nontype(string):
        if string == None:
            return ''
        else:
            return string

    soup = BeautifulSoup(response.read())
    chengyu_res = soup.find('div', id="main").find('table').find_all('td')
    print '\t'.join([chengyu_res[1].string,
                     chengyu_res[3].string,
                     convert_nontype(chengyu_res[5].string)])

def extract_chengyu_list(url):
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        sys.stderr.write(' '.join([str(e.code), e.reason]) + '\n')
        return ''

    soup = BeautifulSoup(response.read())
    for chengyu in soup.find('div', class_="listw").find_all('li'):
        sys.stderr.write(chengyu.a.string + '\n')
        extract_chengyu(url_base + chengyu.a['href'])
    # print soup.prettify()

    page_div = soup.find('div', class_='a2')
    for link in page_div.find_all('a'):
        if link.string == u'下一页':
            return '/'.join([url_base, 'list', link['href']])
    return ''


for letter in string.ascii_uppercase:
    sys.stderr.write('== ' + letter + ' ==\n')
    curpage = letter + '_1.html'
    url = '/'.join([url_base, 'list', curpage])
    while url != '':
        url = extract_chengyu_list(url)
