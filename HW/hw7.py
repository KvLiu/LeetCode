# -*- coding: utf-8 -*-
# 百钱买百鸡
while True:
    try:
        a= raw_input()
        if int(a):
            for x in xrange(0,20):
                for y in xrange(0,34):
                    for z in xrange(0,100,3):
                        if (x+y+z) == 100 and (5*x+3*y+z/3)==100:
                            print '%d %d %d'%(x,y,z)
    except:
        break
