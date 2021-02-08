'''
了解知乎 API 使用方式與回傳內容
撰寫程式存取 API 且添加標頭
'''
#下載檔案
#引入套件
import requests
headers = {'user-agent': 'my-app/0.05'}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers=headers)
response = r.text

#轉換成json
import json
import pprint
data = json.loads(response)
#pprint.pprint(data,indent=1) #幫助判斷階層

'''
取出知乎問題發問時間
取出第一筆與最後一筆回答的時間
'''
#設計一個把time stamp轉換為可讀時間字串的function
import time
import datetime
def printTime(ans_time):
    time_stamp = int(ans_time) #設定time stamp
    struct_time = time.localtime(time_stamp) #轉換成時間元組
    timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time) #轉換成字串
    return timeString

#問題發問時間
question_time = data['data'][0]['question']['created']
print("問題發問時間：",printTime(question_time))


#print(len(data['data'])) #5 → 代表第一筆回答為 [1]；最後一筆回答 [4]

firstans_time = data['data'][0]['created_time']
print("第一筆回答時間：",printTime(firstans_time))
lastans_time = data['data'][4]['created_time']
print("最後一筆回答時間：",printTime(lastans_time))

