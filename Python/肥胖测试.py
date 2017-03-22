#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#This is my first python script

height = float(input("input your height:"))
weight = float(input("input your weight:"))
bmi = weight/(height**2)
if bmi > 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >=18.5:
    print('正常')
else:
    print('过轻')