# -*- coding: UTF-8 -*-

"""
for i in range(100, 1000):
    a = i // 100
    b = (i % 100) // 10
    c = (i % 100) % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
"""

while True:
    inp_l = input('下限: ')
    inp_h = input('上限: ')
    if inp_l == 'e' or inp_h == 'e':
        break
    try:
        inp_l, inp_h = int(inp_l), int(inp_h)
    except ValueError:
        print('不合法')
        continue
    for n in range(inp_l, inp_h):
        i = n/100
        j = n/10 % 10
        k = n % 10
        if i*100+j*10+k == i+j**2+k**3:
            print("%-5d" % n)
        print("hello")