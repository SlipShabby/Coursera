#!/usr/bin/env python3

import sys

digit_string = sys.argv[1]
print(sum(list(map(int, digit_string))))