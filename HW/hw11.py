# 二维数组操作
# -*- coding:utf-8 -*-
while True:
    try:
        m, n = raw_input().split()
        m = int(m)
        n = int(n)
        r1,c1,r2,c2= raw_input().split()
        new_row= int(raw_input())
        new_col= int(raw_input())
        chk_row,chk_col= raw_input().split()
        if m<10 and n<10:
            print 0
        else:
            print -1
        if int(r1)<m and int(r2)<m and int(c1)<n and int(c2)<n:
            print 0
        else:
            print -1
        if new_row < m:
           # m+=1
            print 0
        else:
            print -1
        if new_col < n:
          #  n+=1
            print 0
        else:
            print -1
        if  int(chk_row) < m and int(chk_col)< n:
            print 0
        else:
            print -1
    except:
        break
