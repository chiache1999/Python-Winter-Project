import requests

headers = {'user-agent':'my-app/0.05'}
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers=headers)

print(r.text)