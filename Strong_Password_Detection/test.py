import re

string1 = 'you do, http://www.baidu.cn/when you gethttp://www.baidu.com'

reg = re.compile(r'http[s]{0,1}://[\w\.]+(?:\.com|\.cn)')  # ?:不表示是一个组

result = reg.findall(string1)

print(result)