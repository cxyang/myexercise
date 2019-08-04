# !/usr/bin/env Python
# -*- coding: UTF-8 -*-

import math

list = []

for i in range(100, 1000):
    x = math.floor(i / 100)
    y = math.floor((i - x * 100) / 10)
    z = i - math.floor(i / 10) * 10
    if i == x ** 3 + y ** 3 + z ** 3:
        list.append(str(i))
print(", ".join(tuple(list)))



