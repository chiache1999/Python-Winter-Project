from bs4 import BeautifulSoup
doc = '''
<html>
      <head>
           <title>The story</title>
      </head>
<body>
      <p class="title-class" id="title-id"><b>The Dormouse's story</b></p>
      <p class="content">
            <a href="http://example.com/link1" class="link" id="link1">A</a>
            <a href="http://example.com/link2" class="link" id="link2">B</a>
            <a href="http://example.com/link3" class="link" id="link3">C</a>
      </p>
</body>
</html>
'''
soup = BeautifulSoup(doc,"html.parser")
print(soup.a)