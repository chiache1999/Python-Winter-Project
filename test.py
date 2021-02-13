from grab import Grab
import pycurl
g = Grab()
resp = g.go('https://www.google.com')

#print(resp.body)

from pyquery import PyQuery as pq
doc = pq(resp.body)
h1 = doc('title')
print(type(h1),h1.text())