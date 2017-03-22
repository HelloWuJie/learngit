# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:58:01 2017

@author: WJ
"""
import math

def func1(x):  
    sum = 0 
    for i in range(x+1):
        sum += i
    return(sum)

def my_abs(x):
    if(not isinstance(x,(int,float))):    #检查参数类型
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
        
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    
    if a == 0:
        print("此乃一元一次方程")
        ys = math.gcd(b,c)
        tmp1 = b/ys
        tmp2= c/ys
        if tmp1 == tmp2:
            return '-1'
        else:
            x = '-%d/%d'%(tmp2,tmp1)
            return x
    
    if b**2-4*a*c < 0:
        print("此方程无解")
        return;
    else:
        x1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = ((-b)-math.sqrt(b**2-4*a*c))/(2*a)
        if x1 != x2:
            return x1,x2
        else:
            return x1
    
def power(x,n=2):
    y = x**n
    return y
    
print(power(5))