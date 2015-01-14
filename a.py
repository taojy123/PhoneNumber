import urllib2
import re
import os

page = urllib2.urlopen("http://www.51hao.cc/").read()
links = re.findall(r'href="(http://www.51hao.cc/city/.*?\.php)"\>(.*?)\</A\>', page)
print links

for link, city in links:
    city = link.split("/")[-1].replace(".php", "")
    if os.path.exists(city+".html"):
       continue
    print link
    page = urllib2.urlopen(link).read()
    segments = re.findall(r'<a href=".*?/mobile/.*?html">(.*?)</a>', page)
    open(city+".html", "w").write("\n".join(segments))

print "OK!"




