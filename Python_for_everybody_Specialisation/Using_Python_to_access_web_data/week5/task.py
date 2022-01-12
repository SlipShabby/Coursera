import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL - ')
print('Retrieving ', url)
html = urllib.request.urlopen(url).read()


tree = ET.fromstring(html)
lst = tree.findall('comments/comment/count')
counts = tree.findall('.//count')
sum = 0

for i in lst:
    sum += int(i.text)

print(f'Count: {len(counts)}\nSum: {sum}')
