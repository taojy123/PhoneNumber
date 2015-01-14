import re

s = open("index2.html").read()

# s = re.sub(r'http://www.51hao.cc/city/.*?/(.*?\.php)', lambda m: './citys/' + m.group(1), s)

s = re.sub(r'"http://www.51hao.cc/city/.*?"', '"#"', s)



open("index3.html", "w").write(s)
