# -*- coding: UTF-8 -*-

a_string = "This is a global variable"

def foo():
     print(a_string) # 1
foo()

def two(x, y, *args):
    print(x, y, args)

two("a", "b", "c")
