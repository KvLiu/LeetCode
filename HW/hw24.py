# -*- coding:utf-8 -*-
"""字符统计
实现以下接口：输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）
按照统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASII码由小到大排序输出
清空目前的统计结果，重新统计
调用者会保证：
输入的字符串以‘\0’结尾。
输入描述:
输入一串字符。
输出描述:
对字符中的各个英文字符（大小写分开统计），数字，空格进行统计，并按照统计个数由多到少输出,如果统计的个数相同，则按照ASII码由小到大排序输出 。
如果有其他字符，则对这些字符不用进行统计。
示例1
输入
aadddccddc
输出
dca
"""
while True:
    try:
        s=raw_input()
        d = {}
        for i in s:
            if i.isalnum() or i.isspace():
                if d.has_key(i):
                    d[i] = d[i]+1
                else:
                    d[i] = 1
        string = ''
        #第一次排序，根据字典key排序，得到元组列表
        li1 = sorted(d.items(),key = lambda x:x[0])
        #第二次排序，根据元组列表第二个值排序
        li2 = sorted(li1,key = lambda x:x[1],reverse = True)
        for i in li2:
            string += i[0]
        print string
    except:
        break
