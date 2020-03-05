#!/user/bin/env python3
# -*- coding: utf-8 -*-

def product(*x):
    a = 1
    for i in x:
        a = a * i
    return a
    
b = [1,2,3]
c = product(*b)
print(c)

