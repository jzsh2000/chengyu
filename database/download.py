#!/usr/bin/env python2
import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request("http://chengyu.t086.com/")
try:
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read())
    print soup.prettify()
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"