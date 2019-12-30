# -*- coding:utf-8 -*-
#验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
 #输入参数：
 #    int m：整数(取值范围：1～100)
 #返回值：
 #    m个连续奇数(格式：“7+9+11”);
#--------------数学证明---------------------
#对于任一正整数a,不论a是奇数还是偶数，整数(a×a-a+1)必然为奇数。
#构造一个等差数列，数列的首项为(a×a-a+1),等差数列的差值为2(奇数数列)，则前a项的和为：
#a×((a×a-a+1))+2×a(a-1)/2
#=a×a×a-a×a+a+a×a-a
#=a×a×a
#-----------------------------------
while True:
    try:
        m = int(raw_input())
        # a1 is the first odd numuber
        a1= m*m- m+ 1
        res=str(a1)
        for i in range(1,m):
            res = res+"+"+str(a1+ 2*i)
        print res
    except:
        break
