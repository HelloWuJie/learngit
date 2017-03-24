# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:58:01 2017

@author: WJ
"""
import math

'''
def func1(x):  
    sum = 0 
    for i in range(x+1):
        sum += i
    return(sum)

#检查参数类型
def my_abs(x):
    if(not isinstance(x,(int,float))):    #检查参数类型
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

#坐标移动        
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

#ax^2+bx+c=0 求解
def quadratic(*args):
    a,b,c = args
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

def f1(*args):
    print ('args = ',args)


#N的阶乘计算
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

#N的阶乘计算，方法二
def fact_iter(num, res=1):
    if num == 1:
        return res
    a = num-1
    b = num*res
    return fact_iter(a,b)

#汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('%s --> %s'%(a,c))
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


L = ['a','b','c','d']
r = []
n = 3
for i in range(3):
    r.append(L[i])
print(r)


L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])

def fib(max):
    n, a, b  = 0, 0 ,1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return

f = fib(6)
[print(i) for i in f]


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

'''
def triangles():
    L = [1]
    while 1:
        yield L
        T = []
        L.append(0)
        for i in range(len(L)):
            T.append(L[i-1] + L[i])
        L = T

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
