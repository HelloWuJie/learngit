# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:58:01 2017

@author: WJ
"""
import math
from functools import reduce

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

'''

'''
def findMinAndMax(L):
    if len(L) == 0:
        return ('None','None')
    min  = max = L[0]
    
    for x in L:
        if x < min: min = x
        if x >max: max = x
    return(min,max)

L  = [1,2,3,4,5]
M = findMinAndMax(L)
print(M)


def line_conf(a,b):
    def line(x):
        return (a*x + b)
    return line

line_A = line_conf(2,1)
print(line_A(1))

def who(name):
    def do(what):
        print(name,"say",what)
    return do

Jack = who('Jack')
Lily = who('Lily')

Jack('i want to fuck you!')
Lily('oh yeah~') 


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：


def fn(str):
    T = ''
    for x in range(len(str)):
        if x == 0:
            T = str[0].upper()
        else:
            T = T + str[x].lower()
    return T

def fn(str):
    T = ''
    for k,v in enumerate(str):
        if k == 0:
            T = T + v.upper()
        else:
            T = T + v.lower()
    return T

def normalize(name):
    return map(fn, name)

L = ['adam','LISA','barT']
print(list(normalize(L)))

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)

L = [1,2,3,4]
print(prod(L))




#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
   
def str2float(s):
    def fn1 (x,y):
        return (x*10+y)
    def fn2 (x,y):
        return (x/10+y)
    def char2num(str):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[str]
    if '.' in s:
        pos = s.index('.')
        first = float(reduce(fn1,map(char2num,s[0:pos])))
        second = float(reduce(fn2,map(char2num,s[len(s):pos:-1])))
        return first + second/10
    else:
        return float(reduce(fn1,map(char2num,s)))


print(str2float('1234.56'))

def is_palindrome(n):
    T = str(n)
    for i in range(len(T)):
        if T[i] != T[len(T)-i-1]:
            return False
    return T

def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_age(t):
    return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_age)
print(L2)
print(L3)

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x =  x + 1
        return x
    return counter



def createCounter():
    def numgenerator():
        num = 0
        while True:
            num += 1
            yield num
    myint = numgenerator()
    def counter():
        return (next(myint))
    
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

#装饰器decorator

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

#或者针对带参数的decorator：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print("2015-3-25")

now()


#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        begin = time.time()
        print('%s executed start: %s ' % (fn.__name__, begin))
        result = fn(*args,**kw)
        end = time.time()
        print('%s executed end: %s ' % (fn.__name__, end))
        print('%s executed in : %.2f ms' % (fn.__name__, (end - begin)*1000 ))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
f = fast(11, 22)
print(f)
'''


