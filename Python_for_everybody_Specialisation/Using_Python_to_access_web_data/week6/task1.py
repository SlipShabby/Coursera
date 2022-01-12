import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url:')

data = urllib.request.urlopen(url).read()

info= json.loads(data)

sum = 0
for i in info['comments']:
    sum += int(i['count'])

print(sum)

