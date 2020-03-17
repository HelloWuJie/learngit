#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#利用os模块编写一个能实现dir -l输出的程序

#total 0
#-rw-rw-rw- 1 wujie wujie   43 Mar 17 15:17 dir.py
#drwxrwxrwx 1 wujie wujie 4096 Mar 17 15:13 test
import os,time

for dir_items in os.listdir('.'):
    statinfo  = os.stat(dir_items)
    curr_year = time.localtime(statinfo.st_atime).tm_year
    if curr_year == time.localtime().tm_year:
        print(time.strftime("%b %d %H:%M:%S",time.localtime(statinfo.st_atime)))
    else:
        print(time.strftime("%b %d %Y", time.localtime(statinfo.st_atime)))



