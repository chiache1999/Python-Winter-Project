'''
1. 比較一下範例檔中的 "r.text" 與 "json.loads(r.text)" 讀出的內容有何差異
'''
import requests
import json

r = requests.get("https://api.github.com/events")
print(r.text)
print(type(r.text)) #string
print(json.loads(r.text))
print(type(json.loads(r.text))) #list → json type list&dict組成的結構

'''
r.text 讀出的內容 type = string，是字串無法階層的取出
而經過 json.loads 後會呈現 json 的資料形式 (list 或 dict)，可以按照規則，用編號或key取出想要的資料
'''

'''
2. 自行找一個適合的接口做練習，並且查看其回傳內容
'''
z = requests.get("https://cat-fact.herokuapp.com/facts")
print(z.text) #是一個有關貓冷門知識的網站!

y = requests.get("http://odata.wra.gov.tw/v4/RealtimeWaterLevel")
print(y.text) #這個網站似乎已經沒有資料了!