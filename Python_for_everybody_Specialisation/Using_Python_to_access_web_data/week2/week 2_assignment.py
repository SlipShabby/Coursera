import re

with open('week2.txt') as file:
    str = file.read()
 
l = re.findall('[0-9]+', str)

sum = 0
count = len(l)
for i in range(0,len(l)):
    sum += int(l[i])
    # count += 1


print(sum)