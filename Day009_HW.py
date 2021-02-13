'''
比較 requests + beustifulSoup 與 grab + pyQuery 之間的差別
'''
#使用 requests + beautifulSoup

import requests
from bs4 import BeautifulSoup

r = requests.get('https://google.com')
soup = BeautifulSoup(r.text,'lxml')
print(type(soup.title), soup.title.text)

#使用 grab + pyQuery

from grab import Grab
from pyquery import PyQuery as pq

g = Grab()
resp = g.go('https://google.com')
doc = pq(resp.body)
title = doc('title')
print(type(title),title.text())