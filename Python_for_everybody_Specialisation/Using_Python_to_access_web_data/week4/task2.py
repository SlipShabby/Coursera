import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Provide a link: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) -1
i = 0

for i in range(0,count):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position].get('href')
    name = tags[position].contents[0]
    print(f'Retrieving: {url}')
    link = url
    
print(name)
