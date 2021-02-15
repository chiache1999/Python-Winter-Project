'''
在網路爬蟲當中，正規表達式常常用來過濾以及搜尋特定的pattern字串。
今天要來練習過濾IP address，以及URL。
一個合法的網路IP address，其格式為：X.X.X.X, 其中X是0~255的數字。我們可以用一個regex，來表達IP address的內容。
'''
import re
#建立一個判斷的 function
def RegexMatchingTest(regex, imput_text):
    pattern = re.compile(regex) #轉換pattern
    result = re.search(pattern, imput_text)

    if result:
        # 匹配完的結果會儲存在group()的屬性中，我們可以把匹配的結果列印出來
        print("Matched: %s" % (result.group()))
        
        if result.lastindex is not None:
            # group(0)代表整個字串，group(1)、group(2)...代表分組中，匹配的內容
            for i in range(0, result.lastindex+1):
                print("  group(%d): %s" % (i, result.group(i)))
    else:
        print("Not matched.")

regex = "(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])"

test_string1 = "Test IP 21.58.200.227"
RegexMatchingTest(regex, test_string1)  #測試表達式是否會匹配此合法IP

test_string2 = "Test IP 999.888.777.666"
RegexMatchingTest(regex, test_string2)  #測試表達式是否會匹配此不合法IP

'''
用正規表達式過濾URL。
在網頁爬蟲中，常常會有外部連結的A tag，例如：
< a href="https://movies.yahoo.com.tw/movietime_result.html/id=9467"> 時刻表 < /a >

我們要把"href="之後的URL擷取出來，用來做後續處理。
'''

html_a_tag = "<a href=https://movies.yahoo.com.tw/movietime_result.html/id=9467> 時刻表 </a>"

regex = 'a href=[^>]+' #[^>] 比對非">"的字元 
RegexMatchingTest(regex, html_a_tag)