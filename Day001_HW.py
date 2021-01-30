'''
1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
'''
# 爬蟲屬於主動取得，檔案與API屬於被動取得；
# 檔案與API的不同在於，API允許選擇讀取資料中的特定部分

'''
2.（實作）完成一個程式，需滿足下列需求：
下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
將「Hello World」字串覆寫到 Homework.txt 檔案
檢查 Homework.txt 檔案字數是否符合 Hello World 字數
'''

#引入套件
from urllib.request import urlretrieve
import os

#下載檔案到指定路徑
try:
    os.makedirs('./Data',exist_ok=True)
    url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    urlretrieve(url,"./Data/Homework.txt")
except:
    print("error")

#檢查檔案是否存在

files = os.listdir('./Data') #type=list
if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')

#將 Hello World 字串覆寫至檔案內
rpl_text = 'Hello World'
with open("./Data/Homework.txt",'w') as fh:
    fh.write(rpl_text)
try:
    with open("./Data/Homework.txt",'r') as fh1:
        f = fh1.read()
except EnvironmentError:
    pass

#檢查檔案內的字串長度是否與 "Hello World" 相同
if len(rpl_text) == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')