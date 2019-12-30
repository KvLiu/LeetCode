# -*- coding: utf-8 -*-
#按照字节截取字符串
while True:
    try:
        str1,int1 = raw_input().split()
        int1 = int(int1)
        if str1[int1-1].isalpha():
            print str1[:int1]
        else:
            print str1[:int1-1]
    except:
        break
