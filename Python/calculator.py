#!/usr/bin/python
# -*- coding: UTF-8 -*-

from operator import *

def calculator(a,b,k):
    return{
        '+':add,
        '-':sub,
        '*':mul,
        '/':truediv,
        '**':pow
    }[k](a,b)

print(calculator(2,3,'+'))
print(calculator(2,3,'*'))
print(calculator(2,3,'/'))