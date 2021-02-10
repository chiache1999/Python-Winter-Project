import requests

url = "https://search.books.com.tw/"
url += "search/query/cat/all/sort/1/v/0/ms2/ms2_1/page/1/key/python"

r = requests.get(url)

print(r.status_code)

if r.status_code == requests.codes.ok:
      print("ok")