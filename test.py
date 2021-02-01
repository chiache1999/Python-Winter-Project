import xmltodict

#存取檔案
with open("./example/sample.xml",encoding="utf-8") as fd:
    doc = dict(xmltodict.parse(fd.read()))
print(doc)
#存取我們要的資訊


#用迴圈存取我們的資訊
