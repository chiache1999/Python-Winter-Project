#引入套件
from urllib.request import urlretrieve
import requests
import os
import json
from bs4 import BeautifulSoup
from PIL import Image 

#取得soup
url = 'https://www.ptt.cc/bbs/Beauty/M.1574854555.A.E5C.html'
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
resp = requests.get(url, cookies = {'over18': '1'},headers = headers) #ptt 會問是否滿18
soup = BeautifulSoup(resp.text,"html.parser")
#print(soup.prettify())

#儲存的資料夾
output_dir = 'downloads'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#找出所有圖片的tag
image_tags = soup.find(id = 'main-content').findChildren('a',recursive=False) #是否只針對tag的direct children
for img_tag in image_tags:
    if 'imgur' not in img_tag['href']:
        continue #若非圖片，跳過這次迴圈
    img_id = img_tag['href'].split('/')[-1]
    #print(img_id)
    img_url = 'https://i.imgur.com/{}.jpg'.format(img_id)
    with requests.get(img_url,stream = True) as r: #stream 會跟網路建立通道，將檔案分不同 chunk 下載
        r.raise_for_status() #check if any error occurs
        img = Image.open(r.raw)
        #print(img.format) #確認檔案格式
        img_save_name = '{outdir}/{img_id}.{img_form}'.format(outdir = output_dir,img_id = img_id,img_form = img.format.lower())
        #print(img_save_name)
        img.save(img_save_name)
    

