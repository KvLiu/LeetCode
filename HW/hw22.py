# -*- coding: utf-8 -*-
"""
假设渊子原来一个BBS上的密码为YUANzhi1987,为了方便记忆，他通过一种算法把这个密码变换成zvbo9441987，
这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
他是这么变换的，大家都知道手机上的字母：
1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。
记住，z往后移是a哦。
输入描述:
输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾
输出描述:
输出渊子真正的密文
示例1
输入
YUANzhi1987
输出
zvbo9441987
"""
#Solution1: 将字符串转换为列表挨个处理每个元素
while 1:
    try:
        pass
        s1 = list(raw_input())
        for i in range(len(s1)):
            if s1[i] in 'abc':
                s1[i]='2'
            elif s1[i] in 'def':
                s1[i]='3'
            elif s1[i] in 'ghi':
                s1[i]='4'
            elif s1[i] in 'jkl':
                s1[i]='5'
            elif s1[i] in 'mno':
                s1[i]='6'
            elif s1[i] in 'pqrs':
                s1[i]='7'
            elif s1[i] in 'tuv':
                s1[i]='8'
            elif s1[i] in 'wxyz':
                s1[i]='9'
            elif s1[i] =='Z':
                s1[i]='a'
            elif s1[i].isalpha():
                s1[i]= chr(ord(s1[i].lower())+1)
        print "".join(s1)
    except:
        break
#Solution2： 定义一个空字符串s，遍历输入字符串的每个每个元素并加入s
