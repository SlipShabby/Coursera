#!/usr/bin/env python3
import sys

num = int(sys.argv[1])

for i in range(1, num + 1):
    print(' '*(num-i)+'#'*i)