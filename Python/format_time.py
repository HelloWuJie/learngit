#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#格式化时间函数,输入时间戳
def formatTime(longtime):
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))

print(formatTime(3793937836))
