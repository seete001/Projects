import urllib.request
import xml.etree.ElementTree as ET
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#https://py4e-data.dr-chuck.net/comments_2213691.xml
url = input('Enter URL: ')

xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
lst= tree.findall('comments/comment')
#print(lst)
total = 0
for item in lst:
    total +=int(item.find('count').text)

print(total)