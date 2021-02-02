'''
1. 比較 File I/O 與 xmltodict 讀出來的內容差異
'''

#引入需要的套件
import urllib.request
import zipfile
import os, sys
import xmltodict

#下載檔案
res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res, "./data/example.zip")
f = zipfile.ZipFile('./data/example.zip')
f.extractall('./data')

with open('./example/sample.xml',encoding='utf-8') as fh:
    #用File I/O
    content = fh.read()
    print(content)
    print(type(content)) #string
    #用 xmltodict
    doc = xmltodict.parse(content)
    print(dict(doc)) #dict (orderDict)
    
'''
可以發現用 File I/O 讀出來的是string，保持原先<標籤> </標籤>的樣貌
而 xmltodict 則是 OrderDict 的形式
如果使用 File I/O 就算用 readlines 也很難單獨取出內容或屬性的值
'''

'''
2.請問高雄市有多少地區有溫度資料？
請取出每一個地區所記錄的第一個時間點跟溫度
請取出第一個地區所記錄的每一個時間點跟溫度
'''

with open('./data/64_72hr_CH.xml', "r",encoding="utf-8") as fd:
    xml = fd.read()
    doc2 = xmltodict.parse(xml)
    dic_xml = dict(doc2)
    #print(dic_xml)
    
#有多少地區有溫度資料 
locations = dic_xml['cwbopendata']['dataset']['locations']['location']
print(len(locations)) #38

#請取出每一個地區所記錄的第一個時間點跟溫度
for location in locations:
    lc_name = location['locationName']
    lc_1st_time = location['weatherElement'][0]['time'][0]['dataTime']
    lc_1st_temp = location['weatherElement'][0]['time'][0]['elementValue']['value']
    print(lc_name,lc_1st_time,lc_1st_temp)

#請取出第一個地區所記錄的每一個時間點跟溫度
lc1 = locations[0]['weatherElement'][0]['time']
for data in lc1:
    time = data['dataTime']
    temp = data['elementValue']['value']
    print(time,temp)