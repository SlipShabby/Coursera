import urllib.request
from bs4 import BeautifulSoup

link = input('Provide a link: ')

with urllib.request.urlopen(link) as url:
    html= url.read()

soup = BeautifulSoup(html, "html.parser")
tag = soup('span')

count = 0
sum = 0 

for i in tag:
    x = int(i.text)
    count += 1
    sum += x

print(f'Count: {count}\nSum: {sum}')