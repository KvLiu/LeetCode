# -*- coding: utf-8 -*-
#实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
# 输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
#Reference:https://www.nowcoder.com/profile/5426857/codeBookDetail?submissionId=12385563
#Solution1:
def delete(s):
    minlen= len(s)
    l = list(s)
    for i in l:
        if l.count(i) <minlen:
            minlen= l.count(i)
    newl =[]
    for i in l:
        if l.count(i)==minlen:
           pass
        else:
            newl.append(i)

    return "".join(newl)

while True:
    try:
        s = raw_input()
        print delete(s)
    except:
        break
#Solution2: 使用字典方式：答案错误，仍需修改，例如输入：aabbccc 输出abccc
def delete(s):
    li= list(s)
    di = {}
    for i in li:
        if i in di.keys():
            di[i] = di[i]+1
        else:
            di[i]=1
    minlen =min(di.values())

    for i in di:
        if di[i] == minlen:
            li.remove(i)
    return ''.join(li)

while True:
    try:
        s = raw_input()
        print delete(s)
    except:
        break
