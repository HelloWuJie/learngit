# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:57:50 2017

@author: WJ
"""

from functools import reduce

def str2int(s):
    def fn(x,y):
        return(x*10+y)
    def char2num(s):
        return {'0': 0, '1': 1,\
                '2': 2, '3': 3,\
                '4': 4, '5': 5,\
                '6': 6, '7': 7,\
                '8': 8, '9': 9}[s]
    
    return reduce(fn, map(char2num, s))

print(str2int('12345'))
