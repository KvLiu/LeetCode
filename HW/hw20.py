# -*- coding:utf-8 -*-
"""
reference:https://www.nowcoder.com/profile/8426185/codeBookDetail?submissionId=12275751
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
       如，输入： Type   输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
     如，输入： BabA   输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
     如，输入： By?e   输出： Be?y
样例：
    输入：A Famous Saying: Much Ado About Nothing(2012/8).

    输出：A aaAAbc dFgghh: iimM nNn oooos Sttuuuy(2012/8).
"""
while True:
    try:
        str1 = raw_input()
        char_list=sorted(str1,key = str.lower)
        li = []
        for i in char_list:
            if i.isalpha():
                li.append(i)
        for i in xrange(len(str1)):
            if not str1[i].isalpha():
                li.insert(i,str1[i])

        print "".join(li)
    except:
        break
