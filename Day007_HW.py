'''
1. Request 取回之後該怎麼取出資料，資料型態是什麼？
'''
import requests
headers = {'user-agent': 'my-app/0.05'}
r1 = requests.get("https://www.dcard.tw/f") #dcard
r2 = requests.get("https://www.zhihu.com/explore",headers=headers) #知乎
print(type(r1)) #'requests.models.Response'
r2.encoding ="utf-8"
r1_str = r1.text
r2_str = r2.text
print(r1.text) # type = str
print(r2.text) # 403 Forbidden → 要加 headers
'''
2. 為什麼要使用 BeatifulSoup 處理？ 處理後型態為何?
'''
from bs4 import BeautifulSoup
soup1 = BeautifulSoup(r1_str,"html.parser")
soup2 = BeautifulSoup(r2_str,"html.parser")
print(type(soup1)) #'bs4.BeautifulSoup'
'''
3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
'''
#因為解碼問題 encoding = 'utf-8'
