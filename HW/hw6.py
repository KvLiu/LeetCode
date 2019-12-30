# -*- coding:utf-8 -*-
#给定一个字符串描述的算术表达式，计算出结果值。
while True:
    try:
        str1 = raw_input()
        print eval(str1)
    except:
        break
