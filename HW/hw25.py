# -*- coding: utf-8 -*-
"""放苹果
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
输入每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。
样例输入
7 3
样例输出
8
* 计算放苹果方法数目
* 输入值非法时返回-1

分析：
放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。
令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。
1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可
2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上
即求(m-n，n)
"""
def f(m,n):
    #递归出口
    #苹果个数小于苹果个数，不存在所有盘子都放满情况,f(m-n,n) = 0
    if m< 0:
        return 0
    # 苹果个数等于盘子个数，f(m-n,n) =1
    if m == 0:
        return 1
    if m ==1 or n==1:
        return 1
    else:
        return f(m,n-1)+ f(m-n,n)

while True:
    try:
        li = raw_input().strip().split()
        if len(li)!=2 or not li[0].isdigit() or not li[1].isdigit():
            print -1
            break
        m = int(li[0])
        n = int(li[1])
        print f(m,n)

    except:
        break
