import re
import requests

URL = input("Wordpress URL: ")

response = requests.get(URL+"/feed/")
with open('feed.xml', 'wb') as file:
    file.write(response.content)
f = open('feed.xml','r')
res = f.readlines()
for d in res:
    data = re.findall('<link>(https:\/\/.+)<\/link>',d)
for i in data:
   print(i)