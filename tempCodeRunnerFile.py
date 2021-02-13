from grab import Grab
import pycurl
g = Grab()
resp = g.go('https://google.com')
resp.body