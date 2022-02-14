import sys
from math import sqrt

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

x1 = int((-b + sqrt(b**2 - 4*a*c))/(2*a))
x2 = int((-b - sqrt(b**2 - 4*a*c))/(2*a))

print(x1)
print(x2)