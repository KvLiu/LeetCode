# -*- coding:utf-8 -*-
#给定n个字符串，请对n个字符串按照字典序排列。
#输入描述:
#输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
#输出描述:
#数据输出n行，输出结果为按照字典序排列的字符串。
while True:
    try:
        n = int(raw_input())
        l=[]
        for i in range(n):
            l.append(raw_input())
        l.sort()
        for i in l:
            print i
    except:
        break
