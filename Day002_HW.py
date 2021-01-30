'''
1. 比較以 File I/O 與 CSV 讀取之差異
'''
#引入套件
from urllib.request import urlretrieve
import os
import csv
import json

#下載檔案
res = "https://cumatrixfile.cupoy.com/0000017714F8929D000000026375706F795F70726572656C656173654349/marathon/example.csv?t=1610964571348"
urlretrieve(res,'./example.csv')

#確認檔案是否存在
if os.path.exists('example.csv')==True:
    pass
else:
    print('檔案存取失敗')    

#以 File I/O
with open('example.csv','r',newline='',encoding='utf-8') as fh:
    content1 = fh.readlines()
    for row1 in content1:
        print(row1)
        print(type(row1)) #string

#以 CSV
with open('example.csv','r',newline='',encoding='utf-8') as fh:
    content2 = csv.reader(fh, delimiter=',')
    for row2 in content2:
        print(row2)
        print(type(row2)) #list

'''
兩者最大的差異在於 File I/O read 每一格是同一個 string 內以逗號隔開；
用 CSV read 每一行是一個 list，每一格為 list 內的一個元素
'''

'''
2-1. 取出班次一的每一個時間 (這裡以csv為例)
2-2. 將班次一的每一個時間用一種資料型態保存
2-3. 將班次一到五與其所有時間用個別一種資料型態保存
→ 使用 json 型態，既能保有 list 的順序，也能有 dict 的 value & key 特性
'''
#把每個序號做為 key，底下的 value 再依序把[路線編號]、[起訖站]...當作 key
bus_dict = {}
i = 0
key_list = []
with open('example.csv','r',newline='',encoding='utf-8') as fh:
    content2 = csv.reader(fh, delimiter=',')
    for row2 in content2:
        if i == 0:
            key_list = row2
            i += 1
        else:
            temp_dict = {}
            for k in range(1,len(row2)):
                temp_dict[key_list[k]] = row2[k]
            bus_dict[row2[0]] = temp_dict
#print(bus_dict)
#取出班次一到班次五的每一個時間存成個別的 dict，在放入 list 內 → 形成 json
bus_schs = []
for j in range(0,4):
    bus_sch = {}
    for i in range(5,15):
        bus_sch[key_list[i]] = bus_dict['1'][key_list[i]]
    bus_schs.append(bus_sch)
#轉換成json
json_bus_schs = json.dumps(bus_schs)
print(type(json_bus_schs)) #str
print(json.loads(json_bus_schs))
print(type(json.loads(json_bus_schs))) #list