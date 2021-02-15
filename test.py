import re
regex = '((abcde)\s\d+)'
pattern = re.compile(regex)
test_str = 'abcde 21dkksabcde 223'
result = re.search(pattern,test_str)
print(result.lastindex)