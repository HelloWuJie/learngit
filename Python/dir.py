#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#利用os模块编写一个能实现dir -l输出的程序

#total 0
#-rw-rw-rw- 1 wujie wujie   43 Mar 17 15:17 dir.py
#drwxrwxrwx 1 wujie wujie 4096 Mar 17 15:13 test
import os, time
import pwd,grp


dict_priv = {'7':'rwx','6':'rw-','5':'r-x','4':'r--','3':'-wx','2':'-w-','1':'--x','0':'---'}
for dir_items in os.listdir('.'):
    statinfo  = os.stat(dir_items)
    #获取权限的字符串格式
    if os.path.isdir(dir_items):
        prefix = 'd'
    else:
        prefix = '-'
    priv = str(oct(statinfo.st_mode)[-3:])
    _str = ''
    for x in priv:
        _str = _str + dict_priv[x]
    priv_str = prefix + _str
    #获取文件属主和属组
    _uid = statinfo.st_uid(dir_items)
    _gid = statinfo.st_gid(dir_items)
    uid_name = pwd.getpwuid(_uid).pw_name
    gid_name = grp.getgrgid(_gid).gr_name
    print(uid_name,gid_name)
    #获取时间的字符串格式
    curr_year = time.localtime(statinfo.st_atime).tm_year
    if curr_year == time.localtime().tm_year:
        time_format = time.strftime("%b %d %H:%M",time.localtime(statinfo.st_atime))
    else:
        time_format = time.strftime("%b %d %Y", time.localtime(statinfo.st_atime))
    print('%s\t%s\t%s' % (priv_str,time_format,dir_items))


